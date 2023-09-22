from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.telegram.utils import get_year, day_in_months, working_time_in_day
from fluentogram import TranslatorRunner
from aiogram.fsm.context import FSMContext
from src.postgres.dao import DAO


def answer_yes() -> InlineKeyboardMarkup:
    yes_button: InlineKeyboardButton = InlineKeyboardButton(
        text='✅️',
        callback_data='yes'
    )
    no_button: InlineKeyboardButton = InlineKeyboardButton(
        text='❌',
        callback_data='no'
    )
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(yes_button, no_button)
    return kb_builder.as_markup()


def year() -> InlineKeyboardMarkup:
    year_now, next_year = str(get_year()), str(get_year() + 1)
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=year,
        callback_data=year
    ) for year in [year_now, next_year]])
    return kb_builder.as_markup()


def month(l10n: TranslatorRunner) -> InlineKeyboardMarkup:
    months = l10n.months().split(', ')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=month,
        callback_data=month
    ) for month in months], 
    width=3)
    return kb_builder.as_markup()


async def day(l10n: TranslatorRunner, state: FSMContext) -> InlineKeyboardMarkup:
    data = await state.get_data()
    year_, month_ = data.get('year'), data.get('month')
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

    mnth_year_btn: InlineKeyboardButton = InlineKeyboardButton(
        text=f'{month_} {year_}',
        callback_data='FWTddfa'
    )
    kb_builder.row(mnth_year_btn)

    kb_builder.row(*[InlineKeyboardButton(
        text=d,
        callback_data='FWTddfa'
    ) for d in l10n.week.days().split(', ')])

    lst_months = l10n.months().split(', ')
    number_month = lst_months.index(month_)
    kb_builder.row(*[InlineKeyboardButton(
        text=dd,
        callback_data=dd
    ) for dd in day_in_months(year_, number_month)], width=7)

    return kb_builder.as_markup()


def time(l10n: TranslatorRunner) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    time_ = working_time_in_day(l10n)
    kb_builder.row(*[InlineKeyboardButton(
        text=time,
        callback_data=time
    ) for time in time_], width=4)
    return kb_builder.as_markup()


async def service(
        l10n: TranslatorRunner, 
        state: FSMContext,
        acc_btn: bool = False) -> InlineKeyboardMarkup:
    data = (await state.get_data()).get('type_of_service')
    del_serv = data.split(', ') if data else []
    services = [service for service in l10n.services().split(', ') if service not in del_serv]
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=serv,
        callback_data=serv) for serv in services], width=1)
    if acc_btn:
        accept_button: InlineKeyboardButton = InlineKeyboardButton(
            text='✅️ Подтвердить',
            callback_data='acc_btn')
        kb_builder.row(accept_button)
    return kb_builder.as_markup()


async def delete_record(
        dao: DAO,
        l10n: TranslatorRunner,
        acc_btn: bool = False
) -> InlineKeyboardMarkup:
    data = await dao.admin.get_all_records()
    kb_builder = InlineKeyboardBuilder()
    kb_builder.row(*[InlineKeyboardButton(
        text=l10n.rec(
            name=rec.client_name,
            date=rec.datetime,
            time=f'{rec.datetime.hour}:{rec.datetime.minute}' if rec.datetime.minute else f'{rec.datetime.hour}:00'
        ),
        callback_data=str(rec.datetime)
    ) for rec in sorted(data, key=lambda i: i.datetime)], width=1)
    if acc_btn:
        accept_button: InlineKeyboardButton = InlineKeyboardButton(
            text='✅️ Подтвердить',
            callback_data='acc_btn')
        kb_builder.row(accept_button)
    else:
        cancel_button: InlineKeyboardButton = InlineKeyboardButton(
            text='❌ Отмена',
            callback_data='cncl_btn')
        kb_builder.row(cancel_button)
    return kb_builder.as_markup()