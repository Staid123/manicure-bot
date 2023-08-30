from src.postgres.dao.user import UserDAO
from src.postgres.dao.admin import AdminDAO
from asyncpg import Connection


class DAO():
    __slots__ = ('user', 'admin')

    def __init__(self, connect: Connection) -> None:
        self.user = UserDAO(connect)
        self.admin = AdminDAO(connect)