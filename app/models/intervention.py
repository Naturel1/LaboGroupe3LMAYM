from app import db
from app.models.base_entity import BaseEntity


class Intervention(BaseEntity, db.Model):
    """Represents an intervention carried out by a technician on a ticket."""

    __tablename__ = 'interventions'

    intervention_id = db.Column(db.Integer, primary_key=True,
                                autoincrement=True)
    intervention_date = db.Column(db.DateTime(timezone=True), nullable=False)

    # Duration expressed in minutes
    intervention_duration = db.Column(db.Integer, nullable=False)
    intervention_report = db.Column(db.String(256), nullable=False)

    ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'), nullable=False)
    technician_id = db.Column(db.ForeignKey('users.user_id'), nullable=False)
    intervention_type_id = db.Column(
        db.ForeignKey('intervention_types.intervention_type_id'),
        nullable=False
    )

    ticket = db.relationship('Ticket', back_populates='interventions')
    technician = db.relationship('User', back_populates='interventions')
    intervention_type = db.relationship('InterventionType',
                                        back_populates='interventions')

    def __repr__(self):
        return f"<Intervention {self.intervention_id} ticket={self.ticket_id}>"
