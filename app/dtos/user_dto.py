from app.dtos.abstract_dto import AbstractDTO


class UserDTO(AbstractDTO):
    """A user as seen by the views (templates, JSON responses...)."""
    
    def __init__(self):
        self.user_id = None
        self.username = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.description = None
        self.email_verified = None



    @staticmethod
    def build_from_entity(user) -> "UserDTO":
        """Build a UserDTO from a User entity."""

        user_dto = UserDTO()

        user_dto.user_id = user.user_id
        user_dto.username = user.username
        user_dto.firstname = user.firstname
        user_dto.lastname = user.lastname
        user_dto.email = user.email
        user_dto.description = user.description
        user_dto.email_verified = user.email_verified

        return user_dto


    def get_json_parsable(self):
        """Return a dict of base types, ready for jsonify()."""

        data = dict(self.__dict__)
        return data