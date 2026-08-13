from flask_wtf import FlaskForm
from wtforms import EmailField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Regexp

from app import app

# Password rules: lenient in debug, strict in production.
# Same rules in reset form (see user_reset_password_form.py): new password must be as strong as the initial one.
PASSWORD_VALIDATORS = (
    # DEBUG:
    [DataRequired(), Length(min=4, max=128)]
    if app.debug else
    # PRODUCTION:
    [DataRequired(), Length(min=12, max=128),
     Regexp(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)',
            message="Password must contain at least one lowercase letter, "
                    "one uppercase letter and one digit.")]
)


class UserRegisterForm(FlaskForm):
    """Registration form.

    FlaskForm (flask-wtf) adds two things to WTForms:
    - automatic reading of request.form (no need to pass the data)
    - a hidden CSRF field, signed with app.secret_key, rendered by
      form.hidden_tag() in the template. Without it, form.validate_on_submit()
      rejects the POST: this is the protection against forms submitted from
      another site.

    The validators are the only place where we define the rules: the HTML
    (`required`) is for user convenience only, and can be easily bypassed.
    """

    username = StringField('Username',
                           validators=[DataRequired(), Length(min=3, max=80)])
    firstname = StringField('First name',
                            validators=[DataRequired(), Length(min=1, max=64)])
    lastname = StringField('Last name',
                           validators=[DataRequired(), Length(min=1, max=64)])
    email = EmailField('Email',
                       validators=[DataRequired(), Email(), Length(max=120)])
    password = PasswordField('Password',
                             validators=[*PASSWORD_VALIDATORS,
                                         EqualTo('confirm',
                                                 message='Passwords do not match!')])
    confirm = PasswordField('Confirmation', validators=[DataRequired()])
