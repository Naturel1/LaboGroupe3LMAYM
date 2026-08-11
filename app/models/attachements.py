from app import db
from app.models.base_entity import BaseEntity


class Attachment(BaseEntity, db.Model):
    """Represents a file attachment linked to a ticket."""

    __tablename__ = 'attachments'

    attachment_id = db.Column(db.Integer, primary_key=True,
                              autoincrement=True)
    attachment_filename = db.Column(db.String(255), unique=True, index=True)
    attachment_path = db.Column(db.String(255))
    attachment_size = db.Column(db.Integer)
    attachment_ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'))
    attachment_author_id = db.Column(db.ForeignKey('users.user_id'))

    # Add relationships
