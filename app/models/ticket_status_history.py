from app import db
from app.models.base_entity import BaseEntity


class TicketStatusHistory(BaseEntity, db.Model):
    """Represents the history of status changes for a ticket."""

    __tablename__ = 'ticket_status_histories'

    ticket_status_history_id = db.mapped_column(db.Integer, primary_key=True,
                                       autoincrement=True)
    ticket_status_history_ticket_id = db.mapped_column(
        db.ForeignKey('tickets.ticket_id')
    )
    ticket_status_history_user_id = db.mapped_column(db.ForeignKey('users.user_id'))
    ticket_status_history_old_status = db.mapped_column(db.String(16), nullable=False,
                                                 default='')
    ticket_status_history_new_status = db.mapped_column(db.String(16), nullable=False)

    # Add relationships
    ticket = db.relationship('Ticket', back_populates='histories')
    user = db.relationship('User', back_populates='ticket_status_histories')
