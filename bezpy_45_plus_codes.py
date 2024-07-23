# see https://towardsdatascience.com/plus-codes-open-location-code-and-scripting-in-google-bigquery-30b7278f3495
# Note that the OpenStreetMap API is completely free, but is slower and less accurate than the Google maps API.

# https://plus.codes/87G8R739+MQ8
# Note: 87 = East Coast,
#       G8 = East Long Island,
#       R7 = Great Neck,
#       39 = Area around Franklin Pl.
#       MQ = 36 Franklin
#       8  = Center of Property  (Additional digit for extra precision

# Format 1 (10-digits)  “87G8R739+MQ”     (ignore '+' as it is only a divider)
# Format 2 (6-digits city,country)        (“R739+MQ Great Neck, New York”)
# Format 3 (11-digits) “87G8R739+MQ8”     (Additional digit of Precision)


format1 = "87G8R739+MQ"
format2 = "R739+MQ Great Neck, New York"
format3 = "87G8R739+MQ8"
url = f"https://plus.codes/{format1}"


# https://console.cloud.google.com/apis/credentials  for API settings / IP restrictions
# TO TEST API, GO TOP: https://maps.googleapis.com/maps/api/geocode/json?key=AIzaSyB0A8fKaC8Iljzv2RgqbhpRH1hqgnoSxCU&address=London
# JAN 2021 Error is 'Enable Billing'  - they require connection with billing account now

from openlocationcode import openlocationcode as olc
import googlemaps
import sys

if __name__ == '__main__':
    geo_code = olc.encode(40.804187,-73.730563,10)  # Returns the 10-digit code = "87G8R739+MQ" from (lon, lat, digits)
    olc.isFull('87G8R739+MQ')   # True
    olc.isValid('87G8R739+MQ')  # True
    olc.isShort('87G8R739+MQ')  # False
    olc.isShort('R739+MQ')      # True
    olc.decode('87G8R739+MQ') # [40.804125, -73.730625, 40.80425, -73.7305, 40.8041875, -73.7305625, 10]


    google_geocoding_api_key = 'AIzaSyB0A8fKaC8Iljzv2RgqbhpRH1hqgnoSxCU'
    gmaps = googlemaps.Client(key = google_geocoding_api_key) # initialize the client

    try:
        geocode_result = gmaps.geocode('kilometro cero madrid')  # geocode the place "kilometro cero madrid"
    except googlemaps.exceptions.ApiError:
        print('API request has been denied, check your API Settings from https://console.cloud.google.com/apis/credentials')
        sys.exit(1)

    geocode_result[0]['geometry']['location'] # let's see the location (lat and long) # >>> {'lat': 40.4166359, 'lng': -3.7038101}
    geocode_result[0]['plus_code'] # let's see the location in plus code  # >>> {'compound_code': 'C78W+MF Madrid, Spain', 'global_code': '8CGRC78W+MF'}
    reverse_geocode_result = gmaps.reverse_geocode((40.4166359,-3.7038101)) # reverse geocode (form lat,long to name of the place)
    reverse_geocode_result[1]['formatted_address'] # location in zip code format # >>> 'Puerta del Sol, 7, 28013 Madrid, Spain'
    reverse_geocode_result[1]['plus_code'] # plus code format # >>> {'compound_code': 'C78W+MF Madrid, Spain', 'global_code': '8CGRC78W+MF'}