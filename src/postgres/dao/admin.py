from asyncpg import Connection


class AdminDAO():
    __slots__ = ('connect', )

    def __init__(self, connect: Connection) -> None:
        self.connect = connect
