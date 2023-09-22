from src.postgres.dao.user import UserDAO
from src.postgres.dao.admin import AdminDAO
from asyncpg import Connection
from src.core.dao import AbstractDAO


class DAO(AbstractDAO):
    __slots__ = ('user', 'admin')

    def __init__(self, connect: Connection) -> None:
        self.user = UserDAO(connect)
        self.admin = AdminDAO(connect)