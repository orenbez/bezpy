#!/usr/bin/python
"""
https://darksky.net/dev/account
User: oren.bezalely@gmail.com
Pwd:  badge7383 or 

"""

import json
import sys  # print(sys.version_info[:]) prints full version of python
import cgi  # used for retrieving POST/GET
#import cgbit #displays error messages
#cgbit.enable()

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>TSC Weather Report</title>')
print ('</head>')
print ('<body>')
print ('<h2>TSC Weather Report</h2>')

locu_api_key = '8f4aab25bf22e16fd83edca15dac8029'
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
print ('Location:' + str(json_obj['timezone']) + '<br>')
# print ('Time:' + str(json_obj['currently']['time']) + '<br>')
print ('Report:' + str(json_obj['minutely']['summary']) + '<br>')
x = json_obj['hourly']['summary']
z = list[x]

print (str(x[7].encode('utf-8')))
print (list(x))


print ('</body>')
print ('</html>')