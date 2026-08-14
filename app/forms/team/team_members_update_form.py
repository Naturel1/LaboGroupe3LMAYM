from flask_wtf import FlaskForm
from wtforms import SelectMultipleField
from wtforms.validators import Optional

from app.models.user import User


class TeamMembersUpdateForm(FlaskForm):
    """Team members assignment form."""

    members = SelectMultipleField('Members', coerce=int, validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.members.choices = [(user.user_id, user.user_username)
                                for user in User.query.filter_by(active=True).order_by(User.user_id).all()]
