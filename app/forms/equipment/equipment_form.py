from flask_wtf import FlaskForm
from wtforms import StringField, DateField, IntegerField
from wtforms.validators import DataRequired, Length

class EquipmentForm(FlaskForm):
    name = StringField("Equipment name", validators=[
        DataRequired(),
        Length(min=2, max=100)
    ])
    equipment_type = StringField("Type", validators=[
        DataRequired(),
        Length(min=2, max=80)
    ])
    serial = StringField("Serial Number", validators=[
        DataRequired(),
        Length(min=2, max=100)
    ])
    purchase_date = DateField("Purchase Date", validators=[
        DataRequired()
    ])
    site_id = IntegerField("Site", validators=[
        DataRequired()
    ])
    user_id = IntegerField("Assigned User", validators=[])
