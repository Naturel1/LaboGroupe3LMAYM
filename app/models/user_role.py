from app import db
from app.models.base_entity import BaseEntity


class UserRole(BaseEntity, db.Model):
    """Association table between users and roles."""
    __tablename__ = 'user_roles'

    user_role_user_id = db.mapped_column(db.ForeignKey('users.user_id'),
                                         primary_key=True)
    user_role_role_id = db.mapped_column(db.ForeignKey('roles.role_id'),
                                         primary_key=True)

    # Add relationships
    user = db.relationship('User', back_populates='roles')
    role = db.relationship('Role', back_populates='users')
