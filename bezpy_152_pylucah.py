# pyluach
# https://github.com/simlist/pyluach
# https://pyluach.readthedocs.io/
# Can be used to list parshiot but not festivals

from datetime import date, timedelta
from astral import LocationInfo
from astral.sun import sun
from pyluach import dates, parshios, hebrewcal

h_date = dates.HebrewDate(year=5784, month=13, day=12)  # 12th of Adar II
h_date.hebrew_date_string(thousands=False)   # י״ב אדר ב׳ תשפ״ד'

g_date = h_date.to_greg()      # GregorianDate(2024, 3, 22)
g_date = h_date.to_pydate()    # datetime.date(2024, 3, 22)

g_date = dates.GregorianDate(2024, 3, 22)
g_date.strftime('%m/%d/%Y')   # '03/22/2024'

# searches to the following saturday after or equal to your date
parshios.getparsha(date=h_date, israel=False)  # returns [23]  (i.e. 23rd parsha), could be list of 2 numbers for a double parsha
parshios.getparsha(date=g_date, israel=False)  # returns [23]  (i.e. 23rd parsha), could be list of 2 numbers for a double parsha

parshios.getparsha_string(h_date, hebrew=True)   # 'ויקרא'
parshios.getparsha_string(g_date, hebrew=True)   # 'ויקרא'

parsha_dates = parshios.parshatable(year=5784, israel=False)  # returns full dict of parshiot
# OrderedDict([(HebrewDate(5784, 7, 1), None),
#              (HebrewDate(5784, 7, 8), [52]),
#              (HebrewDate(5784, 7, 15), None),
#              (HebrewDate(5784, 7, 22), None),
#              (HebrewDate(5784, 7, 29), [0]),
#              (HebrewDate(5784, 8, 6), [1]), ...
#


def shabbat_times(dt: date) -> str:

    city = LocationInfo(name="Great Neck",
                        region="USA",
                        timezone="America/New_York",
                        latitude=40.788,
                        longitude=-73.693)

    shabbat_in = sun(observer=city.observer,
                      date=dt - timedelta(days=1),
                      tzinfo=city.tzinfo).get('sunset')

    shabbat_out = sun(observer=city.observer,
                      date=dt,
                      dawn_dusk_depression=8.5,  # defaulted to 6.0, i.e. civil dawn/dusk
                      tzinfo=city.tzinfo).get('dusk')

    return shabbat_in, shabbat_out

hebrewcal.utils.FESTIVALS          # ['Rosh Hashana', 'Yom Kippur', 'Succos', ... , "Tu B'av"]
hebrewcal.utils.MONTH_NAMES        # ['Nissan', 'Iyar', ..., 'Adar 2']
hebrewcal.to_hebrew_numeral(5784)  # 'תשפ״ד'

if __name__ == '__main__':
    year = 5784
    print(f'Shabbat Out Times for Great Neck: {year}')
    for h_date in parshios.parshatable(year=year, israel=False).keys():
        hewbrew_date_str = h_date.hebrew_date_string(thousands=False)
        g_date = h_date.to_pydate()
        times = shabbat_times(g_date)
        candles = (times[0] - timedelta(minutes=18)).strftime('%m/%d/%Y %H:%M')
        shabbat_in = times[0].strftime('%m/%d/%Y %H:%M')
        shabbat_out = times[1].strftime('%m/%d/%Y %H:%M')
        parsha_e = parshios.getparsha_string(h_date, hebrew=False)
        parsha_h = parshios.getparsha_string(h_date, hebrew=True)
        print(f'Candles: {candles}, Sunset: {shabbat_in}, Shabat Out: {shabbat_out} | {parsha_e} ({parsha_h} - {hewbrew_date_str})')


