from app import db
from app.models.base_entity import BaseEntity


class User(BaseEntity, db.Model):
    """Represents a user (client, technician, or administrator)."""
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String(80), unique=True,
                              nullable=False, index=True)
    user_firstname = db.Column(db.String(64), nullable=False)
    user_lastname = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(128), unique=True, nullable=False,
                           index=True)
    user_password = db.Column(db.String(256), nullable=False)  # hash argon2
    user_team_id = db.Column(db.ForeignKey('teams.team_id'), nullable=True)
    user_site_id = db.Column(db.ForeignKey('sites.site_id'), nullable=True)

    roles = db.relationship('UserRole', back_populates='user',
                            cascade='all, delete-orphan')
    team = db.relationship('Team', back_populates='members')
    site = db.relationship('Site', back_populates='user')

    tickets_created = db.relationship('Ticket', back_populates='author',
                                      foreign_keys='Ticket.ticket_author_id')
    tickets_assigned = db.relationship(
        'Ticket', back_populates='technician',
        foreign_keys='Ticket.ticket_technician_id'
    )
