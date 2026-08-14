from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

from app.services.category_service import CategoryService
from app.services.priority_service import PriorityService
from app.services.equipment_service import EquipmentService

class TicketUpdateForm(FlaskForm):
    """
    Form for ticket update.
    """

    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=255)])
    equipment_id = SelectField('Equipment', coerce=int, validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.equipment_service = EquipmentService()
        self.equipment_id.choices = [(equipment.equipment_id, equipment.equipment_name)
                                      for equipment in self.equipment_service.find_all_entities()]