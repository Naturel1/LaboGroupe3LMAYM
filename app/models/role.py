from app import db
from app.models.base_entity import BaseEntity


class Role(BaseEntity, db.Model):
    """Represents a user role within the system."""
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False,
                          index=True)

    users = db.relationship('UserRole', back_populates='role',
                            cascade='all, delete-orphan')
