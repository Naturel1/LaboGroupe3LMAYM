from app import db
from app.models.base_entity import BaseEntity


class TicketTag(BaseEntity, db.Model):
    """Association table between tickets and tags."""

    __tablename__ = 'ticket_tags'

    ticket_tag_tag_id = db.mapped_column(db.ForeignKey('tags.tag_id'), primary_key=True)
    ticket_tag_ticket_id = db.mapped_column(db.ForeignKey('tickets.ticket_id'), primary_key=True)

    rel_tag = db.relationship('Tag', back_populates='rel_ticket')
    rel_ticket = db.relationship('Ticket', back_populates='tags')
