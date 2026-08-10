from app import db
from app.models.base_entity import BaseEntity


class Tag(BaseEntity, db.Model):
    """Represents a label that can be attached to one or more tickets."""

    __tablename__ = 'tags'

    tag_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.Column(db.String(64), unique=True, nullable=False)
    tag_color = db.Column(db.String(7), nullable=False)

    rel_ticket = db.relationship('TicketTag', back_populates='rel_tag')
