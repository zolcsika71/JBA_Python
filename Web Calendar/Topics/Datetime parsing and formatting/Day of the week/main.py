from datetime import datetime


def get_weekday(datetime_obj):
    return datetime.strftime(datetime_obj, '%A')
