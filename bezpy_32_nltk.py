#  You do not know how this works yet



# natural language tool kit  see https://www.tutorialspoint.com/natural_language_processing/natural_language_processing_python.htm
# Natural language processing - process and analyze large amounts of natural language data. e.g speech recognition, 
# built-in python module 'tokenize': This module provides support for tokenizing strings useful in NLP  (splitting string into tokens)


from bs4 import BeautifulSoup
import re
import requests # see bezpy_26_requests.py
import heapq
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords


# Requires you to download the following using the command line ...
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')


def clean(text):
    text = re.sub(r"\[[0-9]*\]"," ",text)
    text = text.lower()
    text = re.sub(r'\s+'," ",text)
    text = re.sub(r","," ",text)
    return text



url = r'https://en.wikipedia.org/wiki/Python_(programming_language)'
num = 5  # number of summary sentance


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
res = requests.get(url,headers=headers)
summary = ""
soup = BeautifulSoup(res.text,'html.parser')
content = soup.findAll("p")
for text in content:
    summary +=text.text

summary = clean(summary)

print("Getting the data......\n")



sent_tokens = sent_tokenize(summary)  # Tokenizing

summary = re.sub(r"[^a-zA-z]"," ",summary)
word_tokens = word_tokenize(summary)  # Removing Stop words

word_frequency = {}
stopwords =  set(stopwords.words("english"))

for word in word_tokens:
    if word not in stopwords:
        if word not in word_frequency.keys():
            word_frequency[word]=1
        else:
            word_frequency[word] +=1
maximum_frequency = max(word_frequency.values())
print(maximum_frequency)
for word in word_frequency.keys():
    word_frequency[word] = (word_frequency[word]/maximum_frequency)
print(word_frequency)
sentences_score = {}
for sentence in sent_tokens:
    for word in word_tokenize(sentence):
        if word in word_frequency.keys():
            if (len(sentence.split(" "))) <30:
                if sentence not in sentences_score.keys():
                    sentences_score[sentence] = word_frequency[word]
                else:
                    sentences_score[sentence] += word_frequency[word]

print(max(sentences_score.values()))
def get_key(val):
    for key, value in sentences_score.items():
        if val == value:
            return key
key = get_key(max(sentences_score.values()))
print(key+"\n")
print(sentences_score)
summary = heapq.nlargest(num,sentences_score,key=sentences_score.get)
print(" ".join(summary))
summary = " ".join(summary)



# Text to Speech module
import pyttsx3
speaker = pyttsx3.init()
speaker.say('Testing, testing. This is a test.')
speaker.runAndWait() # executes above speech and continutes flow when completed.
speaker.stop()