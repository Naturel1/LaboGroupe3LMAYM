from app import db
from app.models.base_entity import BaseEntity

class TicketTag(BaseEntity, db.Model):
    """Association table for Ticket <-> Tag .
    """

    __tablename__ = 'ticket_tags'

    tag_id = db.Column(db.ForeignKey('tags.tag_id'), primary_key=True)
    ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'), primary_key=True)

    rel_tag = db.relationship('Tag', back_populates='rel_ticket')
    rel_ticket = db.relationship('Ticket', back_populates='tags')