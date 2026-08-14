from app.dtos.abstract_dto import AbstractDTO


class UserDTO(AbstractDTO):
    """A user as seen by the views (templates, JSON responses...)."""
    
    def __init__(self):
        self.user_id = None
        self.username = None
        self.firstname = None
        self.lastname = None
        self.email = None
        self.email_verified = None



    @staticmethod
    def build_from_entity(user) -> "UserDTO":
        """Build a UserDTO from a User entity."""

        user_dto = UserDTO()

        user_dto.user_id = user.user_id
        user_dto.username = user.user_username
        user_dto.firstname = user.user_firstname
        user_dto.lastname = user.user_lastname
        user_dto.email = user.user_email
        user_dto.email_verified = None

        return user_dto


    def get_json_parsable(self):
        """Return a dict of base types, ready for jsonify()."""

        data = dict(self.__dict__)
        return data