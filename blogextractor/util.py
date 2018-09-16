from datetime import datetime, timedelta
import calendar


def to_datetime(time, day, year, offset):
    """

    :param time: string e.g '11:44am', '7:15pm'
    :param day: string e.g 'Sep 07', 'July 17' or None
    :param year: string e.g '2017', '2017' or None
    :param offset: int e.g 1 for Nigeria (gmt + 1)
    :return: datetime object
    """
    current_ts = datetime.utcnow() + timedelta(hours=offset)
    print(time, day, year, offset)
    if time:
        [hr, mn] = time.split(':')
        if mn.endswith('am'):
            hour = int(hr)
        else:
            hour = int(hr) + 12
            if hour == 24:
                hour = 0
        minute = int(mn[:-2])
    else:
        hour = 0
        minute = 0

    if day:
        mth, dy = day.split()
        day = int(dy)
        month = list(calendar.month_abbr).index(mth[:3])
    else:
        day = current_ts.day
        month = current_ts.month

    if year:
        year = int(year)
    else:
        year = current_ts.year

    return datetime(
        year=year,
        month=month,
        day=day,
        hour=hour,
        minute=minute
    )
