from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import DataRequired, Length


class PriorityForm(FlaskForm):
    """
    Form for priority creation and update.
    """

    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=255)])
    level = IntegerField('Level', validators=[DataRequired()])
    delay_hours = IntegerField('Delay (hours)', validators=[DataRequired()])