from app.dtos.ticket_dto import TicketDTO
from app.forms.ticket.ticket_create_form import TicketCreateForm
from app.forms.ticket.ticket_update_form import TicketUpdateForm
from app.mappers.abstract_mapper import AbstractMapper
from app.models.ticket import Ticket

class TicketMapper(AbstractMapper):

    @staticmethod
    def entity_to_dto(entity: Ticket) -> TicketDTO:
        return TicketDTO.build_from_entity(entity)

    @staticmethod
    def form_to_entity(form: TicketCreateForm | TicketUpdateForm, ticket: Ticket) -> Ticket:
        if isinstance(form, TicketCreateForm):
            ticket.ticket_title = form.title.data
            ticket.ticket_description = form.description.data
            ticket.ticket_category_id = form.category_id.data
            ticket.ticket_priority_id = form.priority_id.data
            ticket.ticket_equipment_id = form.equipment_id.data
        elif isinstance(form, TicketUpdateForm):
            ticket.ticket_description = form.description.data
            if ticket.ticket_equipment_id is None:
                ticket.ticket_equipment_id = form.equipment_id.data
        return ticket