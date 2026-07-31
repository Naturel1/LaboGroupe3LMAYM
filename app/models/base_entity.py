from sqlalchemy.sql import func

from app import db


class BaseEntity:
    """
    to do
    """

    created_at = db.Column(db.DateTime(timezone=True), server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now())
    deleted_at = db.Column(db.DateTime(timezone=True))
    active = db.Column(db.Boolean, nullable=False, default=True,
                       server_default=db.true())

    def soft_delete(self):
        """Deactivate the entity without dropping it"""
        self.active = False
        self.deleted_at = func.now()
