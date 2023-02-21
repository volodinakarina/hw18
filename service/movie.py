from typing import List

from implemented import MovieDAO
from dao.model.movie import Movie


class MovieService:

    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_all(self) -> List["Movie"]:
        return self.dao.get_all()

    def get_by_id(self, mid) -> Movie:
        return self.dao.get_by_id(mid)

    def get_by_director(self, director_id) -> List["Movie"] | Movie:
        return self.dao.get_by_director(director_id)

    def get_by_genre(self, genre_id) -> List["Movie"] | Movie:
        return self.dao.get_by_genre(genre_id)

    def get_by_year(self, year) -> List["Movie"] | Movie:
        return self.dao.get_by_year(year)

    def add_movie(self, data) -> None:
        return self.dao.add_movie(data)

    def change_movie_data(self, data) -> None:
        mid = data.get('mid')
        movie = self.get_by_id(mid)

        movie.title = data.get('title')
        movie.description = data.get('description')
        movie.trailer = data.get('trailer')
        movie.year = data.get('year')
        movie.rating = data.get('rating')
        movie.genre_id = data.get('genre_id')
        movie.director_id = data.get('director_id')

        self.dao.change_movie_data(movie)

    def patch_movie_data(self, data) -> None:
        mid = data.get('mid')
        movie = self.get_by_id(mid)

        if 'title' in data:
            movie.title = data.get('title')
        if 'description' in data:
            movie.description = data.get('description')
        if 'trailer' in data:
            movie.trailer = data.get('trailer')
        if 'year' in data:
            movie.year = data.get('year')
        if 'rating' in data:
            movie.rating = data.get('rating')
        if 'genre_id' in data:
            movie.genre_id = data.get('genre_id')
        if 'director_id' in data:
            movie.director_id = data.get('director_id')

        self.dao.change_movie_data(movie)

    def delete(self, mid) -> None:
        self.dao.delete(mid)

