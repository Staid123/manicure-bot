from fluentogram import TranslatorRunner


def working_time_in_day(l10n: TranslatorRunner) -> list:
    start_time = l10n.start.working.time()
    lst: list[str] = [start_time]
    while start_time != '18:00':
        if str(int(start_time[-2:]) + 15) != '60':
            hour = start_time.split(':')[0]
            minutes = str(int(start_time[-2:]) + 15)
        else:
            hour = str(int(start_time.split(':')[0]) + 1)
            minutes = '00'
        start_time = hour + ':' + minutes
        lst.append(start_time)
    return lst