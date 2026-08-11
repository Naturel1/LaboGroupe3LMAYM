from app import db
from app.models.base_entity import BaseEntity


class Equipment(BaseEntity, db.Model):
    """Represents hardware or equipment assigned to a site or user."""
    __tablename__ = 'equipments'

    equipment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    equipment_name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(80), nullable=False)
    equipment_serial = db.Column(db.String(100), nullable=False, unique=True)
    equipment_purchase_date = db.Column(db.DateTime, nullable=False)
    equipment_site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'),
                        nullable=False)
    equipment_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                        nullable=True)

    # Add relationships
    site = db.relationship('Site', back_populates='equipments', cascade='all, delete-orphan')
    user = db.relationship('User', back_populates='equipments', cascade='all, delete-orphan')
