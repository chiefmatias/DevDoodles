from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ListForm(FlaskForm):
    name = StringField("List Name", validators=[DataRequired()])
    add_list = SubmitField("Save Changes")
    edit_list = SubmitField("Save Changes")
    delete_list = SubmitField("Delete List")
