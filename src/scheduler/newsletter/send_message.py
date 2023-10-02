from aiogram import Bot
from fluentogram import TranslatorRunner
from src.postgres.dao import DAO
from datetime import datetime


async def send_message(
    dao: DAO,
    l10n: TranslatorRunner,
    bot: Bot
) -> None:
    records = await dao.user.get_all_records()
    print(records)
    for user in records:
        print(user)
        print((user.datetime - datetime.now()).days)
        if (user.datetime - datetime.now()).days in (0, 1):
            await bot.send_message(
                chat_id=user.client_id, 
                text=l10n.send.reminder(
                    service=user.type_of_service,
                    date=user.datetime
                )
            )