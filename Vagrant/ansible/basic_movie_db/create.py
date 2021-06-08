from application import db
from application.models import movies

db.drop_all()
db.create_all()

new_movie = movies(movie = "Citizen Kane, Thriller, Orson Welles: ")
db.session.add(new_movie)

db.session.commit()
