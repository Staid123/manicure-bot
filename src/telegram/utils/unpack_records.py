from aiogram.fsm.context import FSMContext
from fluentogram import TranslatorRunner

from datetime import datetime


async def unpack_records(l10n: TranslatorRunner, state: FSMContext) -> tuple[str]:
    data = await state.get_data()
    client_name = data.get('client_name').capitalize()
    phone_number = data.get('phone_number')
    year = int(data.get('year'))
    month_name = data.get('month')
    month = l10n.months().split(', ').index(month_name) + 1
    day = int(data.get('date'))
    time = data.get('time').split(':')
    hour, minute = map(lambda x: int(x), time)
    type_of_service = data.get('type_of_service').lower()
    date = datetime(
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute
    )
    return (client_name, 
            phone_number, 
            date,
            type_of_service)