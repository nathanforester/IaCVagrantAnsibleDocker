from application import db
from application.models import movies


class movies(db.Model): # customise
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    review = db.relationship('Review', backref='movies')

class Review(db.Model): # customise
    id = db.Column(db.Integer, primary_key=True)
    rev = db.Column(db.String(255))
    rating = db.Column(db.Integer)
    movies_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=True) 

db.drop_all()
db.create_all()

db.session.commit()

