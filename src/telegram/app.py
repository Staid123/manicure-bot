from aiogram import Bot, Dispatcher
from redis.asyncio import Redis
from aiogram.fsm.storage.redis import DefaultKeyBuilder, RedisStorage
from asyncpg import Pool

from src.telegram import Config
from src.telegram.handlers.routers import router
from src.telegram.middlewares import L10NMiddleware, DAOMiddleware
from src.utils import create_translator_hub


async def start_bot(
    pool: Pool,
    redis: Redis,
    config: Config
) -> None:  
    
    bot: Bot = Bot(
        token=config.tgbot.token,
        parse_mode='html')
    
    if config.tgbot.skip_updates:
        await bot.delete_webhook(drop_pending_updates=True)
    
    storage: RedisStorage = RedisStorage(
        redis,
        key_builder=DefaultKeyBuilder(
            with_destiny=True
        )
    )
    dp: Dispatcher = Dispatcher(
        storage=storage,
        events_isolation=storage.create_isolation()
    )
    dp.include_router(router)
    
    dp.update.middleware(L10NMiddleware(create_translator_hub()))
    dp.update.middleware(DAOMiddleware(pool))

    dp['pool'] = pool
    dp['redis'] = redis

    await dp.start_polling(bot)
