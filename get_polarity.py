import sys
import pandas as pd 
from textblob import TextBlob

source = sys.argv[1]
destination = sys.argv[2]
separator = sys.argv[3]
column_names = sys.argv[4]

column_names = list(map(str, column_names.split(',')))

def extract_sentiment(review):
    textblob = TextBlob(review)
    sentiment = textblob.sentiment
    polarity = sentiment.polarity 
    return polarity

reviews = pd.read_csv(source, sep=separator, names=column_names)
reviews.dropna(inplace=True)

reviews['Polarity'] = reviews['content'].apply(lambda x: extract_sentiment(str(x)))

reviews.to_csv(destination)