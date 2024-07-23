#https://www.crummy.com/software/BeautifulSoup/bs4/doc/

from bs4 import BeautifulSoup
import requests
from time import sleep

url = 'http://www.netdania.com/currencies/usdils/netdania_fxa'
response = requests.get(url, timeout=5)
http_status = response.status_code # e.g. 200 = success

while True:
    bs = BeautifulSoup(response.content, "html.parser")
    x = float(bs.find(id = "ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelLast").text)
    y = bs.find(id = "ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelTimeStamp").text
    print(x,y)
    sleep(3)






    


# p = bs.prettify()
#bs.title  # <title>The Dormouse's story</title>

#bs.title.name  # u'title'

#bs.title.string  # u'The Dormouse's story'

#bs.title.parent.name  # u'head'

#bs.p  # <p class="title"><b>The Dormouse's story</b></p>

#bs.p['class'] # u'title'

#bs.a  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

#bs.find_all('a')
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

#bs.find(id="link3")
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>







## Example of HTML
##    <div class="nd-fq-middle">
##        <div class="nd-fq-change-trend-container" title="Today's trend">
##            <span id="ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelTrend" class="nd-fq-change-trend up" data-id="fq-recid-f14-trend"></span>
##        </div>
##        <div class="nd-fq-column2">
##            <div class="nd-fq-last-container nd-fq-last" data-id="fq-recid-f6" title="Last">
##                <span id="ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelLast">3.58178</span>
##           </div>
##            <div class="nd-fq-timestamp-container" data-id="fq-recid-f17" title="Time stamp">
##                <span id="ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelTimeStamp">20-16:17:24 GMT</span>
##            </div>
##        </div>
##        <div class="nd-fq-change-container">
##            <div class="nd-fq-change-net-container nd-fq-value nd-fq-bold" title="Today's net change" data-id="fq-recid-f14">
##                <span id="ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelChangeNet" class=" nd-fq-rise">+0.01500</span>
##            </div>
##            <div class="nd-fq-change-percent-container nd-fq-value nd-fq-bold" title="Today's percent change" data-id="fq-recid-f15">
##                <span id="ctl00_ctl00_MainContent_ContentBody_FullQuoteDescription_LabelChangePercent" class=" nd-fq-rise">+0.42000%</span>
##            </div>
##        </div>





    
