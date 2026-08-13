from app.dtos.role_dto import RoleDTO
from app.framework.decorators.injectable import injectable
from app.models.role import Role
from app.services.base_service import BaseService


@injectable
class RoleService(BaseService):
    """Role management."""

    def find_all(self) -> list[RoleDTO]:
        return [RoleDTO.build_from_entity(role) for role in Role.query.all()]

    def find_all_entities(self) -> list[Role]:
        return Role.query.order_by(Role.role_id).all()

    def find_one(self, entity_id: int) -> RoleDTO | None:
        role = self.find_one_entity(entity_id)

        return RoleDTO.build_from_entity(role) if role else None

    def find_one_entity(self, entity_id: int) -> Role | None:
        return Role.query.filter_by(role_id = entity_id).first()

    def find_on_by(self, **kwargs) -> Role | None:
        return Role.query.filter_by(**kwargs).first()

    def insert(self, data):
        raise NotImplementedError("Roles are create by seeds/mogration")

    def update(self, entity_id: int, data):
        raise NotImplementedError("Roles are create by seeds/mogration")

    def delete(self, entity_id: int):
        raise NotImplementedError("Roles are create by seeds/mogration")