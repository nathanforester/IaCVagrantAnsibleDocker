from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError

from application.models import Movies, Review

class MoviesCheck: #customise
    def __init__(self, message):
        self.message = message

    def __call__(self, form, field): #sends query request to sqlalchemy db
        all_movies = Movies.query.all()
        for movies in all_movies:
            if movies.name == field.data:
                raise ValidationError(self.message)

class MoviesForm(FlaskForm): # customise
    name = StringField('Movie Name',
                validators=[
                    DataRequired(),
                    MoviesCheck(message= 'You have already added this movie')
                ]
            )
    submit = SubmitField('Add Movie')

class ReviewForm(FlaskForm): # customise
    rating = SelectField('Rating',
                choices=[
                    ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1'), ('0', '0')])
    rev = StringField('Review',
                validators=[
                    DataRequired()])
    submit = SubmitField('Add Review')
