from asyncpg import create_pool, Pool
from src.telegram.config import Config


async def create_postgres_pool(config: Config) -> Pool:
    """
    Create asyncpg Pool
    
    :param config: config
    :return: asyncpg.Pool
    """


    return await create_pool(
        host=config.psql.host,
        port=config.psql.port,
        password=config.psql.password,
        database=config.psql.database,
        user=config.psql.user
    )