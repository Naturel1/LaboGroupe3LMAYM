from app import db
from app.models.base_entity import BaseEntity


class KnowledgeArticle(BaseEntity, db.Model):
    """Represents an article in the knowledge base."""
    __tablename__ = 'knowledge_articles'

    knowledge_article_id = db.mapped_column(
        db.Integer, primary_key=True, autoincrement=True
    )
    knowledge_article_title = db.mapped_column(
        db.String(100), nullable=False
    )
    knowledge_article_content = db.mapped_column(
        db.Text, nullable=False
    )
    knowledge_article_category_id = db.mapped_column(
        db.Integer, db.ForeignKey('categories.category_id'),
        nullable=False
    )
    knowledge_article_author_id = db.mapped_column(
        db.Integer, db.ForeignKey('users.user_id'), nullable=False
    )

    # Add relationships
    category = db.relationship('Category', back_populates='knowledge_articles')
    author = db.relationship('User', back_populates='knowledge_articles')
