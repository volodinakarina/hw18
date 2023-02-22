from typing import List

from implemented import GenreDAO
from dao.model.genre import Genre


class GenreService:

    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_all(self) -> List["Genre"]:
        return self.dao.get_all()

    def get_by_id(self, gid) -> Genre:
        return self.dao.get_by_id(gid)
