import calendar 


def day_in_months(year: int, month: int) -> list:
    calend = calendar.Calendar().itermonthdays(int(year), month + 1)
    return map(lambda date: '-' if date == 0 else str(date), calend)