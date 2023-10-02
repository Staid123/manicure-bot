from src.core.dto import GetUserRecordsDTO
from fluentogram import TranslatorRunner
from typing import List, Optional


def get_text2(l10n: TranslatorRunner, data: Optional[List[GetUserRecordsDTO]]) -> str:
    text: Optional[List[GetUserRecordsDTO]] = (f'\n{l10n.delimiter()}\n').join([l10n.user.records(
        name=rec.client_name, 
        date=rec.datetime,
        time=f'{rec.datetime.hour}:{rec.datetime.minute}' if rec.datetime.minute else f'{rec.datetime.hour}:00',
        service=rec.type_of_service,
        phone=rec.phone_number) for rec in sorted(data, key=lambda i: i.datetime)])
    return text