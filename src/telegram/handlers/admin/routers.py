from aiogram import Router
from src.telegram.filters import IsAdmin
from src.telegram.handlers.admin import start, client_anketa, other_commands


router = Router(name='admin/router')
router.message.filter(IsAdmin())
files = (start, client_anketa, other_commands)

for file in files:
    router.include_router(file.router)