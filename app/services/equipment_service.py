from app import db
from app.framework.decorators.injectable import injectable
from app.models.user import User
from app.services.base_service import BaseService
from app.models.equipment import Equipment
from app.forms.equipment.equipment_form import EquipmentForm
from app.mappers.equipment_mapper import EquipmentMapper


@injectable
class EquipmentService(BaseService):
    def find_all(self):
        return [EquipmentMapper.entity_to_dto(eq) for eq in Equipment.query.filter_by(active=True).all()]

    def find_one(self,equipment_id):
        eq = self.find_one_entity(equipment_id)
        return EquipmentMapper.entity_to_dto(eq) if eq else None

    def find_one_entity(self, entity_id: int):
        return Equipment.query.filter_by(equipment_id=entity_id, active=True).first()

    def find_one_by(self, **kwargs):
        return Equipment.query.filter_by(active=True, **kwargs).first()

    def insert(self, form: EquipmentForm):
        eq = Equipment()
        eq = EquipmentMapper.form_to_entity(form, eq)
        db.session.add(eq)
        db.session.commit()
        return EquipmentMapper.entity_to_dto(eq)

    def update(self, equipment_id, form: EquipmentForm):
        eq = self.find_one_entity(equipment_id)
        if eq is None:
            return None
        eq = EquipmentMapper.form_to_entity(form, eq)
        db.session.commit()
        return EquipmentMapper.entity_to_dto(eq)

    def delete(self, equipment_id):
        eq = self.find_one(equipment_id)
        if eq is None:
            return None
        eq.soft_delete()
        db.session.commit()
        return eq.equipment_id
