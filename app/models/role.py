from app import db
from app.models.base_entity import BaseEntity


class Role(BaseEntity, db.Model):
    """Represents a user role within the system."""
    __tablename__ = 'roles'

    role_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True)
    role_name = db.Column(db.String(80), unique=True, nullable=False,
                          index=True)

    # Add relationships
    users = db.relationship('UserRole', back_populates='role',
                            foreign_keys='UserRole.user_role_role_id', cascade='all, delete-orphan')
