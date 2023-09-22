from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter, or_f
from src.telegram.states import FSMadmin
from aiogram.types import Message, CallbackQuery
from fluentogram import TranslatorRunner
from src.telegram.utils import check_phone, unpack_records
from src.telegram.keyboards import year, month, day, time, service
from src.postgres.dao import DAO
from src.core.dto import InsertrecordDTO


router = Router(name='admin/client/anketa/router')


@router.callback_query(
    StateFilter(FSMadmin.fill_yes_no_in_start),
    F.data=='yes'
)
async def accept_button(
    callback: CallbackQuery,
    l10n: TranslatorRunner,
    state: FSMContext
) -> None:
    await callback.message.delete_reply_markup()
    await callback.message.edit_text(text=l10n.admin.yes())
    await state.set_state(FSMadmin.fill_enter_client_name)


@router.message(
    StateFilter(FSMadmin.fill_enter_client_name),
    F.text
)
async def enter_name(
    message: Message,
    l10n: TranslatorRunner,
    state: FSMContext
) -> None:
    await state.update_data(client_name=message.text)
    await message.answer(text=l10n.admin.phone.number())
    await state.set_state(FSMadmin.fill_enter_client_phone_number)


@router.message(
    StateFilter(FSMadmin.fill_enter_client_phone_number)
)
async def enter_phone(
    message: Message,
    l10n: TranslatorRunner,
    state: FSMContext
) -> None:
    if await check_phone(message, l10n):
        await state.update_data(phone_number=message.text)
        await message.answer(
            text=l10n.admin.year(),
            reply_markup=year()
        )
        await state.set_state(FSMadmin.fill_enter_year)


@router.callback_query(
    StateFilter(FSMadmin.fill_enter_year),
    F.data
)
async def enter_year(
    callback: CallbackQuery,
    l10n: TranslatorRunner,
    state: FSMContext
) -> None:
    await state.update_data(year=callback.data)
    await callback.message.edit_text(
        text=l10n.admin.month(),
        reply_markup=month(l10n)
    )
    await state.set_state(FSMadmin.fill_enter_month)


@router.callback_query(
    StateFilter(FSMadmin.fill_enter_month),
    F.data
)
async def enter_month(
    callback: CallbackQuery,
    l10n: TranslatorRunner,
    state: FSMContext
) -> None:
    await state.update_data(month=callback.data)
    await callback.message.edit_text(
        text=l10n.admin.day(),
        reply_markup=await day(l10n, state)
    )
    await state.set_state(FSMadmin.fill_enter_date)


@router.callback_query(
    StateFilter(FSMadmin.fill_enter_date),
    or_f(F.data == 'FWTddfa', F.data == '-')
)
async def enter_not_month(callback: CallbackQuery) -> None:
    await callback.answer()


@router.callback_query(
    StateFilter(FSMadmin.fill_enter_date),
    F.data.isdigit()
)
async def enter_day(
    callback: CallbackQuery,
    state: FSMContext,
    l10n: TranslatorRunner,
) -> None:
    data = await state.get_data()
    month = data.get('month')
    month_ = l10n.months().split(', ').index(month) + 1
    await state.update_data(date=callback.data)
    await callback.message.edit_text(
        text=l10n.admin.time(),
        reply_markup=time(l10n)
    )
    await state.set_state(FSMadmin.fill_enter_time)


@router.callback_query(
    StateFilter(FSMadmin.fill_enter_time),
    F.data
)
async def enter_time(
    callback: CallbackQuery,
    state: FSMContext,
    l10n: TranslatorRunner
) -> None:
    await state.update_data(time=callback.data)
    await callback.message.edit_text(
        text=l10n.admin.service(),
        reply_markup=await service(l10n, state)
    )
    await state.set_state(FSMadmin.fill_enter_type_of_service)

    
@router.callback_query(
    StateFilter(FSMadmin.fill_enter_type_of_service),
    ~(F.data=='acc_btn')
)
async def enter_type_of_service(
    callback: CallbackQuery,
    state: FSMContext,
    l10n: TranslatorRunner,
) -> None:
    services = (await state.get_data()).get('type_of_service')
    if services:
        await state.update_data(type_of_service=services + ', ' + callback.data)
    else:
        await state.update_data(type_of_service=callback.data)
    await callback.message.edit_text(
        text=l10n.admin.service.more(),
        reply_markup=await service(
            l10n, 
            state, 
            acc_btn=True)
    )


@router.callback_query(
    StateFilter(FSMadmin.fill_enter_type_of_service),
    F.data=='acc_btn'
)
async def accept_btn(
    callback: CallbackQuery,
    state: FSMContext,
    l10n: TranslatorRunner,
    dao: DAO
) -> None:
    client_name, phone_number, date, type_of_service = await unpack_records(l10n, state)
    await dao.admin.insert_record(
        InsertrecordDTO(
            client_name=client_name,
            phone_number=phone_number,
            datetime=date,
            type_of_service=type_of_service
        )
    )
    await callback.message.delete_reply_markup()
    await callback.message.edit_text(text=l10n.admin.send.anketa(
        client_name=client_name, 
        date=date,
        type_of_service=type_of_service
        )
    )
    await callback.message.answer(text=l10n.admin.end())
    await state.clear()