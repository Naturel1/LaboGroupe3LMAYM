from flask_wtf import FlaskForm
from wtforms import EmailField, SelectMultipleField, TextAreaField
from wtforms.validators import DataRequired, Email, Length, Optional

from app.services.role_service import RoleService


class UserUpdateForm(FlaskForm):
    """Profil modification form.

    userroles is a SelectMultipleField: WTForms REFUSES any value that is not in `choices`.
    This prevents the invention of a non-existent role.

    """

    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    description = TextAreaField('Description', validators=[Optional(), Length(max=255)])
    roles = SelectMultipleField('Roles', coerce=int, validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.role_service = RoleService()
        self.roles.choices = [(role.role_id, role.role_name)
                              for role in self.role_service.find_all_entities()]

    def selected_roles(self):
        """Roles entities corresponding to the selected role_ids in the form."""
        return [self.role_service.find_one_entity(role_id)
                for role_id in (self.roles.data or [])]
