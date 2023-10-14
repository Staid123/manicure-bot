from aiogram import Bot
from fluentogram import TranslatorRunner
from src.postgres.dao import DAO
from datetime import datetime
from src.telegram import Config

async def send_message(
    dao: DAO,
    l10n: TranslatorRunner,
    bot: Bot,
    config: Config
) -> None:
    for admin_id in config.admin.ids:
        await bot.send_message(
            chat_id=admin_id,
            text=l10n.admin.ready_reminder()
        )
    records = await dao.user.get_all_records()
    for user in records:
        if (user.datetime - datetime.now()).days in (0, 1):
            await bot.send_message(
                chat_id=user.client_id, 
                text=l10n.send.reminder(
                    service=user.type_of_service,
                    date=user.datetime
                )
            )
    for admin_id in config.admin.ids:
        await bot.send_message(
            chat_id=admin_id,
            text=l10n.send.reminder.done())