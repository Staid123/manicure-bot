from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from src.telegram.states import FSMadmin
from aiogram.fsm.state import default_state
from fluentogram import TranslatorRunner
from src.postgres.dao import DAO
from src.telegram.utils import get_text
from src.telegram.keyboards.inline import delete_record
from src.core.dto import DeleteRecordDTO
from src.telegram.utils import get_datetime


router = Router(name='admin/other_commands/router')


@router.message(
    Command(commands=['help']), 
    StateFilter(default_state)
)
async def help_command(
    message: Message, 
    l10n: TranslatorRunner
    ) -> None:
    await message.answer(text=l10n.help.command())


@router.message(
    Command(commands=['check_records']),
    StateFilter(default_state)
)
async def check_records_command(
    message: Message,
    dao: DAO,
    l10n: TranslatorRunner
) -> None:
    data = await dao.admin.get_all_records()
    text: str = get_text(l10n, data)
    await message.answer(text=text)
    await message.answer(text=l10n.admin.end())


@router.message(
    Command(commands=['delete_record']),
    StateFilter(default_state)
)
async def delete_records_command(
    message: Message,
    state: FSMContext,
    l10n: TranslatorRunner,
    dao: DAO
) -> None:
    await message.answer(
        text=l10n.admin.delete.record(), 
        reply_markup=await delete_record(dao, l10n))
    await state.set_state(FSMadmin.fill_edit_working_time)


@router.callback_query(
    F.data=='cncl_btn',
    StateFilter(FSMadmin.fill_edit_working_time)
)
async def cancel_button(
    callback: CallbackQuery,
    state: FSMContext,
    l10n: TranslatorRunner
) -> None:
    await callback.message.delete_reply_markup()
    await callback.message.edit_text(
        text=l10n.help.command()
    )
    await state.clear()


@router.callback_query(
    F.data.contains(':'),
    F.data.contains('-'),
    StateFilter(FSMadmin.fill_edit_working_time)
)
async def record_deleted(
    callback: CallbackQuery,
    l10n: TranslatorRunner,
    dao: DAO,
) -> None:
    datetime = get_datetime(data=callback.data)
    await dao.admin.delete_record(
        DeleteRecordDTO(
            datetime=datetime
        )
    )
    await callback.message.edit_reply_markup(
        reply_markup=await delete_record(dao, l10n, acc_btn=True)
    )


@router.callback_query(
    F.data=='acc_btn',
    StateFilter(FSMadmin.fill_edit_working_time)
)
async def accept_button(
    callback: CallbackQuery,
    state: FSMContext,
    l10n: TranslatorRunner
) -> None:
    await callback.message.delete_reply_markup()
    await callback.message.edit_text(text=l10n.help.command())
    await state.clear()