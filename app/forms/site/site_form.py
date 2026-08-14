from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class SiteForm(FlaskForm):
    """Site form.
    """

    name = StringField('Site Name',
                           validators=[DataRequired(), Length(min=1, max=100)])
    address = StringField('Address',
                            validators=[Length(max=255)])
    city = StringField('City',
                           validators=[Length(max=100)])
