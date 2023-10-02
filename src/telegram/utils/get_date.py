from datetime import datetime


def get_year() -> int:
    return datetime.now().year


def get_month() -> int:
    return datetime.now().month


def get_day() -> int:
    return datetime.now().day