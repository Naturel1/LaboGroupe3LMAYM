from app import db
from app.models.base_entity import BaseEntity


class InterventionType(BaseEntity, db.Model):
    """Represents a reference table for intervention types."""

    __tablename__ = 'intervention_types'

    intervention_type_id = db.mapped_column(db.Integer, primary_key=True,
                                     autoincrement=True)
    intervention_type_name = db.mapped_column(db.String(64), unique=True,
                                       nullable=False)
    intervention_type_description = db.mapped_column(db.String(256), nullable=False)

    # Add relationships
    interventions = db.relationship('Intervention', back_populates='intervention_type',
                                    foreign_keys='Intervention.intervention_type_id', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<InterventionType {self.intervention_type_name}>"
