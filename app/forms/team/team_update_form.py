from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class TeamUpdateForm(FlaskForm):
    """Team update form."""

    name = StringField('Name', validators=[DataRequired(), Length(min=1, max=80)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=256)])
