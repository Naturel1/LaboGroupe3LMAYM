from app import app, db
from app.dtos.intervention_dto import InterventionDTO
from app.forms.intervention.intervention_form import InterventionForm
from app.framework.decorators.injectable import injectable
from app.mappers.intervention_mapper import InterventionMapper
from app.models.intervention import Intervention
from app.services.base_service import BaseService


@injectable
class InterventionService(BaseService):

    def find_all(self) -> list[InterventionDTO]:
        return [InterventionMapper.entity_to_dto(intervention)
                for intervention in Intervention.query.filter_by(active=True).order_by(Intervention.intervention_date.desc()).all()]

    def find_one(self, entity_id: int) -> InterventionDTO | None:
        intervention = self.find_one_entity(entity_id)
        return InterventionMapper.entity_to_dto(intervention) if intervention else None

    def find_one_entity(self, entity_id: int) -> Intervention | None:
        return Intervention.query.filter_by(intervention_id = entity_id).first()

    def find_one_by(self, **kwargs) -> InterventionDTO | None:
        intervention = Intervention.query.filter_by(**kwargs).first()
        return InterventionMapper.entity_to_dto(intervention) if intervention else None

    def find_by_ticket(self, ticket_id: int) -> list[InterventionDTO]:
        interventions = Intervention.query.filter_by(intervention_ticket_id=ticket_id, active=True).order_by(Intervention.intervention_date.desc()).all()
        return [InterventionMapper.entity_to_dto(i) for i in interventions]

    def insert(self, form: InterventionForm) -> InterventionDTO | None:
        intervention = Intervention()
        InterventionMapper.form_to_entity(form, intervention)

        try:
            db.session.add(intervention)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert intervention: {e}")
            db.session.rollback()
            return None

        return InterventionMapper.entity_to_dto(intervention)

    def update(self, entity_id: int, form: InterventionForm) -> InterventionDTO | None:
        intervention = self.find_one_entity(entity_id)

        if intervention is None:
            return None

        InterventionMapper.form_to_entity(form,intervention)

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update intervention {entity_id}: {e}")
            db.session.rollback()
            return None

        return InterventionMapper.entity_to_dto(intervention)

    def delete(self, entity_id: int) -> int | None:
        intervention = self.find_one_entity(entity_id)

        if intervention is None:
            return None

        intervention.soft_delete()

        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete intervention {entity_id}: {e}")
            db.session.rollback()
            return None

        return entity_id