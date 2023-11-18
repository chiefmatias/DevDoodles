from datetime import date
from flask_wtf import FlaskForm
from wtforms import DateField, SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Optional


class TaskForm(FlaskForm):
    title = StringField("Task", validators=[DataRequired()])
    due = DateField("Due Date", validators=[DataRequired()], default=date.today)
    priority = SelectField(
        "Priority", choices=["Low", "Medium", "High"], validators=[DataRequired()]
    )
    description = StringField(
        "Description",
        validators=[Optional()],
        render_kw={"class": "form-control custom-textarea"},
    )
    add_task = SubmitField("Confirm")
