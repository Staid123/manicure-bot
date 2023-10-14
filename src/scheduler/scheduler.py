from src.scheduler.newsletter import send_message, delete_records
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from src.postgres.dao import DAO
from asyncpg import Pool
from fluentogram import TranslatorRunner
from src.telegram import Config

async def set_scheduled_jobs(
    scheduler: AsyncIOScheduler, 
    bot: Bot, 
    pool: Pool, 
    l10n: TranslatorRunner,
    config: Config
):
    dao: DAO = DAO(pool)
    scheduler.add_job(
        send_message, 
        trigger="interval", 
        days=1, 
        args=(dao, l10n, bot, config)
    )
    scheduler.add_job(
        delete_records,
        trigger="interval",
        days=1.5,
        args=(dao, l10n, bot, config)
    )