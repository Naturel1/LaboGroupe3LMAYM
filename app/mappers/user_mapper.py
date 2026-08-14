from app.dtos.user_dto import UserDTO
from app.forms.user.user_login_form import UserLoginForm
from app.forms.user.user_register_form import UserRegisterForm
from app.forms.user.user_update_form import UserUpdateForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.user import User

class UserMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: User) -> UserDTO:
        return UserDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form, user: User) -> User:

        if isinstance(form, UserRegisterForm):
            user.user_username = form.username.data
            user.user_firstname = form.firstname.data
            user.user_lastname = form.lastname.data
            user.user_email = form.email.data
            user.user_password = form.password.data

        elif isinstance(form, UserLoginForm):
            user.user_username = form.username.data
            user.user_password = form.password.data

        elif isinstance(form, UserUpdateForm):
            user.user_email = form.email.data

        return user