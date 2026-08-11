from app import db
from app.models.base_entity import BaseEntity


class TicketStatusHistory(BaseEntity, db.Model):
    """Represents the history of status changes for a ticket."""

    __tablename__ = 'ticketstatushistories'

    ticketstatushistory_id = db.Column(db.Integer, primary_key=True,
                                       autoincrement=True)
    ticketstatushistory_ticket_id = db.Column(
        db.ForeignKey('tickets.ticket_id')
    )
    ticketstatushistory_user_id = db.Column(db.ForeignKey('users.user_id'))
    ticketstatushistory_old_status = db.Column(db.String(16), nullable=False,
                                               default='')
    ticketstatushistory_new_status = db.Column(db.String(16), nullable=False)

    # Add relations
