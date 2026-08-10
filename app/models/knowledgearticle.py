from app import db
from app.models.base_entity import BaseEntity


class KnowledgeArticle(BaseEntity, db.Model):
    """Represents an article in the knowledge base."""
    __tablename__ = 'knowledgearticles'

    knowledgearticles_id = db.Column(db.Integer, primary_key=True,
                                     autoincrement=True)
    knowledgearticles_title = db.Column(db.String(100), nullable=False)
    knowledgearticles_content = db.Column(db.Text, nullable=False)

    category_id = db.Column(
        db.Integer, db.ForeignKey('categories.category_id'),
        nullable=False
    )
    author_id = db.Column(db.Integer, db.ForeignKey('users.user_id'),
                          nullable=False)

    category = db.relationship('Category', back_populates='knowledgearticles')
    author = db.relationship('User', back_populates='knowledgearticles')
