from app import db
from app.models.base_entity import BaseEntity


class Category(BaseEntity, db.Model):
    """Represents a category for tickets or knowledge articles."""

    __tablename__ = 'categories'

    category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    category_name = db.Column(db.String(100), nullable=False, unique=True)
    category_description = db.Column(db.String(255), nullable=True)
