from datetime import datetime, timedelta

semester_start = datetime(2020, 1, 13)


def get_current_week():
    d = datetime.today() + timedelta(hours=6) - semester_start
    return d.days // 7 + 1
