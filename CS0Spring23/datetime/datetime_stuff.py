import datetime

# get current time
curr_time = datetime.datetime.now()
print(curr_time)

# get current date
current_date = datetime.date.today()
print(current_date)

# construct a date using the date class
d = datetime.date(2022, 12, 25)
print(d)

# today() to get current date
todays_date = datetime.date.today()
print("Today's date =", todays_date)

now_stamp = curr_time.timestamp()
print(now_stamp)

timestamp = datetime.date.fromtimestamp(now_stamp)
print("Date =", timestamp)

# date object of today's date
today = datetime.date.today() 
print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


print()
# time stuff
from datetime import time
# time(hour = 0, minute = 0, second = 0)
a = time()
print(a)

# time(hour, minute and second)
b = time(11, 34, 56)
print(b)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print(c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print(d)


# timedelta stuff
print()
from datetime import datetime, date

# using date()
t1 = date(year = 2018, month = 7, day = 12)
t2 = date(year = 2017, month = 12, day = 23)

t3 = t1 - t2

print("t3 =", t3)

# using datetime()
t4 = datetime(year = 2018, month = 7, day = 12, hour = 7, minute = 9, second = 33)
t5 = datetime(year = 2019, month = 6, day = 10, hour = 5, minute = 55, second = 13)
t6 = t4 - t5
print("t6 =", t6)

print("Type of t4 =", type(t4))
print("Type of t3 =", type(t3)) 
print("Type of t6 =", type(t6))


from datetime import timedelta
print()
t = timedelta(days = 5, hours = 1, seconds = 33, microseconds = 233423)
print("Total seconds =", t6.total_seconds())