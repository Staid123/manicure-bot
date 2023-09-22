import asyncio
import logging

from redis.asyncio import Redis
from src.telegram import config
from src.utils import create_postgres_pool
from src.postgres.utils import creating_tables
from src.telegram import start_bot


async def main() -> None:
    pool = await create_postgres_pool(config)
    redis = Redis(
        host=config.redis.host,
        db=config.redis.database,
        port = config.redis.port,
        #password = config.redis.password
    )
    try:
        async with pool.acquire() as connect:
            await creating_tables(connect, force=False)
        await start_bot(pool, redis, config)
    except Exception as e:
        raise e
    finally:
        await pool.close()
        await redis.close()
 
logging.basicConfig(level=logging.DEBUG)
asyncio.run(main())