from bs4 import BeautifulSoup
import requests   # see bezpy_26_requests.py
import json

url = 'http://ethans_fake_twitter_site.surge.sh'
response = requests.get(url, timeout=5)
http_status = response.status_code # e.g. 200 = success

bs = BeautifulSoup(response.content, "html.parser")
tweet_list = []

for tweet in bs.find_all('div', attrs={"class": "tweetcontainer"}):
    tweet_obj = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text,
        "likes": tweet.find('p', attrs={"class": "likes"}).text,
        "shares": tweet.find('p', attrs={"class": "shares"}).text}
    tweet_list.append(tweet_obj)


## Example of HTML
##---------------------------------------------------
## <div class="tweetcontainer">
##   <h2 class="author">jimmyfallon</h2>
##   <p class="content">Don't miss tonight's show!</p>
##   <h5 class="dateTime">17/01/2017 13:47</h5>
##   <p class="likes">Likes  184</p>
##   <p class="shares">Shares  42</p>
## </div>



## Example of a tweet_obj
##---------------------------------------------------    
## tweet_obj = {
##              "author" : "JimmyFallon",
##              "date"   : "17/01/2017 13:47",
##              "tweet"  : "Don't miss tonight's show!",
##              "likes"  : "Likes  184",
##              "shares" : "Shares  42"}




# JSON FILE IS AN ARRAY OF OBJECTS  [{...}, {...}, ...]  easier to manage 
with open('.\\mydata\\twitter1.json', 'w') as outfile:
    json.dump(tweet_list, outfile)


# Generate Nested Dictionary {'0':{...}, '1':{...}, ...
keys = list(range(len(tweet_list)))
values = tweet_list
tweet_dict = {k:v for k, v in zip(keys, values)}


# JSON FILE IS A NESTED DICTIONARY
with open('.\\mydata\\twitter2.json', 'w') as outfile:
    json.dump(tweet_dict, outfile)

with open('.\\mydata\\twitter1.json') as json_data:
    jd = json.load(json_data)

    
