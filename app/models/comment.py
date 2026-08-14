from app import db
from app.models.base_entity import BaseEntity


class Comment(BaseEntity, db.Model):
    """Represents a comment made on a ticket by a user."""

    __tablename__ = 'comments'

    comment_id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    comment_content = db.mapped_column(db.Text, nullable=True)
    comment_author_id = db.mapped_column(db.ForeignKey('users.user_id'))
    comment_ticket_id = db.mapped_column(db.ForeignKey('tickets.ticket_id'))

    # Add relationships
    author = db.relationship("User", back_populates='comments')
    ticket = db.relationship("Ticket", back_populates='comments')
