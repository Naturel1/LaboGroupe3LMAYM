from app import app, db
from app.dtos.ticket_dto import TicketDTO
from app.forms.ticket.ticket_create_form import TicketCreateForm
from app.forms.ticket.ticket_update_form import TicketUpdateForm
from app.framework.decorators.injectable import injectable
from app.mappers.ticket_mapper import TicketMapper
from app.models.ticket import Ticket
from app.services.base_service import BaseService
from app.services.user_service import UserService
from app.services.priority_service import PriorityService
from datetime import datetime, timedelta


@injectable
class TicketService(BaseService):
    """
    Provides implementation of ticket service.
    """

    def find_all(self) -> list[TicketDTO]:
        return [TicketMapper.entity_to_dto(ticket)
                for ticket in Ticket.query.filter_by(active=True).order_by(Ticket.ticket_id).all()]

    def find_one(self, entity_id: int) -> TicketDTO | None:
        ticket = self.find_one_entity(entity_id)
        return TicketMapper.entity_to_dto(ticket) if ticket else None

    def find_one_entity(self, entity_id: int) -> Ticket | None:
        return Ticket.query.filter_by(ticket_id=entity_id, active=True).first()

    def find_one_by(self, **kwargs) -> TicketDTO | None:
        ticket = Ticket.query.filter_by(active=True, **kwargs).first()
        return TicketMapper.entity_to_dto(ticket) if ticket else None

    def insert(self, form: TicketCreateForm) -> TicketDTO | None:
        ticket = Ticket()
        TicketMapper.form_to_entity(form, ticket)
        user_service = UserService()
        author = user_service.get_current_user()
        if author is None:
            app.logger.error("insert ticket: no current user found")
            return None
        ticket.ticket_author_id = author.user_id
        ticket.ticket_status = 'open'
        delay_hours = PriorityService.find_one_entity(ticket.ticket_priority_id).priority_delay_hours
        ticket.ticket_due_date = datetime.now() + timedelta(hours=delay_hours)
        try:
            db.session.add(ticket)
            db.session.commit()
        except Exception as e:
            app.logger.error(f"insert ticket: {e}")
            db.session.rollback()
            return None
        return TicketMapper.entity_to_dto(ticket)

    def update(self, entity_id: int, form: TicketUpdateForm) -> TicketDTO | None:
        ticket = self.find_one_entity(entity_id)
        if ticket is None:
            return None
        TicketMapper.form_to_entity(form, ticket)
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"update ticket {entity_id}: {e}")
            db.session.rollback()
            return None
        return TicketMapper.entity_to_dto(ticket)

    def delete(self, entity_id: int) -> int | None:
        ticket = self.find_one_entity(entity_id)
        if ticket is None:
            return None
        ticket.active = False
        try:
            db.session.commit()
        except Exception as e:
            app.logger.error(f"delete ticket {entity_id}: {e}")
            db.session.rollback()
            return None
        return entity_id