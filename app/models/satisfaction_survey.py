from app import db
from app.models.base_entity import BaseEntity


class SatisfactionSurvey(BaseEntity, db.Model):
    """Represents a satisfaction survey completed after a ticket is closed."""
    __tablename__ = 'satisfaction_surveys'

    __table_args__ = (
        db.CheckConstraint(
            'satisfaction_survey_rating >= 1 AND '
            'satisfaction_survey_rating <= 5',
            name='Rating_range'
        ),
    )

    satisfaction_survey_id = db.Column(db.Integer, primary_key=True,
                                       autoincrement=True)
    satisfaction_survey_rating = db.Column(db.Integer, nullable=False)
    satisfaction_survey_comment = db.Column(db.Text, nullable=True)
    satisfaction_survey_ticket_id = db.Column(
        db.Integer, db.ForeignKey('tickets.ticket_id'),
        nullable=False, unique=True
    )
    satisfaction_survey_client_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                          nullable=False)

    # Add relationships
    ticket = db.relationship('Ticket', back_populates='satisfaction_survey', cascade='all, delete-orphan')
    client = db.relationship('User', back_populates='satisfaction_surveys', cascade='all, delete-orphan')
