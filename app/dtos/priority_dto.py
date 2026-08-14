from app.dtos.abstract_dto import AbstractDTO


class PriorityDTO(AbstractDTO):
    """
    Data Transfer Object for Priority entity.
    """

    def __init__(self):
        self.priority_id = None
        self.name = None
        self.level = None
        self.delay_hours = None

    @staticmethod
    def build_from_entity(entity) -> "PriorityDTO":
        priority_dto = PriorityDTO()
        priority_dto.priority_id = entity.priority_id
        priority_dto.name = entity.name
        priority_dto.level = entity.level
        priority_dto.delay_hours = entity.delay_hours
        return priority_dto

    def get_json_parsable(self):
        return self.__dict__