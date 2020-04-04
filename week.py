from datetime import date

semester_start = date(2020, 1, 13)


def get_current_week():
    d = date.today() - semester_start
    return d.days // 7 + 1
