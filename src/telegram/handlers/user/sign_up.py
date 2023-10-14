from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command, or_f
from fluentogram import TranslatorRunner
from src.telegram.keyboards import requert_number
from src.core.dto import GetUserRecordsDTO, InsertrecordDTO
from src.postgres.dao import DAO
from src.telegram.utils import get_text2

router = Router(name='user/sign_up/router')

@router.message(
    or_f(CommandStart(), 
    Command(commands='see_my_records')))
async def start_command(
    message: Message,
    l10n: TranslatorRunner
) -> None:
    await message.answer(
        l10n.user.start(name=message.from_user.first_name),
        reply_markup=requert_number(l10n))


@router.message(Command(commands='help'))
async def command_help(
    message: Message,
    l10n: TranslatorRunner
) -> None:
    await message.answer(l10n.user.commands())


@router.message(F.contact)
async def enter_phone_number(
    message: Message,
    dao: DAO,
    l10n: TranslatorRunner
) -> None:
    phone_number = message.contact.phone_number
    if phone_number[0] == '+':
        phone_number = phone_number[1:]
    data = await dao.user.get_rec_by_phone(
        GetUserRecordsDTO(
            phone_number=phone_number))
    if data:
        text: str = get_text2(l10n, data)
        await message.answer(text=text)
    else:
        await message.answer(text=l10n.no.records())
    for rec in data:
        count_records = await dao.user.check_record(rec.datetime)
        if not count_records:
            await dao.user.insert_record(
                InsertrecordDTO(
                    client_name=rec.client_name,
                    phone_number=rec.phone_number,
                    type_of_service=rec.type_of_service,
                    datetime=rec.datetime,
                    client_id=message.from_user.id
                )
            )