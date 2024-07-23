import sys
from time import sleep

# ======================================================================================================================
# urllib module from the standard library provides a URL-related API, also see urllib2
# ======================================================================================================================
from urllib.request import urlretrieve, urlopen, Request  # alternative library is 'requests' not from standard lib
from urllib import parse

# ======================================================================================================================
# urllib has 5 modules
# ======================================================================================================================
# request: opens urls
# response: used internally (will now work with this directly)
# error: to be used for request exceptions
# parse: to break up the url
# robotparser: inspects robots.txt files for permissions granted to bots/crawlers

url = 'https://www.wikipedia.org/'
res = urlopen(url)
res.code   # the response code
res.length # byte length of the response
res.peek() # displays first section of response
data = res.read()  # can read the full response as bytes only once, after which the connection is closed
data.decode('utf-8') # gives html as string


params = {'v': 'LosIGgon_KM',
          'list': 'PLi01XoE8jYohWFPpC17Z-wWhPOSuh8Er-',
          'index': '33'}
query_string = parse.urlencode(params)
url = 'https://www.youtube.com/watch?' + query_string
res = urlopen(url)
res.code
res.isclosed()  # returns False / checks to see if still connected to server
html = res.read().decode('utf-8')

# https://towardsdatascience.com/download-all-free-textbooks-from-springer-using-python-bd0b10e0ccc
# TRY THIS: https://towardsdatascience.com/how-to-download-files-using-python-ffbca63beb5c

import requests
import wget  # This is for downloading
import pandas as pd


df = pd.read_excel(".\myfiles\Free+English+textbooks.xlsx")
for index, row in df.iterrows():
        # loop through the excel list
        file_name = f"{row.loc['Book Title']}_{row.loc['Edition']}".replace('/','-').replace(':','-')
        url = f"{row.loc['OpenURL']}"
        r = requests.get(url)  # Url response
        download_url = f"{r.url.replace('book','content/pdf')}.pdf"  # Modify the URL string for download operation
        wget.download(download_url, f"./download/{file_name}.pdf")
        print(download_url,file_name)
        print(f"downloading {file_name}.pdf Complete ....")


# note that wget is based on urllib

# This fails as the webserver is blocking the urllib bot giving an "HTTP Error 403: Forbidden", access denied error
# urlretrieve(('https://beta.hebrewbooks.org/pagefeed/hebrewbooks_org_36093_12.pdf', 'hb_file'))


for i in range(1,47):
    index = str(i).zfill(2)
    url = f'https://beta.hebrewbooks.org/pagefeed/hebrewbooks_org_36093_{index}.pdf'
    req = Request(url, headers={"User-Agent": "Chrome"}) # THE REQUEST disguises the agent as a CHROME browser
    res = urlopen(req)   # THE RESPONSE
    f = open(f'{i}.pdf','wb')
    f.write(res.read())
    f.close()
    sleep(5)

    print(url)


# ======================================================================================================================
# urlparse module from the standard library
# ======================================================================================================================

from urllib.parse import urlparse
parsed = urlparse('http://netloc/path;parameters?query=argument#fragment')
# ParseResult(scheme='http', netloc='netloc', path='/path', params='parameters', query='query=argument', fragment='fragment')

# ======================================================================================================================
# furl module requires `pip install furl`  -- easier to use than urlparse
# ======================================================================================================================
from furl import furl
f = furl('http://netloc/path;parameters?query=argument#fragment')
