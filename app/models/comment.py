from app import db
from app.models.base_entity import BaseEntity

class Comment(BaseEntity, db.Model):
    """
    to do
    """

    __tablename__ = 'comments'

    comment_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    commment_content = db.Column(db.String(1024), nullable=True)
    comment_author_id = db.Column(db.ForeignKey('users.user_id'))
    comment_ticket_id = db.Column(db.ForeignKey('tickets.ticket_id'))

    # Add relations

