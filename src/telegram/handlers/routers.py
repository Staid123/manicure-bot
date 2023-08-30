from logging import getLogger

from aiogram import Router
from asyncpg import Pool
from redis.asyncio.client import Redis

from src.telegram.handlers.admin import routers as admin_router
from src.telegram.handlers.user import routers as user_router


logger = getLogger('manicure.bot')

router = Router()
router.include_routers(
    admin_router,
    user_router
)


@router.shutdown()
async def close(redis: Redis, pool: Pool) -> None:
    await pool.close()
    await redis.close()
    logger.warning('Closed redis connect and postgres pool')