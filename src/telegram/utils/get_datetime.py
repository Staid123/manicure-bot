from datetime import datetime


def get_datetime(data: str) -> datetime:
    date, time = data.split(' ')
    return datetime(
        year=int(date.split('-')[0]),
        month=int(date.split('-')[1]),
        day=int(date.split('-')[2]),
        hour=int(time.split(':')[0]),
        minute=int(time.split(':')[1])
    )