from app import db
from app.models.base_entity import BaseEntity


class Site(BaseEntity, db.Model):
    """Represents a physical location or site."""
    __tablename__ = 'sites'

    site_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    site_name = db.Column(db.String(100), nullable=False)
    site_address = db.Column(db.String(255), nullable=True)
    site_city = db.Column(db.String(100), nullable=True)

    user = db.relationship('User', back_populates='sites')

    equipment = db.relationship('Equipment', back_populates='sites')
