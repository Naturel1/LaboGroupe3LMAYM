from app import db
from app.models.base_entity import BaseEntity


class Intervention(BaseEntity, db.Model):
    """Represents an intervention carried out by a technician on a ticket."""

    __tablename__ = 'interventions'

    intervention_id = db.mapped_column(db.Integer, primary_key=True,
                                autoincrement=True)
    intervention_date = db.mapped_column(db.DateTime(timezone=True), nullable=False)
    intervention_duration = db.mapped_column(db.Integer, nullable=False) # Duration expressed in minutes
    intervention_report = db.mapped_column(db.String(256), nullable=False)
    intervention_ticket_id = db.mapped_column(db.ForeignKey('tickets.ticket_id'), nullable=False)
    intervention_technician_id = db.mapped_column(db.ForeignKey('users.user_id'), nullable=False)
    intervention_type_id = db.mapped_column(
        db.ForeignKey('intervention_types.intervention_type_id'),
        nullable=False
    )

    # Add relationships
    ticket = db.relationship('Ticket', back_populates='interventions')
    technician = db.relationship('User', back_populates='interventions')
    intervention_type = db.relationship('InterventionType',
                                        back_populates='interventions')

    def __repr__(self):
        return f"<Intervention {self.intervention_id} ticket={self.intervention_ticket_id}>"
