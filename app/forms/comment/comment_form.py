from flask_wtf import FlaskForm
from wtforms import TextAreaField
from wtforms.validators import Length

class CommentForm(FlaskForm):
    """
    
    """

    content = TextAreaField('Content', validators=[Length(max=2000)])
