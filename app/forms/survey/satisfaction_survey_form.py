from flask_wtf import FlaskForm
from wtforms import IntegerField, TextAreaField
from wtforms.validators import DataRequired, NumberRange


class SatisfactionSurveyForm(FlaskForm):
    rating = IntegerField("Rating", validators=[
        DataRequired(),
        NumberRange(min=1, max=5)
    ])
    comment = TextAreaField("Comment", validators=[
    ])
    ticket_id = IntegerField("Ticket", validators=[
        DataRequired()
    ])
    client_id = IntegerField("Client", validators=[
        DataRequired()
    ])
