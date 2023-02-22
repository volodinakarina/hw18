from flask_restx import Resource, Namespace

from implemented import genre_service
from dao.model.genre import genre_schema, genres_schema

genre_ns = Namespace('genres')


@genre_ns.route('/')
class GenresView(Resource):
    def get(self):
        all_genres = genre_service.get_all()
        return genres_schema.dump(all_genres), 200


@genre_ns.route('/<int:gid>')
class GenreView(Resource):
    def get(self, gid):
        genre = genre_service.get_by_id(gid)
        return genre_schema.dump(genre), 200