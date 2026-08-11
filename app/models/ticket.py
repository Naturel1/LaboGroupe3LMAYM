from app import db
from app.models.base_entity import BaseEntity
from app.models.ticket_status_history import TicketStatusHistory


class Ticket(BaseEntity, db.Model):
    """Represents a support ticket in the system."""

    __tablename__ = 'tickets'

    ticket_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ticket_title = db.Column(db.String(64), nullable=False)
    ticket_description = db.Column(db.String(255), nullable=True)
    ticket_status = db.Column(db.String(64), nullable=False)
    ticket_due_date = db.Column(db.DateTime, nullable=True)
    ticket_author_id = db.Column(
        db.Integer, db.ForeignKey('users.user_id'), nullable=False
    )
    ticket_technician_id = db.Column(
        db.Integer, db.ForeignKey('users.user_id'), nullable=True
    )
    ticket_category_id = db.Column(
        db.Integer, db.ForeignKey('categories.category_id'), nullable=False
    )
    ticket_priority_id = db.Column(
        db.Integer, db.ForeignKey('priorities.priority_id'), nullable=False
    )
    ticket_equipment_id = db.Column(
        db.Integer, db.ForeignKey('equipments.equipment_id'), nullable=True
    )

    # Add relationships
    author = db.relationship(
        'User', foreign_keys=[ticket_author_id],
        back_populates='tickets_created'
    )
    technician = db.relationship(
        'User', foreign_keys=[ticket_technician_id],
        back_populates='tickets_assigned'
    )
    category = db.relationship('Category', back_populates='category_tickets')
    priority = db.relationship('Priority', back_populates='priority_tickets')
    equipment = db.relationship(
        'Equipment', back_populates='equipment_tickets'
    )
    comments = db.relationship(
        'Comment', back_populates='ticket', cascade='all, delete-orphan',
        foreign_keys='Comment.comment_ticket_id'
    )
    histories = db.relationship(
        'TicketStatusHistory', back_populates='ticket',
        cascade='all, delete-orphan',
        foreign_keys='TicketStatusHistory.ticket_status_history_ticket_id'
    )
    attachments = db.relationship(
        'Attachment', back_populates='ticket', cascade='all, delete-orphan',
        foreign_keys='Attachment.attachment_ticket_id'
    )
    satisfaction_survey = db.relationship(
        'SatisfactionSurvey', back_populates='ticket', cascade='all, delete-orphan',
        foreign_keys='SatisfactionSurvey.satisfaction_survey_ticket_id'
    )
    tags = db.relationship(
        'TicketTag', back_populates='rel_ticket', cascade='all, delete-orphan',
        foreign_keys='TicketTag.ticket_tag_ticket_id'
    )
    interventions = db.relationship(
        'Intervention', back_populates='ticket', cascade='all, delete-orphan',
        foreign_keys='Intervention.intervention_ticket_id'
    )

    def change_status(self, new_status):
        """Change the status and log the change in status history."""

        history_entry = TicketStatusHistory(
            ticket_id=self.ticket_id,
            user_id=self.ticket_technician_id or self.ticket_author_id,
            old_status=self.ticket_status,
            new_status=new_status
        )
        db.session.add(history_entry)
        self.ticket_status = new_status
        db.session.commit()
