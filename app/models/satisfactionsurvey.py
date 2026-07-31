from app import db
from app.models.base_entity import BaseEntity


class Satisfactionsurvey(BaseEntity, db.Model):
    """
    to do
    """
    __tablename__ = 'satisfactionsurveys'

    __table_args__ = (
        db.CheckConstraint('satisfactionsurveys_rating >=1 AND satisfactionsurveys_rating <=5', name='Rating_range'),
    )

    satisfactionsurveys_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    satisfactionsurveys_rating = db.Column(db.Integer, nullable=False)
    satisfactionsurveys_comment = db.Column(db.Text, nullable=True)

    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'), nullable=False, unique=True)
    client_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)

    ticket = db.relationship('Ticket', back_populates='survey', uselist=False)
    client = db.relationship('User', back_populates='surveys')
