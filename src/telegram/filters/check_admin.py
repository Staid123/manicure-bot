from aiogram.filters import BaseFilter
from aiogram.types import Message
from src.telegram import config


class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in config.admin.ids:
            return True
        return False