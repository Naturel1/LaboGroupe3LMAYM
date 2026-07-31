from app import db
from app.models.base_entity import BaseEntity

class User(BaseEntity, db.Model):
    """
    to do
    """
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    user_firstname = db.Column(db.String(64), nullable=False)
    user_lastname = db.Column(db.String(64), nullable=False)
    user_email = db.Column(db.String(128), unique=True, nullable=False, index=True)
    user_password = db.Column(db.String(256), nullable=False)
