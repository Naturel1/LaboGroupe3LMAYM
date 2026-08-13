from app import db
from app.models.base_entity import BaseEntity


class Tag(BaseEntity, db.Model):
    """Represents a label that can be attached to one or more tickets."""

    __tablename__ = 'tags'

    tag_id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    tag_name = db.mapped_column(db.String(64), unique=True, nullable=False)
    tag_color = db.mapped_column(db.String(7), nullable=False)

    # Add relationships
    rel_ticket = db.relationship('TicketTag', back_populates='rel_tag', cascade='all, delete-orphan',
                                 foreign_keys='TicketTag.ticket_tag_tag_id')
