from typing import Callable, Any, Awaitable, Dict

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from asyncpg import Pool
from src.postgres.dao import DAO


class DAOMiddleware(BaseMiddleware):
    def __init__(self, pool: Pool):
        self._pool = pool

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, any]], Awaitable[str, Any]],
        event: TelegramObject,
        data: Dict[str, Any]
    ) -> Any:
        async with self._pool.acquire() as connect:
            data['dao'] = DAO(connect)
            await handler(event, data)