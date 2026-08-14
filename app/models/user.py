from app import db
from app.models.base_entity import BaseEntity


class User(BaseEntity, db.Model):
    """Represents a user (client, technician, or administrator)."""
    __tablename__ = 'users'

    user_id = db.mapped_column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.mapped_column(db.String(80), unique=True,
                              nullable=False, index=True)
    user_firstname = db.mapped_column(db.String(64), nullable=False)
    user_lastname = db.mapped_column(db.String(64), nullable=False)
    user_email = db.mapped_column(db.String(128), unique=True, nullable=False,
                           index=True)
    user_password = db.mapped_column(db.String(256), nullable=False)  # hash argon2
    user_team_id = db.mapped_column(db.Integer, db.ForeignKey('teams.team_id'), nullable=True)
    user_site_id = db.mapped_column(db.Integer, db.ForeignKey('sites.site_id'), nullable=True)

    # Add relationships
    team = db.relationship('Team', back_populates='members')
    site = db.relationship('Site', back_populates='users')
    roles = db.relationship('UserRole', back_populates='user',
                            foreign_keys='UserRole.user_role_user_id', cascade='all, delete-orphan')
    tickets_created = db.relationship('Ticket', back_populates='author',
                                      foreign_keys='Ticket.ticket_author_id', cascade='all, delete-orphan')
    tickets_assigned = db.relationship(
        'Ticket', back_populates='technician',
        foreign_keys='Ticket.ticket_technician_id', cascade='all, delete-orphan')
    comments = db.relationship('Comment', back_populates='author',
                               foreign_keys='Comment.comment_author_id', cascade='all, delete-orphan')
    ticket_status_histories = db.relationship(
        'TicketStatusHistory', back_populates='user',
        foreign_keys='TicketStatusHistory.ticket_status_history_user_id',
        cascade='all, delete-orphan'
    )
    attachments = db.relationship('Attachment', back_populates='author',
                                  foreign_keys='Attachment.attachment_author_id', cascade='all, delete-orphan')
    equipments = db.relationship('Equipment', back_populates='user',
                                 foreign_keys='Equipment.equipment_user_id', cascade='all, delete-orphan')
    knowledge_articles = db.relationship('KnowledgeArticle', back_populates='author',
                                         foreign_keys='KnowledgeArticle.knowledge_article_author_id', cascade='all, delete-orphan')
    satisfaction_surveys = db.relationship('SatisfactionSurvey', back_populates='client',
                              foreign_keys='SatisfactionSurvey.satisfaction_survey_client_id', cascade='all, delete-orphan')
    interventions = db.relationship('Intervention', back_populates='technician',
                                    foreign_keys='Intervention.intervention_technician_id', cascade='all, delete-orphan')