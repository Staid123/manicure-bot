from src.scheduler.newsletter import send_message
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from src.postgres.dao import DAO
from asyncpg import Pool
from fluentogram import TranslatorRunner


async def set_scheduled_jobs(
    scheduler: AsyncIOScheduler, 
    bot: Bot, 
    pool: Pool, 
    l10n: TranslatorRunner
):
    dao: DAO = DAO(pool)
    scheduler.add_job(
        send_message, 
        trigger="interval", 
        seconds=3, 
        args=(dao, l10n, bot)
    )