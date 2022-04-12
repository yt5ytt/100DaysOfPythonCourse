from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# *** These are classes for forms definition  *** #


class UpdateForm(FlaskForm):
    # rating = FloatField("Your rating out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review")
    button = SubmitField("Update")


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    button = SubmitField("Add Movie")
