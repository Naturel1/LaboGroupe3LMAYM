from app.mappers.abstract_mapper import AbstractMapper
from app.dtos.equipment_dto import EquipmentDTO
from app.models.equipment import Equipment
from app.forms.equipment.equipment_form import EquipmentForm


class EquipmentMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: Equipment):
        return EquipmentDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: EquipmentForm, entity: Equipment):
        entity.equipment_name = form.name.data
        entity.equipment_type = form.equipment_type.data
        entity.equipment_serial = form.serial.data
        entity.equipment_purchase_date = form.purchase_date.data
        entity.equipment_site_id = form.site_id.data
        entity.equipment_user_id = form.user_id.data

        return entity
