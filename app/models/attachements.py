from app import db
from app.models.base_entity import BaseEntity

class Attachement(BaseEntity, db.Model):
    """
    To do
    """

    __tablename__ = 'attachements'

    attachement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    attachement_filename = db.Column(db.String(255), unique=True, index=True)
    attachement_path = db.Column(db.String(255))
    attachement_size = db.Column(db.Integer)
    attachement_ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'))
    attachement_author_id = db.Column(db.ForeingKey('users.user_id'))

    #Add relationships
