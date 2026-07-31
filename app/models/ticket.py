from app import db
from app.models.base_entity import BaseEntity

class Ticket(BaseEntity, db.Model):
    """
    TO DO: Add a description for the Ticket model.
    """

    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_title = db.Column(db.String(64), nullable=False)
    ticket_description = db.Column(db.String(255), nullable=True)
    ticket_status = db.Column(db.String(64), nullable=False)
    ticket_due_date = db.Column(db.DateTime, nullable=True)
    ticket_author_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    ticket_technician_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=True)
    ticket_category_id = db.Column(db.Integer, db.ForeignKey('categories.category_id'), nullable=False)
    ticket_priority_id = db.Column(db.Integer, db.ForeignKey('priorities.priority_id'), nullable=False)
    ticket_equipment_id = db.Column(db.Integer, db.ForeignKey('equipments.equipment_id'), nullable=True)