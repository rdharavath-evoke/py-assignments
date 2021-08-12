# 1 - imports
from actor import Actor
from base import Session
from contact_details import ContactDetails
from movie import Movie
from datetime import date
import logging

logging.basicConfig(level=logging.DEBUG)
# 2 - extract a session
session = Session()


# 3 - extract all movies
movies = session.query(Movie).all()

# 4 - print movies' details
logging.debug('\n### All movies:')
for movie in movies:
    logging.debug(f'{movie.title} was released on {movie.release_date}')



# 5 - get movies after 15-01-01
movies = session.query(Movie) .filter(Movie.release_date > date(2015, 1, 1)).all()

print('### Recent movies:')
for movie in movies:
    print(f'{movie.title} was released after 2015')
