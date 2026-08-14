from app.dtos.abstract_dto import AbstractDTO


class TicketDTO(AbstractDTO):
    """
    Data Transfer Object for Ticket entity.
    """

    def __init__(self):
        self.ticket_id = None
        self.title = None
        self.description = None
        self.status = None
        self.due_date = None
        self.author_id = None
        self.technician_id = None
        self.category_id = None
        self.priority_id = None
        self.equipment_id = None

    @staticmethod
    def build_from_entity(entity) -> "TicketDTO":
        ticket_dto = TicketDTO()
        ticket_dto.ticket_id = entity.ticket_id
        ticket_dto.title = entity.ticket_title
        ticket_dto.description = entity.ticket_description
        ticket_dto.status = entity.ticket_status
        ticket_dto.due_date = entity.ticket_due_date
        ticket_dto.author_id = entity.ticket_author_id
        ticket_dto.technician_id = entity.ticket_technician_id
        ticket_dto.category_id = entity.ticket_category_id
        ticket_dto.priority_id = entity.ticket_priority_id
        ticket_dto.equipment_id = entity.ticket_equipment_id
        return ticket_dto

    def get_json_parsable(self):
        return self.__dict__