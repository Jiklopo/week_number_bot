from datetime import datetime, timedelta
import os

semester_start = datetime.strptime(os.getenv('SEMESTER_START'), '%d/%m/%y %H:%M:%S')


def get_current_week():
    d = datetime.today() + timedelta(hours=6) - semester_start
    return d.days // 7 + 1
