#=======================================================================================================================
#   IMPORTED MODULES - Note need to install 'xlrd'
#=======================================================================================================================
from datetime import timedelta as td, datetime as dt    # Standard Library
from dateutil.relativedelta import relativedelta as rd  # pip install python-dateutil

import calendar
# this returns month range for 07/2018 as a tuple ... e.g. (6, 31)
# digit 1 => first day of the month falls on 6 = Sun, 0 = Mon, 1 = Tue, 2 = Wed
# digit 2 => July 2018 has 31 days
calendar.monthrange(2018,7) # returns (6, 31)  

calendar.isleap(2019)          # Returns True if leap year
calendar.weekday(2019,9,1)     # Return weekday value of a date
calendar.leapdays(2020, 2024)  # Returns leapdays within range    1/1/2020 <= days < 1/1/2024
calendar._monthlen(1974, 2)    # Returns 28

#=======================================================================================================================
#   datetime strftime codes
#=======================================================================================================================
# The following codes let you work with dates exactly as you need to use for strftime()
# %a	Weekday, short version	Wed
# %A	Weekday, full version	Wednesday
# %w	Weekday as a number 0-6, 0 is Sunday	3
# %d	Day of month range 01-31	e.g. 31
# %b	Month name, short version, e.g.	Dec
# %B	Month name, full version	December
# %m	Month as a number range 01-12	e.g. 12
# %y	Year, short version, without century, e.g. 18
# %Y	Year, full version	2018
# %H	Hour 00-23	17
# %I	Hour 00-12	05
# %p	AM/PM	PM
# %M	Minute 00-59	41
# %S	Second 00-59	08
# %f	Microsecond 000000-999999	548513
# %z	UTC offset	+0100
# %Z	Timezone	CST
# %j	Day number of year 001-366	365
# %U	Week number of year, Sunday as the first day of week, 00-53	52
# %W	Week number of year, Monday as the first day of week, 00-53	52
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018
# %x	Local version of date	12/31/18
# %X	Local version of time	17:41:00
# %%	A % character	%
# %G	ISO 8601 year	2018
# %u	ISO 8601 weekday (1-7)	1
# %V	ISO 8601 weeknumber (01-53)	01



# ========================================================
# LIST OF datetime functions invoked by a datetime object
# ========================================================
# strftime()                # datetime -> string ,function generates a formatted string from a datetime object
# strptime()                # string -> datetime ,function generates a datetime object from a string.
# utcnow()                  # Universal datetime stamp
# now()                     # local datetime stamp
# today()                   # same as above
# isoweekday()              # returns day of the week Monday = 1 ... Sunday = 7
# weekday()                 # returns day of the week Monday = 0 ... Sunday = 6
# isocalendar()             # Return a 3-tuple containing ISO year, week number, and weekday.
# isoformat(sep, timespec)  # datetime -> timestamp string in iso format
# fromisoformat()           # inverse of above function dt.isoformat(x)
# timestamp()               # datetime -> epoch time  (see below)
# fromtimestamp(et)         # epoch time -> datetime
# max                       # returns largest datetime datetime.datetime(9999, 12, 31, 23, 59, 59, 999999)
# min                       # returns smallest datetime object  datetime.datetime(1, 1, 1, 0, 0)  YEAR 0001 AD
# fromordinal(int)          # converts integer to datetime  1 = dt(1,1,1,0,0)
# toordinal()               # converts integer to proleptic Gregorian ordinal  1 = dt(1,1,1,0,0)
# ctime()                   # converts dt -> string  e.g 'Tue Mar 17 18:26:46 2020'   fixed string type
# date()                    # returns only date from full stamp as type datetime.date
# time()                    # returns only time from full stamp as type datetime.time
# timetuple()               # converts datetime -> struct_time  (from time library - see below)
# combine()
# astimezone()
# dst
# fold
# replace()                 # replace one of the values or tzinfo e.g. datetime(1974, 2, 20, 16, 10, 0).replace(hour=3)  replaces 16 with 3
# resolution
# timetz
# tzinfo
# tzname
# utcfromtimestamp(ts)      # epoch time -> utc datetime
# utcoffset
# utctimetuple
#

utc_now = dt.utcnow()    # Universal datetime stamp
now = dt.now()           # Local datetime stamp
print (now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)

# International Organization for Standardization
now.isoweekday()   # returns day of the week Monday = 1 ... Sunday = 7

now.isocalendar()  # Return a 3-tuple containing ISO year, week number, and weekday.
                   # e.g. (2019, 47, 2)
                   # Update for version 3.9  returns namedtuple() e.g. datetime.IsoCalendarDate(year=2021, week=3, weekday=5)

# dt.isoformat(sep, timespec)
now.isoformat('|', 'minutes') # Returns '2019-11-19|10:20'
# sep: is used to separate the year from the time, and defaults to 'T'. dt.isoformat(dt.now()) Returns '2020-01-28T13:52:29.850150'
# timespec: specifies what components of the time to include e.g 'auto', 'hours', 'minutes', 'seconds', 'milliseconds', and 'microseconds'

date_string = now.strftime('%m/%d/%Y') # e.g. '04/02/2018'
new_years1 = dt(2017, 1, 1)
fall_equinox = dt(year=2016, month=9, day=22)
new_years2 = dt.strptime('1/1/2017', '%m/%d/%Y') #from string -> dt

#ny_string = 'January 01, 2017, 12:00:00 AM'
ny_string = new_years2.strftime('%B %d, %Y, %I:%M:%S %p') #from dt-> string

x = '2022-12-31T10:10:10'  # ISO FORMAT DATETIME
dt.fromisoformat(x)  # datetime.datetime(2022, 12, 31, 10, 10, 10)

y ='2022-12-31'  # ISO FORMAT DATE
dt.fromisoformat(y) # datetime.datetime(2022, 12, 31, 0, 0)



#=======================================================================================================================
# use relativedelta for time differences - it is an expansion of timedelta
# better than timedelta which can't calc months.
# however if you don't need month differences then best go with timedelta since it belongs
# to datetime which is in the standard library. dateutil is extension to datetime. 
# It is an external package requires `pip install python-dateutil`
#=======================================================================================================================
d2 = dt(1990, 10, 10, 23, 15, 55, 999999)  #Oct 10 1990  11:15:55 pm  999,999 MicroSeconds
d1 = dt(1989, 8,   7, 19, 10, 49, 999998)  #Aug 07 1989  07:10:49 pm  999,998 MicroSeconds

diff = rd(d2, d1) # measures time difference between d2 & d1
y = diff.years   # The full number of years difference
m = diff.months  # The full number of months difference
d = diff.days
h = diff.hours
mns = diff.minutes
s = diff.seconds
mcs = diff.microseconds
print(f'Difference = {y}YRS, {m}MTS, {d}DYS, {h}HRS, {mns}MNS, {s}SCS, {mcs}MCS')
# Difference = 1YRS, 2MTS, 3DYS, 4HRS, 5MNS, 6SCS, 1MCS


end_date = dt(2015, 11, 3)

# Subtract 12 months - use relativedelta as it can calclulate length of varying months
start_date = end_date - rd(months=12)

# timedelta which can not calculate month differences but should be a bit faster
start_date = end_date - td(weeks=40, days=84, hours=23, minutes=50, seconds=600, microseconds=9999)

# td can take -ve values too
three_hours_ago = dt.now() + td(hours=-3)

d1 = dt(2020, 2, 20, 16, 30, 00)
d2 = dt(2024, 12, 31, 23, 59, 59)
d2 - d1  # returns a timedelta object  i.e. datetime.timedelta(days=1776, seconds=26999)
(d2 - d1).days      # 1776
(d2 - d1).seconds   # 26999
#=======================================================================================================================
from dateutil import parser

x = parser.parse('2024-01-01T00:00:00.000Z')  # datetime.datetime(2024, 1, 1, 0, 0, tzinfo=tzutc())
#=======================================================================================================================

now = dt.now()  # same as dt.today()

def calc_years(dt1,dt2=now):
    """Calculates years difference between dt2 and dt1"""
    return rd(dt2,dt1).years

def calc_months(dt1,dt2=now):
    """Calculates months difference between dt2 and dt1"""
    y = rd(dt2,dt1).years
    m = rd(dt2,dt1).months
    return  12*y + m

# Calculate First of the current month
end_date_dt = dt(now.year, now.month, 1)

# Subtract 12 months for start date
start_date_dt = end_date_dt - rd(months=12)

# Convert to formatted String
start_date = start_date_dt.strftime('%Y-%m-%d')
end_date = end_date_dt.strftime('%Y-%m-%d')

# Can also use f-strings
start_date_fs = f'{start_date_dt:%Y-%m-%d}'
end_date_fs = f'{end_date_dt:%Y-%m-%d}'

# Converts .net times measured in ticks to python datetime
# where ticks = seconds * 10**7
# datetime(1, 1, 1) represents 0001-01-01 00:00:00
def dot_net(ticks):
    secs = ticks/10**7
    return dt(1, 1, 1) + rd(seconds=secs)


# ======================================================================================================================
# TIME ZONES
# ======================================================================================================================
# import datetime
# datetime.datetime.utcnow().timestamp()                      # Returns UTC time as unix_time but .timestamp() adjusts to local time zone
# datetime.datetime.now(datetime.timezone.utc).timestamp()    # Returns UTC time as unix_time and .timestamp() is consistent accross platforms


from datetime import timezone   # this 'timezone' can take a timedelta as input
dt(2009, 4, 22, 11, 59, 2, tzinfo=timezone.utc)             # sets timezone   datetime.datetime(2009, 4, 22, 11, 59, 2, tzinfo=datetime.timezone.utc)
dt(2009, 4, 22, 11, 59, 2, tzinfo=timezone(td(hours=0)))    # same as above datetime.datetime(2009, 4, 22, 11, 59, 2, tzinfo=datetime.timezone.utc)
dt.now(tz=timezone(td(hours=0)))        # Also returns UTC time and is the same as datetime.datetime.now(datetime.timezone.utc)
dt.now().astimezone()                   # Sets local time zone - datetime.datetime(2024, 3, 17, 21, 27, 38, 964480, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=72000), 'Eastern Daylight Time'))
dt.now(tz=timezone(td(hours=-5)))       # defines fixed offset from UTC (not adjusted for DST), note 'tz=' is not required
dt.now().astimezone(tz=timezone(td(hours=-5)))  # same as above
dt.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")  # '2021-11-25 22:57:51 Eastern Standard Time'


# datetime.datetime.utcnow().timestamp()   <--- this will not give the same value on servers around the world
# datetime.datetime.now(datetime.timezone.utc).timestamp()  <---this will give the same value on servers around the world

def utc_to_local(utc_dt):
    """returns local time from UTC time"""
    return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)    # tz=None i.e. local time zone
utc_to_local(dt.utcnow())


# Use community library pytz (none standard to adjust for DST and give actual time)
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones  
from pytz import timezone   # in contrast to datetime.timezone this takes string as input
utc_timezone = timezone('UTC')
amsterdam = timezone('Europe/Amsterdam')
dt.now(amsterdam)    # datetime.datetime(2024, 3, 18, 2, 39, 56, 396014, tzinfo=<DstTzInfo 'Europe/Amsterdam' CET+1:00:00 STD>)
dt.now(amsterdam).tzname()  # CET
new_york = timezone('America/New_York')
dt.now(new_york)  # datetime.datetime(2024, 3, 17, 21, 43, 50, 437033, tzinfo=<DstTzInfo 'America/New_York' EDT-1 day, 20:00:00 DST>)
dt.now(new_york).tzname()  # 'EDT'
dt(2024, 3, 18, 2, 39, 56, tzinfo=new_york)  # datetime.datetime(2024, 3, 18, 2, 39, 56, tzinfo=<DstTzInfo 'America/New_York' LMT-1 day, 19:04:00 STD>)
dt(2024, 3, 18, 2, 39, 56, tzinfo='America/New_York')


# new_york.localize(dt(2023, 3, 12, 2, 15), is_dst=None)   raise NonExistentTimeError(dt)   because clocks went forward 2AM -> 3AM so time didn't exist locally
london = timezone('Europe/London')
# also see new built-in module 'ZoneInfo' as of python 3.9




import holidays  # community library, pip install holidays
holidays.USA(years=2021) # Returns object of holidays
dt(2021,12,25) in holidays.USA()  # Returns True


#=======================================================================================================================
# datetime.date
#=======================================================================================================================
from datetime import date # this has reduced properties from datetime
date.today()   # returns date object with today's date.  Note" now() is not available.
d = date(1974, 2, 20)
d.isoformat()   #'1974-02-20'
d.isocalendar() #(1974, 8, 3)
issubclass(dt, date)  # True   datetime.datetime is subclass of datetime.date
isinstance(dt(1974, 2, 20), date) # True - since datetime.datetime is a subclass of datetime.date
dt(1974, 2, 20, 16, 10, 00).date()  # converts datetime to date object

#=======================================================================================================================
# use timeit to measure time performing a function 'number' times. but easier to use the 'time' module (below)
#=======================================================================================================================
import timeit

timeit.default_timer()   # gives precise time,  same as time.perf_counter()   see perf_counter()
timeit.default_number    # 1000000
timeit.default_repeat    # 5

def costly_func():
   return map(lambda x: x**2, range(100))

x = list(costly_func()) # [0, 1, 4, 9, 16, 25, ... , 9801]

# Measure it since costly_func is a callable without argument
print(timeit.timeit(costly_func, number = 10000))

# Measure it using raw statements
print(timeit.timeit("""map(lambda x: x**2, range(100))""", number = 10000))



#=======================================================================================================================
# time module
#=======================================================================================================================
from time import sleep, time, localtime, asctime, ctime, gmtime, mktime, strptime, strftime, perf_counter

### 3 formats for time

# struct_time = (tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)
# epoch_time = 1569436387.44159 # number of seconds from the Epoch Time  0 secs
# string_time = 'Wed Sep 25 14:38:57 2019'

# Note: t=0 epoch_time = (tm_year=1969, tm_mon=12, tm_mday=31, tm_hour=19, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=365, tm_isdst=0) FOR NEW YORK
#       tm_yday =  year_day = 268 (i.e. julian numbered day of the year 1 - 366
#       tm_isdst = daylight savings time boolean  {-1, 0, 1}  -1 means library determines DST
#       struct_time can be used like a tuple
dt.fromtimestamp(0)   # returns datetime for zero epoch time
# >>> datetime.datetime(1969, 12, 31, 19, 0)

## Commonly used format codes:
#         %Y Four-digit year, such as 2016
#         %y Two-digit year, such as 16
##        %Y  Year with century as a decimal number.
##        %m  Month as a decimal number [01,12].
##        %d  Day of the month as a decimal number [01,31].
##        %H  Hour (24-hour clock) as a decimal number [00,23].
##        %M  Minute as a decimal number [00,59].
##        %S  Second as a decimal number [00,61].
##        %z  Time zone offset from UTC.
##        %a  Locale's abbreviated weekday name.
##        %A  Locale's full weekday name.
##        %b  Locale's abbreviated month name.
##        %B  Locale's full month name.
##        %c  Locale's appropriate date and time representation.
##        %I  Hour (12-hour clock) as a decimal number [01,12].
##        %p  Locale's equivalent of either AM or PM.


et = 1569436387.4415972 # sample epoch_time


time()               # -> current epoch_time  e.g. 1616447333.0677261
localtime()          # -> current struct_time e.g. time.struct_time(tm_year=2021, tm_mon=3, tm_mday=22, tm_hour=17, tm_min=9, tm_sec=7, tm_wday=0, tm_yday=81, tm_isdst=1)
asctime(localtime()) # -> current string_time e.g. 'Mon Mar 22 17:10:17 2021'
localtime().tm_hour  # -> current hour in 24hr time  e.g. 17 for 5pm

st = localtime(et)        # epoch_time  -> struct_time = time.struct_time(tm_year=2019, tm_mon=9, tm_mday=25, tm_hour=14, tm_min=33, tm_sec=7, tm_wday=2, tm_yday=268, tm_isdst=1)
ctime(et)                 # epoch_time  -> string_time = 'Wed Sep 25 14:33:07 2019'
gmtime(et)                # epoch_time  -> struct_time , same as localtime() but returns UST / GMT
asctime(st)               # struct_time -> string_time = 'Wed Sep 25 14:33:07 2019'
mktime(st)                # struct_time -> epoch_time  = 1569436387.0



strptime('1/1/2017', '%m/%d/%Y')                      # string, format -> struct_time = time.struct_time(tm_year=2017, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=1, tm_isdst=-1)
strptime('1/1/2017-13:12:59', '%m/%d/%Y-%H:%M:%S')    # string, format -> struct_time = time.struct_time(tm_year=2017, tm_mon=1, tm_mday=1, tm_hour=13, tm_min=12, tm_sec=59, tm_wday=6, tm_yday=1, tm_isdst=-1)
mktime(strptime('1/1/2017-13:12:59', '%m/%d/%Y-%H:%M:%S'))  # convert string to epoch time

dt(2017,1,1,13,12,59).timestamp()                     # datetime -> epoch-time = 1483294379.0

strftime('%B %d, %Y, %I:%M:%S %p', st) # format[, struct_time]) -> formatted string
strftime('%B %d, %Y, %I:%M:%S %p')     # current time as formatted string


# Data Values for 'time' class 
# altzone = 14400
# daylight = 1
# timezone = 18000  # offset in seconds of the local time zone (without DST)
# tzname = ('Eastern Standard Time', 'Eastern Daylight Time')


# Measure time lapse
start_time = perf_counter()  # more precise than time.time()
sleep(3) # pause for 3 secs. Fractions are allowed
end_time = perf_counter()    # more precise than time.time()
print("Sleep time=", end_time - start_time, 'seconds')
# Sleep time= 3.000300168991089 seconds
days_passed = (end_time - start_time) / (60*60*24)


# ======================================================================================================================
# USE the performance counter  time.perf_counter() for time deltas !!!!!!
# time.perf_counter() always returns the float value of time in seconds of a performance counter,
# i.e. a clock with the highest available resolution to measure a short duration.
# It does include time elapsed during sleep and is system-wide.
# The reference point of the returned value is undefined,
# so that only the difference between the results of consecutive calls is valid. i.e. only time delta is of significance
# ======================================================================================================================
# time.perf_counter()  - real amount of time for a process to take including sleep time, high resolution value. Only time delta is meaningful
# time.process_time()  - time spent by the computer for the current process (system and user CPU time) excluding sleep time. Only time delta is meaningful
# time.time()          - the current time in seconds since the Epoch, adjustable so better not to use for time deltas
# time.clock()         - deprecated in 3.3
# time.monotonic()     - low resolution value, do not use
# time.time_ns()       - for nano seconds
# ======================================================================================================================
