from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError, VerificationError, InvalidHashError

from app import app, db
from app.dtos.user_dto import UserDTO
from app.forms.user.user_login_form import UserLoginForm
from app.forms.user.user_register_form import UserRegisterForm
from app.forms.user.user_update_form import UserUpdateForm
from app.framework.decorators.injectable import injectable
from app.mappers.user_mapper import UserMapper
from app.models.role import Role
from app.models.user import User
from app.services.base_service import BaseService


@injectable
class UserService(BaseService):
    """Registration, login, management of users."""

    def __init__(self):
        self.__hasher = PasswordHasher()

    # List all active users (active=True dont show desactivated users)
    def find_all(self) -> list[UserDTO]:
        return [UserMapper.entity_to_dto(user)
                for user in User.query.filter_by(active=True).order_by(User.user_id).all()]

    # Find one user by id (Return a DTO or None)
    def find_one(self, entity_id: int) -> UserDTO | None:
        user = self.find_one_entity(entity_id)
        return UserMapper.entity_to_dto(user) if user else None

    # Find one SQLalchemy entity by any field (Return a User or None)
    def find_one_entity(self, entity_id: int) -> User | None:
        return User.query.filter_by(user_id=entity_id).first()

    # Find one SQLalchemy entity by any field (Return a User or None, used for login)
    def find_one_by(self, **kwargs) -> User | None:
        return User.query.filter_by(**kwargs).first()

    def insert(self, form: UserRegisterForm) -> UserDTO | None:
        """Create a new user. Return the DTO of the new user or None if email/username already exists."""
        user = User()
        UserMapper.form_to_entity(form, user)
        user.user_password = self.__hasher.hash(user.user_password)

        role_user = Role.query.filter_by(role_name="USER").first()
        if role_user is not None:
            user.add_role(role_user)

        try:
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert user: {e}")
            db.session.rollback()
            return None

        return UserMapper.entity_to_dto(user)

    def update(self, entity_id: int, form: UserUpdateForm) -> UserDTO | None:
        """Update email or description of a user."""
        user = self.find_one_entity(entity_id)

        if user is None:
            return None

        UserMapper.form_to_entity(form, user)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update user {entity_id}: {e}")
            db.session.rollback()
            return None

        return UserMapper.entity_to_dto(user)


    def update_password(self, entity_id: int, plain_password: str) -> UserDTO | None:
        """Update the password."""
        user = self.find_one_entity(entity_id)

        if user is None:
            return None

        user.user_password = self.__hasher.hash(plain_password)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update password {entity_id}: {e}")
            db.session.rollback()
            return None

        return UserMapper.entity_to_dto(user)

    def update_roles(self, entity_id: int, roles: list[Role]) -> UserDTO | None:
        """Update the roles of a user."""
        user = self.find_one_entity(entity_id)

        if user is None:
            return None

        wanted = [role.role_name for role in roles]

        for role in roles:
            user.add_role(role)

        for user_role in list(user.roles):
            if user_role.role.role_name not in wanted:
                user.remove_role(user_role.role)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update roles {entity_id}: {e}")
            db.session.rollback()
            return None

        return UserMapper.entity_to_dto(user)

    def delete(self, entity_id: int) -> int | None:
        """Delete a user. 
        Default = soft deleted to keep history of tickets.
        For a real delete: db.session.delete(user)
        The cascades declared on the relationships will remove roles and tickets.

        """
        user = self.find_one_entity(entity_id)

        if user is None:
            return None

        user.soft_delete()

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete user {entity_id}: {e}")
            db.session.rollback()
            return None

        return user.user_id

    def login(self, form: UserLoginForm) -> UserDTO | None:
        """Check username and password."""
        candidate = User()
        UserMapper.form_to_entity(form, candidate)

        user = self.find_one_by(user_username=candidate.user_username, active=True)

        if user is None:
            # Hash password anyway to avoid timing attacks.
            self.__hasher.hash(candidate.user_password)
            return None

        try:
            # Exception raised if invalid password
            self.__hasher.verify(user.user_password, candidate.user_password)
        except (VerifyMismatchError, VerificationError, InvalidHashError):
            return None

        if self.__hasher.check_needs_rehash(user.user_password):
            user.user_password = self.__hasher.hash(candidate.user_password)
            db.session.commit()

        return UserMapper.entity_to_dto(user)
