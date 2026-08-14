from flask import session

from app.dtos.user_dto import UserDTO
from app.framework.decorators.inject import inject
from app.framework.decorators.injectable import injectable
from app.framework.injector import Scope
from app.services.auth_service import AuthService
from app.services.user_service import UserService


@injectable(base=AuthService, scope=Scope.SCOPED)
class AuthServiceImpl(AuthService):
    """Provides implementation of authentication service."""

    @inject
    def __init__(self, user_service: UserService):
        self.__user_service = user_service
        self.__current_user: UserDTO | None = None
        self.__loaded: bool = False

    def get_current_user(self) -> UserDTO | None:
        if not self.__loaded:
            self.__loaded = True
            user_id = session.get("user_id")

            if user_id is not None:
                self.__current_user = self.__user_service.find_one(user_id)

                if self.__current_user is None:
                    session.pop("user_id", None)
        return self.__current_user

    def login(self, user: UserDTO):
        session["user_id"] = user.user_id
        session.permanent = True
        self.__current_user = user
        self.__loaded = True

    def logout(self):
        session.clear()
        self.__current_user = None
        self.__loaded = True # Todo : check if needed

    def is_authenticated(self) -> bool:
        return self.__current_user is not None
