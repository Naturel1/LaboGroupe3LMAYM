from app import db
from app.models.base_entity import BaseEntity


class Equipment(BaseEntity, db.Model):
    """Represents hardware or equipment assigned to a site or user."""
    __tablename__ = 'equipments'

    equipment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    equipment_name = db.Column(db.String(100), nullable=False)
    equipment_type = db.Column(db.String(80), nullable=False)
    equipment_serial = db.Column(db.String(100), nullable=False, unique=True)
    equipment_purchasedate = db.Column(db.DateTime, nullable=False)

    site_id = db.Column(db.Integer, db.ForeignKey('sites.site_id'),
                        nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                        nullable=True)

    site = db.relationship('Site', back_populates='equipments')
    user = db.relationship('User', back_populates='equipments')
