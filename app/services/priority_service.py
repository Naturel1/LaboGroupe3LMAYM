from app import app, db
from app.dtos.priority_dto import PriorityDTO
from app.forms.priority.priority_form import PriorityForm
from app.framework.decorators.injectable import injectable
from app.mappers.priority_mapper import PriorityMapper
from app.models.priority import Priority
from app.services.base_service import BaseService


@injectable
class PriorityService(BaseService):
    """
    Provides implementation of priority service.
    """

    def find_all(self) -> list[PriorityDTO]:
        return [PriorityMapper.entity_to_dto(priority)
                for priority in Priority.query.filter_by(active=True).order_by(Priority.priority_id).all()]

    def find_one(self, entity_id: int) -> PriorityDTO | None:
        priority = self.find_one_entity(entity_id)
        return PriorityMapper.entity_to_dto(priority) if priority else None

    def find_one_entity(self, entity_id: int) -> Priority | None:
        return Priority.query.filter_by(priority_id=entity_id, active=True).first()

    def find_one_by(self, **kwargs) -> PriorityDTO | None:
        priority = Priority.query.filter_by(active=True, **kwargs).first()
        return PriorityMapper.entity_to_dto(priority) if priority else None

    def insert(self, form: PriorityForm) -> PriorityDTO | None:
        priority = Priority()
        PriorityMapper.form_to_entity(form, priority)
        try:
            db.session.add(priority)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert priority: {e}")
            db.session.rollback()
            return None
        return PriorityMapper.entity_to_dto(priority)

    def update(self, entity_id: int, form: PriorityForm) -> PriorityDTO | None:
        priority = self.find_one_entity(entity_id)
        if priority is None:
            return None
        PriorityMapper.form_to_entity(form, priority)
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update priority {entity_id}: {e}")
            db.session.rollback()
            return None
        return PriorityMapper.entity_to_dto(priority)

    def delete(self, entity_id: int) -> int | None:
        priority = self.find_one_entity(entity_id)
        if priority is None:
            return None
        priority.active = False
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete priority {entity_id}: {e}")
            db.session.rollback()
            return None
        return entity_id