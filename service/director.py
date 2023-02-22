from typing import List

from implemented import DirectorDAO
from dao.model.director import Director


class DirectorService:

    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_all(self) -> List["Director"]:
        return self.dao.get_all()

    def get_by_id(self, did) -> Director:
        return self.dao.get_by_id(did)