from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField
from wtforms.validators import DataRequired, Length


class KnowledgeArticleForm(FlaskForm):
    title = StringField("Title", validators=[
        DataRequired(),
        Length(min=2, max=100)
    ])
    content = TextAreaField("Content", validators=[
        DataRequired()
    ])
    category_id = IntegerField("Category", validators=[
        DataRequired()
    ])
    author_id = IntegerField("Author", validators=[
        DataRequired()
    ])
