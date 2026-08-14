from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateTimeField
from wtforms.validators import DataRequired, NumberRange


class InterventionForm(FlaskForm):

    intervention_date = DateTimeField('Date', validators=[DataRequired()])
    intervention_duration = IntegerField('Duration (minutes)', validators=[DataRequired(), NumberRange(min=1, max=860)])
    intervention_report = StringField('Report', validators=[DataRequired()])
    intervention_ticket_id = IntegerField('Ticket', validators=[DataRequired()])
    intervention_technician_id = IntegerField('Technician', validators=[DataRequired()])
    intervention_type_id =  IntegerField('Intervention type', validators=[DataRequired()])