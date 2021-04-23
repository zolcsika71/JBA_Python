from datetime import datetime


def format_time(datetime_obj):
    print(f'24h {datetime_obj.strftime("%H:%M")}')
    print(f'12h {datetime_obj.strftime("%I:%M")}')
