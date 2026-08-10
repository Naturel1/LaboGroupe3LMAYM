from app import db
from app.models.base_entity import BaseEntity


class Comment(BaseEntity, db.Model):
    """Represents a comment made on a ticket by a user."""

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    comment_content = db.Column(db.String(1024), nullable=True)
    comment_author_id = db.Column(db.ForeignKey('users.user_id'))
    comment_ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'))

    author = db.relationship("User", back_populates='comments')
    ticket = db.relationship("Ticket", back_populates='comment')
