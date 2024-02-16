import nltk
import random
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# geeksforgeeks: https://www.geeksforgeeks.org/python-sentiment-analysis-using-vader/s
# analystics vidhya: https://www.analyticsvidhya.com/blog/2021/06/vader-for-sentiment-analysis/

file_path = '../data/reviews_raw.csv'
df = pd.read_csv(file_path)
print(df.shape)

example = df['reviews'][50]
tokens = nltk.word_tokenize(example)
tagged = nltk.pos_tag(tokens)
# print(tokens)
# print(tagged)

"""VADER - Bag of words approach. 1) stop words are removed 2) each word is scored and combined"""

sia = SentimentIntensityAnalyzer()

# Function to run the sentiment analyzer
def calculate_sentiment(row):
    review = row['reviews']
    sentiment = sia.polarity_scores(review)
    return sentiment

# Create the new column with sentiment scores
df['sentiment'] = df.apply(calculate_sentiment, axis=1)
print(df)
df.to_csv('vader.csv', index=False)

# Inspect random sample of rows
random_sample = df.sample(n=50)
for index, row in random_sample.iterrows():
    print(f"{row['reviews']}; Sentiment Score = {row['sentiment']['compound']}")
