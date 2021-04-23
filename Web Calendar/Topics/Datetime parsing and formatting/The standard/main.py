from datetime import datetime


def convert_to_standard(datetime_obj):
    return datetime.strftime(datetime_obj, '%Y-%m-%d')
