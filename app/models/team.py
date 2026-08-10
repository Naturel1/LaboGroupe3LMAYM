from app import db
from app.models.base_entity import BaseEntity


class Team(BaseEntity, db.Model):
    """Represents a team of users."""
    __tablename__ = 'teams'

    team_id = db.Column(db.Integer, primary_key=True,
                        autoincrement=True)
    team_name = db.Column(db.String(80), unique=True, nullable=False,
                          index=True)
    team_description = db.Column(db.String(256), nullable=True)

    members = db.relationship('User', back_populates='team')
