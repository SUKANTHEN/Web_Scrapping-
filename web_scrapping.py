# Web-Scrapping and Pre-processing/Cleaning Wikipedia data

import nltk            
import bs4 as bs        
import urllib as url
import re

from nltk.corpus import stopwords 

# Scrapping the data from Wikipedia about Steve Jobs
data = url.request.urlopen('https://en.wikipedia.org/wiki/Steve_Jobs').read()

#Parsing the data
soup = bs.BeautifulSoup(data , 'lxml')

# Fetching the data from the source
text = ""
for paragraph in soup.find_all('p'):
    text += paragraph.text

# Pre-processing and cleaning the data
text = re.sub(r'\[[0-9]*\]',' ',text)
text = re.sub(r'\s+',' ',text)
text = text.lower()
text = re.sub(r'\d',' ',text)
text = re.sub(r'\s+',' ',text)

# Convert the paragrapgs to sentences
sentences = nltk.sent_tokenize(text)

# Convert the sentences to words
words = [nltk.word_tokenize(sentence) for sentence in sentences]

