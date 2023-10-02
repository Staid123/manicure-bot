import calendar 
from datetime import datetime


def day_in_months(year: int, month: int) -> list:
    calend = calendar.Calendar().itermonthdays(int(year), month + 1)
    return map(lambda date: '-' if not date else str(date), calend)

