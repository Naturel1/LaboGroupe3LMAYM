from app import db
from app.models.base_entity import BaseEntity


class Attachment(BaseEntity, db.Model):
    """Represents a file attachment linked to a ticket."""

    __tablename__ = 'attachments'

    attachment_id = db.mapped_column(db.Integer, primary_key=True,
                              autoincrement=True)
    attachment_filename = db.mapped_column(db.String(255), unique=True, index=True)
    attachment_path = db.mapped_column(db.String(255))
    attachment_size = db.mapped_column(db.Integer)
    attachment_ticket_id = db.mapped_column(db.ForeignKey('tickets.ticket_id'))
    attachment_author_id = db.mapped_column(db.ForeignKey('users.user_id'))

    # Add relationships
    ticket = db.relationship('Ticket', back_populates='attachments')
    author = db.relationship('User', back_populates='attachments')
