from dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_all(self):
        return self.session.query(Movie).all()

    def get_by_id(self, mid):
        return self.session.query(Movie).get_or_404(mid)

    def get_by_director(self, director_id):
        return self.session.query(Movie).filter(Movie.director_id == director_id)

    def get_by_genre(self, genre_id):
        return self.session.query(Movie).filter(Movie.genre_id == genre_id)

    def get_by_year(self, year):
        return self.session.query(Movie).filter(Movie.year == year)

    def add_movie(self, data):
        movie = Movie(**data)

        self.session.add(movie)
        self.session.flush()
        movie_id = movie.id
        self.session.commit()
        return movie_id

    def change_movie_data(self, movie):
        self.session.add(movie)
        self.session.commit()
        return ''

    def delete(self, mid):
        movie = self.get_by_id(mid)

        self.session.delete(movie)
        self.session.commit()
        return ''
