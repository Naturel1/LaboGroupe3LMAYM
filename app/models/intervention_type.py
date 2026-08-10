from app import db
from app.models.base_entity import BaseEntity


class InterventionType(BaseEntity, db.Model):
    """Represents a reference table for intervention types."""

    __tablename__ = 'intervention_types'

    intervention_type_id = db.Column(db.Integer, primary_key=True,
                                     autoincrement=True)
    intervention_type_name = db.Column(db.String(64), unique=True,
                                       nullable=False)
    intervention_type_description = db.Column(db.String(256), nullable=False)

    interventions = db.relationship('Intervention',
                                    back_populates='intervention_type')

    def __repr__(self):
        return f"<InterventionType {self.intervention_type_name}>"
