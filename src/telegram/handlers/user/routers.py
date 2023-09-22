from aiogram import Router

from src.telegram.handlers.user import sign_up

router = Router(name='user/router')

files = (sign_up, )

for file in files:
    router.include_router(file.router)