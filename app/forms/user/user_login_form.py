from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField
from wtforms.validators import DataRequired


class UserLoginForm(FlaskForm):
    """Login form.

    Whitout length or format validators: we do not give any indication of what exists in the database. The error message
    is always the same ("incorrect username or password"), otherwise we allow enumeration of existing accounts.
    """

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
