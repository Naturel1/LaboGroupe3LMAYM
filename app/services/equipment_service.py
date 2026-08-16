from app import db
from app.framework.decorators.injectable import injectable
from app.services.base_service import BaseService
from app.models.equipment import Equipment
from app.forms.equipment.equipment_form import EquipmentForm
from app.mappers.equipment_mapper import EquipmentMapper


@injectable
class EquipmentService(BaseService):
    def find_all(self):
        return [EquipmentMapper.entity_to_dto(eq) for eq in Equipment.query.filter_by(active=True).all()]

    def find_one(self,equipment_id):
        eq = Equipment.query.filter_by(equipment_id=equipment_id, active=True).first()
        return EquipmentMapper.entity_to_dto(eq) if eq else None

    def find_one_by(self, **kwargs):
        eq = Equipment.query.filter_by(active=True, **kwargs).first()
        return EquipmentMapper.entity_to_dto(eq) if eq else None

    def insert(self, form: EquipmentForm):
        eq = Equipment()
        eq = EquipmentMapper.form_to_entity(form, eq)
        db.session.add(eq)
        db.session.commit()
        return EquipmentMapper.entity_to_dto(eq)

    def update(self, equipment_id, form: EquipmentForm):
        eq = Equipment.query.filter_by(equipment_id=equipment_id, active=True).first()
        if eq is None:
            return None
        eq = EquipmentMapper.form_to_entity(form, eq)
        db.session.commit()
        return EquipmentMapper.entity_to_dto(eq)

    def delete(self, equipment_id):
            eq = self.find_one(equipment_id)
            if eq is None:
                return None
            eq.active = False
            db.session.commit()
            return eq