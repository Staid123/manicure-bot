from aiogram import Bot
from fluentogram import TranslatorRunner
from src.postgres.dao import DAO
from datetime import datetime
from src.core.dto import GetAllRecordsDTO, DeleteRecordDTO
from src.telegram import Config


async def delete_records(
    dao: DAO, 
    l10n: TranslatorRunner, 
    bot: Bot,
    config: Config
) -> None:
    for admin_id in config.admin.ids:
        await bot.send_message(
            chat_id=admin_id,
            text=l10n.admin.ready_delete()
        )
    records: GetAllRecordsDTO = await dao.user.get_all_records()
    for rec in records:
        if rec.datetime < datetime.now():
            await dao.admin.delete_record(
                DeleteRecordDTO(
                    datetime=rec.datetime))
            await dao.user.delete_records(
                DeleteRecordDTO(
                    datetime=rec.datetime))
            flag = True
    for admin_id in config.admin.ids:
        await bot.send_message(
            chat_id=admin_id,
            text=l10n.send.reminder.done())