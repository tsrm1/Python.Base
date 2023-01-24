from datetime import date
from datetime import datetime
import pytz


old_date = date(2022, 2, 24)
print("date                                 -> ", date)
print("old_date = date(2022, 2, 24)         -> ", old_date)

print("old_date.day                         -> ", old_date.day)
print("old_date.month                       -> ", old_date.month)
print("old_date.year                        -> ", old_date.year)
print("old_date.weekday()                   -> ", old_date.weekday())
print("old_date.replace(5)                  -> ", old_date.replace(200-2-3))
print("old_date.timetuple()                 -> ", old_date.timetuple())


print()
timestamp = 1528797322      # 0 = 1970-01-01
date_time = date.fromtimestamp(timestamp)
print("date.fromtimestamp(timestamp)        -> ", date_time)

print()
print("date.today()                         -> ", date.today())
print()
print("datetime.now().strftime('%A')          -> ",
      datetime.now().strftime('%A'))
print("datetime.now().strftime('%Y')          -> ",
      datetime.now().strftime('%Y'))
print("datetime.now().strftime('%m')          -> ",
      datetime.now().strftime('%m'))
print("datetime.now().strftime('%b')          -> ",
      datetime.now().strftime('%b'))
print("datetime.now().strftime('%B')          -> ",
      datetime.now().strftime('%B'))
print("datetime.now().strftime('%c')          -> ",
      datetime.now().strftime('%c'))
print("datetime.now().strftime('%d')          -> ",
      datetime.now().strftime('%d'))
print("datetime.now().strftime('%x')          -> ",
      datetime.now().strftime('%x'))
print("datetime.now().strftime('%X')          -> ",
      datetime.now().strftime('%X'))

print("datetime.now().strftime('%m/%d/%Y, %H:%M:%S') -> ",
      datetime.now().strftime('%m/%d/%Y, %H:%M:%S'))
print("datetime.now().strftime('%I%p')        -> ",
      datetime.now().strftime('%I%p'))

print()
# import pytz
# Get the timezone object for New York
tz_NY = pytz.timezone('America/New_York')
# Get the current time in New York
datetime_NY = datetime.now(tz_NY)
# Format the time as a string and print it
print("NY     time:", datetime_NY.strftime("%H:%M:%S"))

# Get the timezone object for London
tz_London = pytz.timezone('Europe/London')
# Get the current time in London
datetime_London = datetime.now(tz_London)
# Format the time as a string and print it
print("London time:", datetime_London.strftime("%H:%M:%S"))


print()
print("old_date.fromisocalendar(.., .., ..) -> ",
      old_date.fromisocalendar(2023, 2, 1))
print("date.today().isocalendar()           -> ",
      old_date.isocalendar())
print("old_date.fromisoformat('2022-02-25') -> ",
      old_date.fromisoformat("2022-02-25"))
print("date.max                             -> ", date.max)
print("date.min                             -> ", date.min)

print()
print("datetime.now()                       -> ", datetime.now())
print()
# CURRENT DATE AND TIME
now = datetime.now()
# CONVERT FROM DATETIME TO TIMESTAMP
ts = datetime.timestamp(now)
print("datetime.timestamp(datetime.now())", datetime.timestamp(datetime.now()))
# print("datetime.timestamp(date.today())", datetime.timestamp(date.today()))

print()
print('considering date is in dd/mm/yyyy format')
dt_string = '12/11/2018 09:15:32'
# considering date is in dd/mm/yyyy format
dt_object1 = datetime.strptime(dt_string, '%d/%m/%Y %H:%M:%S')
print("date.strftime(dt_string, '%d/%m/%Y %H:%M:%S')", dt_object1)
