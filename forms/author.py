from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
)
from wtforms.validators import (
    DataRequired,
    Length,
)


class AuthorForm(FlaskForm):
    name = StringField(
        label="name",
        validators=[
            DataRequired(),
            Length(min=1)
        ],
    )
    description = TextAreaField()
