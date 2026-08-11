from app import db
from app.models.base_entity import BaseEntity


class UserRole(BaseEntity, db.Model):
    """Association table between users and roles."""
    __tablename__ = 'user_roles'

    UserRole_user_id = db.Column(db.ForeignKey('users.user_id'),
                                 primary_key=True)
    UserRole_role_id = db.Column(db.ForeignKey('roles.role_id'),
                                 primary_key=True)

    # Add relationships
    user = db.relationship('User', back_populates='roles', cascade='all, delete-orphan')
    role = db.relationship('Role', back_populates='users', cascade='all, delete-orphan')
