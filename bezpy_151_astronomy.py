# ======================================================================================================================
# requires `pip install astronomy-engine`
# https://pypi.org/project/astronomy-engine/
# ======================================================================================================================
# NOT WORKING FOR ME
# ======================================================================================================================
# from datetime import datetime, timezone
# from astronomy import astronomy
#
# def utc_to_local(utc_dt):
#     """returns local time from UTC time"""
#     return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
#
# body = astronomy.Body.Sun
# great_neck = astronomy.Observer(latitude=40.788, longitude=-73.693, height=0)
# london = astronomy.Observer(latitude=51.5072, longitude=-0.1276, height=0)
# direction = astronomy.Direction.Set  # sun is in direction of setting
# start = astronomy.Time(0).Utc()  # datetime(2000, 1, 1, 12, 0)
# now = datetime.now()
# days = (now - start).days + 1    # days since midday  2000/1/1
# start_time = astronomy.Time(days)
# current = astronomy.Time.Now()
# utc = astronomy.SearchAltitude(body=body,
#                                observer=london,
#                                direction=direction,
#                                startTime=current,
#                                limitDays=-0.5,
#                                altitude=6).Utc()
# tzayt_shabbat = utc_to_local(utc)
# ======================================================================================================================


# ======================================================================================================================
# Astral is used to calculate Times for various positions of the sun: dawn, sunrise, solar noon, sunset, dusk,
# solar elevation, solar azimuth and rahukaalam. Moon rise, set, azimuth and zenith. The phase of the moon.
# requires `pip install astral`
# https://astral.readthedocs.io/en/latest/
# https://pypi.org/project/astral/
# ======================================================================================================================
import datetime
from astral import LocationInfo
from astral.moon import moonrise, phase
from astral.location import Location
from astral.sun import sun


city = LocationInfo(name="London", region="England", timezone="Europe/London", latitude=51.5, longitude=-0.116)
london = Location(city)


city = LocationInfo(name="Queens", region="USA", timezone="America/New_York", latitude=40.73, longitude=-73.79)
s = sun(city.observer, date=datetime.datetime(2024, 3, 17, tzinfo=city.tzinfo))

# {'dawn': datetime.datetime(2024, 3, 17, 6, 35, 1, 774126, tzinfo=zoneinfo.ZoneInfo(key='America/New_York')),    # CIVIL DAWN 6-degrees
#  'sunrise': datetime.datetime(2024, 3, 17, 7, 2, 48, 633661, tzinfo=zoneinfo.ZoneInfo(key='America/New_York')),
#  'noon': datetime.datetime(2024, 3, 17, 17, 3, 28, tzinfo=datetime.timezone.utc),
#  'sunset': datetime.datetime(2024, 3, 17, 19, 4, 24, 723963, tzinfo=zoneinfo.ZoneInfo(key='America/New_York')),
#  'dusk': datetime.datetime(2024, 3, 17, 19, 32, 14, 981107, tzinfo=zoneinfo.ZoneInfo(key='America/New_York'))}  # CIVIL DUSK 6-degrees

# GREAT NECK TIMES
city = LocationInfo(name="Great Neck", region="USA", timezone="America/New_York", latitude=40.788, longitude=-73.693)
shabbat_out = sun(observer=city.observer,
                  date=datetime.date(2024, 3, 16),
                  dawn_dusk_depression=8.5,   # defaulted to 6.0, i.e. civil dawn/dusk
                  tzinfo=city.tzinfo).get('dusk')



great_neck_moonrise = moonrise(observer=city.observer,
                               date=datetime.date(2024, 3, 16),
                               tzinfo=city.tzinfo)

# Timezone irrelevant for moon phase
phase(date=datetime.date(2024, 3, 16))    # returns 6.333, where 0 <= phase() <= 27.99

# 0 .. 6.99	    = New moon phase
# 7 .. 13.99	= First quarter phase
# 14 .. 20.99	= Full moon phase
# 21 .. 27.99	= Last quarter phase

