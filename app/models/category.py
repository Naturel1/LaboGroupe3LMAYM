from app import db
from app.models.base_entity import BaseEntity


class Category(BaseEntity, db.Model):
    """Represents a category for tickets or knowledge articles."""

    __tablename__ = 'categories'

    category_id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.mapped_column(db.String(100), nullable=False, unique=True)
    category_description = db.mapped_column(db.String(255), nullable=True)

    # Add relationships
    knowledge_articles = db.relationship('KnowledgeArticle', back_populates='category',
                                         foreign_keys='KnowledgeArticle.knowledge_article_category_id', cascade='all, delete-orphan')
    tickets = db.relationship('Ticket', back_populates='category',
                              foreign_keys='Ticket.ticket_category_id', cascade='all, delete-orphan')