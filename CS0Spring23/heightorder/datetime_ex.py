import datetime as dt
import time

t = time.localtime()
print(t.tm_hour)
print(t.tm_isdst)

current_time = time.strftime("%H:%M:%S", t)
print(current_time)

datetime_str = "3/12/2023 12:12"

datetime_object = dt.datetime.strptime(datetime_str, "%m/%d/%Y %H:%M")

print(datetime_object.timetuple())