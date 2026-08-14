from app.dtos.abstract_dto import AbstractDTO
from app.models.role import Role


class RoleDTO(AbstractDTO):
    def __init__(self):
        self.role_id = None
        self.role_name = None

    @staticmethod
    def build_from_entity(entity: Role) -> "RoleDTO":
        role_dto = RoleDTO()

        role_dto.role_id = entity.role_id
        role_dto.role_name = entity.role_name

        return role_dto

    def get_json_parsable(self):
        return self.__dict__