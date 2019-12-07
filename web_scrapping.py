# Web-Scrapping and Pre-processing/Cleaning Wikipedia data

import nltk
import bs4 as bs
import urllib as url
import re

from nltk.corpus import stopwords
nltk.download('stopwords')

data = urb.request.urlopen('').read()

soup = bs.BeautifulSoup(data , 'lxml')

text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

sentences = nltk.sent_tokenize(text)
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
