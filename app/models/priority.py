from app import db
from app.models.base_entity import BaseEntity


class Priority(BaseEntity, db.Model):
    """Represents a ticket priority level and its resolution delay."""

    __tablename__ = 'priorities'

    priority_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    priority_name = db.Column(db.String(100), nullable=False, unique=True)
    priority_level = db.Column(db.Integer, nullable=False)
    priority_delay_hours = db.Column(db.Integer, nullable=False)
