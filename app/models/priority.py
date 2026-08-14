from app import db
from app.models.base_entity import BaseEntity


class Priority(BaseEntity, db.Model):
    """Represents a ticket priority level and its resolution delay."""

    __tablename__ = 'priorities'

    priority_id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    priority_name = db.mapped_column(db.String(100), nullable=False, unique=True)
    priority_level = db.mapped_column(db.Integer, nullable=False)
    priority_delay_hours = db.mapped_column(db.Integer, nullable=False)

    # Add relationships
    tickets = db.relationship('Ticket', back_populates='priority',
                              foreign_keys='Ticket.ticket_priority_id', cascade='all, delete-orphan')
