# ======================================================================================================================
# "requests" is a module which handles api calls
# ======================================================================================================================
# REQUIRES 'pip install requests'  2/25/22= Version 2.27.1
# Note 'urllib' is from the standard library  see bezpy_31_download
# 'requests' is a better alternative library to 'from urllib.request import urlopen'
# ======================================================================================================================
# Docs: https://docs.python-requests.org/en/master/user/quickstart
# ======================================================================================================================
# TRY THIS: https://medium.com/swlh/using-and-calling-an-api-with-python-494a18cb1f44?source=bookmarks---------1----------------------------
# READ THIS: https://www.tutorialspoint.com/http/http_quick_guide.htm
# ======================================================================================================================
# API: Application Programming Interface.
# API Architecture and protocols: JSON-RPC, XML-RPC, SOAP (Simple Object Access Protocol), REST, GraphQL
# ======================================================================================================================
# REST (Representational State Transfer) is an architectural style for building scalable web services
# RESTful APIs use HTTP verbs (like GET, PUT and DELETE) to make requests against resources on the server.
# A RESTful API uses hypermedia links to define how data should be accessed, transformed or manipulated in real-time.
# ======================================================================================================================
# RESTful API architecture applies six key constraints:
# ======================================================================================================================
# 1) All requests are handled via a single outward-facing interface.
# 2) Client-server independence — development and functional changes on one side should not affect the other
# 3) Statelessness — the server does not retain any information about our session; every request is treated as new.
# 4) Caching — the API should specify whether it’s responses can be cached by the user (if a response is valid until a specific time, the API can tell us e.g. Expires Wed, 17 May 2020 07:12:27 UTC).
# 5) Use of layered systems — meaning the API is comprised of layers, where each layer connects to another, creating a modular structure.
# 6) If applicable, the API should be able to provide the user with executable code on request.

# ======================================================================================================================
# 4 Main Types of Requests  GET/POST/PUT/DELETE (standardized HTTP methods for RESTful Services)
# ======================================================================================================================
# POST:    requests.post()     (Create/Update Method) Adds new data to the server or Update (better use PUT as it is clearer what you are doing). e.g. add a new item to your inventory.
# GET:     requests.get()      (Read Method)   Retrieve information (like search results). This is the most common type of request. Using it, we can get the data we are interested in from those that the API is ready to share.
# PUT:     requests.put()      (Update/Replace Method) Updates existing information. Clearer than using POST for Updates. By Convention you pass all fields even those which are not being updated
# PATCH:   requests.patch()    (Update/Modify Method) This is used for partial updates, similar to PUT but by convention only send the updated values that are changing not all the fields
# DELETE:  requests.delete()   (Delete Method) Deletes existing information
# HEAD:    requests.head()     The HEAD method asks for a response identical to that of a GET request, but without the response body.
# OPTIONS: requests.options()  The OPTIONS method is used to describe the communication options for the target resource.
# CONNECT:                     The CONNECT method establishes a tunnel to the server identified by the target resource.
# TRACE:                       The TRACE method performs a message loop-back test along the path to the target resource.


# ======================================================================================================================
# <protocol>://<host>:<port>/<path>?<query_string>#<fragment>
# ======================================================================================================================
# <protocol>:  http, https, ftp
# <host>: 'en.wikipedia.org'
# <port>:  defaults are http=80, https=443
# <path>: 'wiki/url'
# <query_string>: key1=value1&key2=value2
# <fragment>: bookmark


# ======================================================================================================================
# Http Status Codes
# ======================================================================================================================
# 200 – (OK): The request was successful. The answer itself depends on the method used (GET, POST, etc.) and the API specification.
# 201 - (Created): request fulfilled and new resource created (POST/PUT)
# 202 - (Accepted): Workflow execution kicked off and running.
# 204 – No Content. The server successfully processed the request and did not return any content.
# 300 - (Multiple Choices): Workflow execution on hold due to pending User Input (response to include details on request)
# 301 - (Moved Permanently): The server responds that the requested page (endpoint) has been moved to another address and redirects to this address.
# 400 – (Bad Request): The server cannot process the request because the client-side errors (incorrect request format).
# 401 – (Unauthorized): Occurs when authentication was failed, due to incorrect credentials or even their absence.
# 403 – (Forbidden): Access to the specified resource is denied.
# 404 – (Not Found): The requested resource was not found on the server.
# 405 - (Method Not Allowed): unsupported Method request, unless you want to modify the collection itself
# 500 – (Internal Server Error): Occurs when an unknown error has occurred on the server.
# 502 - (Bad Gateway Error): The most common cause of this issue is an incorrect or outdated DNS record

import requests           # Use the requests library to simplify making a REST API call from Python
import json               # NOTE: this library is not required for response.json()

r = requests.get('https://api.github.com/events')  # Normal read request
r = requests.get('https://httpbin.org/get', params={'key1': 'value1', 'key2': 'value2'})  # Get Request with query string
r              # Displays <Response [200]>  <class 'requests.models.Response'>
r.url          # Shows you the URL as query string = 'https://httpbin.org/get?key1=value1&key2=value2'
r.text         # Displays the response body as text string (or json text string if response is of JSON format)
r.encoding     # Retrieves the current response encoding
r.content      # Displays the response body as bytes e.g. for binary image response
# r.json()     # returns JSON as type 'dict' if the response is in JSON, otherwise gives error json.decoder.JSONDecodeError
r.headers      # view the server’s response headers using a Python dictionary
r.status_code  # returns status e.g. 200
r.ok           # returns True when the status code, is  200 <= r.status_code < 400
r.cookies      # returns cookie jar object (see below)
r.elapsed      # returns timedelta for elapsed time
r.request      # returns object <class 'requests.models.PreparedRequest'>  with attributes of the original request

# Can provide a header token so the request appears to be coming from a certain browser
# mozilla = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
# url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
# res = requests.get(url, headers=mozilla)

r = requests.get('https://api.github.com/some/endpoint', headers={'user-agent': 'my-app/0.0.1'})  # Add headers to a request

# ======================================================================================================================
# Cookies and the Cookie Jar
# ======================================================================================================================
r = requests.get('http://example.com/some/cookie/setting/url')
r.cookies   # Retrieve cookies from server of type <class 'requests.cookies.RequestsCookieJar'>
r = requests.get('https://httpbin.org/cookies', cookies={'key1': 'value1'})  # Set Cookies on server with Request
r.text   # '{\n  "cookies": {\n    "key1": "value1"\n  }\n}\n'

jar = requests.cookies.RequestsCookieJar()
jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
r = requests.get('https://httpbin.org/cookies', cookies=jar)
r.text  # '{\n  "cookies": {\n    "tasty_cookie": "yum"\n  }\n}\n'

# ======================================================================================================================


requests.get('https://github.com/', timeout=0.1)  # set timeout for no response

# See https://www.w3schools.com/python/module_requests.asp
r = requests.get('https://httpbin.org/get', params={'key': 'value'})     # get(url, params=None, **kwargs))
r = requests.post('https://httpbin.org/post', data={'key': 'value'})     # post(url, data=None, json=None, **kwargs)
r = requests.put('https://httpbin.org/put', data={'key': 'value'})       # put(url, data=None, **kwargs)
r = requests.delete('https://httpbin.org/delete')                       # delete(url, **kwargs)
r = requests.head('https://httpbin.org/get')                            # head(url, **kwargs)
r = requests.options('https://httpbin.org/get')                         # options(url, **kwargs)
# requests.patch(url, data, args)	  # Sends a PATCH request to the specified url
# requests.request(method, url, args)  # Construct a generic request or any of the above types

# ======================================================================================================================
# API Example Starts Here
# ======================================================================================================================
SUBSCRIPTION_KEY = '8f4aab25bf22e16fd83edca15dac8029'  # safer to store in a .env file (see bezPy02) or vault
url = f'https://api.darksky.net/forecast/{SUBSCRIPTION_KEY}/40.8039314,-73.730418'


response = requests.get(url)       # response object
response_dict = response.json()    # This is actually a python dictionary

print(response)               # >> <Response [200]>
print(response.status_code)   # >>> 200
bool(response)                # True if the response is < 400
response.raise_for_status()   # Raises an exception if the call returns an error code, otherwise returns None

# requests.exceptions
try:
    response = requests.post("http://mi6.uk/agents/")

except requests.exceptions.ConnectionError:
    print("Connection Error occurred")


# ======================================================================================================================
# Sample Code for a POST
# requests.post(url, json=json_obj, headers=headers)
# requests.post(url, data=data, headers=headers)
# 'data' can be: A dictionary, list of tuples, bytes or a file object to send to the specified url  which has been serialized
# 'json' must be a json serializeable dictionary,  object will be encoded in the body as bytestring
# ======================================================================================================================
url = 'https://httpbin.org/post'
d = {'name': 'John', 'age': 21}
# 'Content-type' = input to expect,  'Accept' = acceptable output
response = requests.post(url, data=json.dumps(d), headers={'Content-Type': 'application/json', 'Accept': 'text/plain'})  # Same as below
response = requests.post(url, json=d)  # This automatically sets header={'content-type': 'application/json'}


if response.headers['Content-Type'].startswith('application/json'):
    r = response.json()  # Return json parsing result. Usually a dict, although some endpoints return a list.
else:
    r = response.text

# {
#   "args": {}, 
#   "data": "{\"name\": \"John\", \"age\": 21}", 
#   "files": {}, 
#   "form": {}, 
#   "headers": {
#     "Accept": "text/plain", 
#     "Accept-Encoding": "gzip, deflate", 
#     "Content-Length": "27", 
#     "Content-Type": "application/json", 
#     "Host": "httpbin.org", 
#     "User-Agent": "python-requests/2.27.1", 
#     "X-Amzn-Trace-Id": "Root=1-63595c91-10eda4b0173470356109f711"
#   }, 
#   "json": {
#     "age": 21, 
#     "name": "John"
#   }, 
#   "origin": "108.14.31.90", 
#   "url": "https://httpbin.org/post"
# }


headers = {'content-type': 'application/json'}  # json payloads
headers = {'content-type': 'application/xml'}   # xml payloads
headers = {'Content-Type': 'application/octet-stream', 'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY}  # passing an image directly
headers = {'Content-Type': 'application/x-www-form-urlencoded'}  # the body of the HTTP message sent is a query string
headers = {'Content-Type': 'multipart/form-data'}  # large binary payloads
headers = {'Content-Type': 'application/pdf'}  # pdf
headers = {'Content-Type': 'application/vnd.ms-excel'}  # excel

# https://www.geeksforgeeks.org/http-headers-content-disposition/
# Content-Disposition: inline    #  default value, indicating it can be displayed inside the Web page, or as the Web page
# Content-Disposition: attachment
# Content-Disposition: attachment; filename="filename.jpg"  # indicating it should be downloaded; most browsers presenting a 'Save as' dialog, prefilled with the value of the filename parameters if present
# Content-Disposition: form-data; name="field2"; filename="example.txt"    # this goes with mulitpart/form-data

# replace escape characters 
requests.utils.unquote('xxx%20xxx%3Axxx%3Dxxx')   # 'xxx xxx:xxx=xxx'

# encodes escape characters
requests.utils.quote('xxx xxx:xxx=xxx')       # 'xxx%20xxx%3Axxx%3Dxxx'


# SSL Error,  if you get the below error from a requests.post() execution then you need the library `pip install pip-system-certs`
# e.g.  ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: self signed certificate in certificate chain (_ssl.c:1045)
