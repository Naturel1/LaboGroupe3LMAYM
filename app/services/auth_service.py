from abc import ABC, abstractmethod

from app.dtos.user_dto import UserDTO

class AuthService(ABC):
    """

    """
    @abstractmethod
    def get_current_user(self) -> UserDTO | None:
        """If the user is authenticated, return the user DTO."""

    @abstractmethod
    def login(self, user: UserDTO) -> bool:
        """Login the user."""

    @abstractmethod
    def logout(self) -> None:
        """Logout the user."""

    @abstractmethod
    def is_authenticated(self) -> bool:
        """Return True if the user is authenticated."""