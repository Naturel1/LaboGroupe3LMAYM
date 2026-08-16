from app.dtos.abstract_dto import AbstractDTO

class EquipmentDTO(AbstractDTO):
    def __init__(self):
        self.equipment_id = None
        self.equipment_name = None
        self.equipment_type = None
        self.equipment_serial = None
        self.equipment_purchase_date = None
        self.equipment_site_id = None
        self.equipment_user_id = None

    @staticmethod
    def build_from_entity(entity):
        dto = EquipmentDTO()
        dto.equipment_id = entity.equipment_id
        dto.equipment_name = entity.equipment_name
        dto.equipment_type = entity.equipment_type
        dto.equipment_serial = entity.equipment_serial
        dto.equipment_purchase_date = entity.equipment_purchase_date
        dto.equipment_site_id = entity.equipment_site_id
        dto.equipment_user_id = entity.equipment_user_id
        return dto

    def get_json_parsable(self):
        return dict(self.__dict__)