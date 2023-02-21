from flask import request
from flask_restx import Resource, Namespace

from implemented import movie_service
from dao.model.movie import movie_schema, movies_schema

movie_ns = Namespace('movies')


@movie_ns.route('/')
class MoviesView(Resource):
    def get(self):
        director = request.args.get('director_id')
        genre = request.args.get('genre_id')
        year = request.args.get('year')
        if director:
            all_movies = movie_service.get_by_director(director)
        elif genre:
            all_movies = movie_service.get_by_genre(genre)
        elif year:
            all_movies = movie_service.get_by_year(year)
        else:
            all_movies = movie_service.get_all()
        return movies_schema.dump(all_movies), 200

    def post(self):
        req_json = request.json
        movie_id = movie_service.add_movie(req_json)
        return '', 201, {'location': f'/movies/{movie_id}'}


@movie_ns.route('/<int:mid>')
class MovieView(Resource):
    def get(self, mid):
        movie = movie_service.get_by_id(mid)
        return movie_schema.dump(movie), 200

    def put(self, mid):
        req_json = request.json
        req_json['mid'] = mid

        movie_service.change_movie_data(req_json)
        return '', 204

    def patch(self, mid):
        req_json = request.json
        req_json['mid'] = mid

        movie_service.patch_movie_data(req_json)
        return '', 204

    def delete(self, mid):
        movie_service.delete(mid)
        return '', 204