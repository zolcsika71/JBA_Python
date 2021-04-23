from datetime import datetime

dt = "2020-11-15 00:00:00"

dt1 = datetime(2020, 11, 15, 0, 0)

# print(datetime.strptime(dt, '%Y-%m-%d'))

print(dt1.strftime('%Y-%m-%d'))


