#!/usr/bin/env python
""" https://darksky.net/dev/account
User: oren.bezalely@gmail.com
Pwd:  badge7383 """

import json
import sys  # print(sys.version_info[:]) prints full version of python
import cgi  # used for retrieving POST/GET
import time
import datetime
import pytz  # time zones
#import cgitb #displays error messages
#cgitb.enable()


EPOCH_DATETIME = datetime.datetime(1970,1,1)
SECONDS_PER_DAY = 24*60*60


def utc_to_local_datetime( utc_datetime ):
    delta = utc_datetime - EPOCH_DATETIME
    utc_epoch = SECONDS_PER_DAY * delta.days + delta.seconds
    time_struct = time.localtime( utc_epoch )
    dt_args = time_struct[:6] + (delta.microseconds,)
    return datetime.datetime( *dt_args )


# fonts from ... https://fonts.google.com/
print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ("<link rel='stylesheet' type='text/css' href='http://fonts.googleapis.com/css?family=Lato'>")
print ("<link rel='stylesheet' href='https://www.w3schools.com/w3css/4/w3.css'>")
print ("<style>body {font-family: 'Lato', serif;font-size: 28px;}</style>")
print ('<title>TSC Weather Report</title>')
print ('</head>')
print ('<body>')
print ("<img src='https://mytscinsurance.com/logo.jpg' style='width:200px;'>")
print ('Live Weather Report')

api_key = '8f4aab25bf22e16fd83edca15dac8029'
url = 'https://api.darksky.net/forecast/8f4aab25bf22e16fd83edca15dac8029/40.7886532,-73.5512059'
#https://api.darksky.net/forecast/[key]/[latitude],[longitude]

if sys.version_info[0] == 3:
	import requests
	r = requests.get(url)
	json_obj = r.json()
else: # FOR VERSION 2
	import urllib2
	json_obj = json.load(urllib2.urlopen(url))


#print (json_obj['currently'])
#for i,j in json_obj['currently'].items():
#	print (str(i) + '=' + str(j))
#print (json_obj)
# print (r.text) prints full api response from url which is json

utc = pytz.timezone('UTC')
now = utc.localize(datetime.datetime.utcnow())
local_time = str(now.astimezone(pytz.timezone('America/New_York')))
#Asia/Jerusalem


print ("<table class='w3-table w3-striped w3-bordered'>")
print ('<tr><td>Python Version</td><td>' + str(sys.version_info[0]) + '.' + str(sys.version_info[1]) + '.' + str(sys.version_info[2]) + '</td></tr>')
print ('<tr><td><b>Coordinates:</b></td>' +  '<td>' + str(round(json_obj['latitude'],1)) + ',' + str(round(json_obj['longitude'],1)) + '</td></tr>')
print ('<tr><td><b>Location:</b></td>' +  '<td>' + str(json_obj['timezone']) + '<br>')
print ('<tr><td><b>Time:</b></td>' +  '<td><b>' + local_time[11:19] + '</b></td></tr>')
# print (int(time.time())) this prints current unix time
print ('<tr><td><b>Current Weather:</b></td>' +  '<td>' + str(json_obj['currently']['summary']) + '</td></tr>')
print ('<tr><td><b>Precipitation:</b></td>' +  '<td>' + str(json_obj['currently']['precipProbability']*100) + '%</td></tr>')
print ('<tr><td><b>Temperature:</b></td>' +  '<td>' + str(json_obj['currently']['temperature']) + 'F</td></tr>')
print ('<tr><td><b>Apparent Temperature:</b></td>' +  '<td>' + str(json_obj['currently']['apparentTemperature']) + 'F</td></tr>')
print ('<tr><td><b>Cloud Cover:</b></td>' +  '<td>' + str(json_obj['currently']['cloudCover']*100) + '%</td></tr>')

ustr = json_obj['minutely']['summary']
astr = ustr.encode("ascii","replace").replace('?','-')
print ('<tr><th><b>Hourly Report:</b></th>' +  '<th>' + astr + '</th></tr>')



plural = ''
for i in range(1,13):
	if ( i > 1):
		plural = 's'
	print ('<tr><td><b>Precip. / Apparent Temp. + ' + str(i) + 'Hr' + plural + '.: </b></td><td>' + str(json_obj['hourly']['data'][i]['summary']) + ' / ' + str(json_obj['hourly']['data'][i]['precipProbability']*100) + '% / ' + str(json_obj['hourly']['data'][i]['temperature']) + 'F</td></tr>')




ustr = json_obj['hourly']['summary']
astr = ustr.encode("ascii","replace").replace('?','-')
print ('<tr><td><b>Daily Report:</b></td>' +  '<td>' + astr + '</td></tr>')



ustr = json_obj['daily']['summary']
astr = ustr.encode("ascii","replace").replace('?','-')
print ('<tr><td><b>Weekly Report:</b></td>' +  '<td>' + astr + '</td></tr>')
print ('</table>')


print ('</body>')
print ('</html>')
