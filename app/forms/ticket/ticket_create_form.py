from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional

from app.services.category_service import CategoryService
from app.services.priority_service import PriorityService
from app.services.equipment_service import EquipmentService

class TicketCreateForm(FlaskForm):
    """
    Form for ticket creation.
    """

    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=255)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(min=2, max=255)])
    category_id = SelectField('Category', coerce=int, validators=[DataRequired()])
    priority_id = SelectField('Priority', coerce=int, validators=[DataRequired()])
    equipment_id = SelectField('Equipment', coerce=int, validators=[Optional()])

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.category_service = CategoryService()
        self.category_id.choices = [(category.category_id, category.category_name)
                                    for category in self.category_service.find_all_entities()]
        self.priority_service = PriorityService()
        self.priority_id.choices = [(priority.priority_id, priority.priority_name)
                                    for priority in self.priority_service.find_all_entities()]
        self.equipment_service = EquipmentService()
        self.equipment_id.choices = [(equipment.equipment_id, equipment.equipment_name)
                                      for equipment in self.equipment_service.find_all_entities()]