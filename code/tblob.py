import nltk
import random
import pandas as pd
from textblob import TextBlob

file_path = '../data/reviews_raw.csv'
df = pd.read_csv(file_path)

"""TextBlob - very similar to the VADER approach, inferior to the RoBERTa model"""

# Go row by row and populate the TextBlob sentiment column
for index, row in df.iterrows():
    review = row['reviews']
    polarity = TextBlob(review).sentiment.polarity
    polarity = round(polarity, 3)
    subjectivity = TextBlob(review).sentiment.subjectivity
    subjectivity = round(subjectivity, 3)
    result = f"{{'polarity': {polarity}, 'subjectivity': {subjectivity}}}"
    df.at[index, 'sentiment'] = result

# Write these changes to the CSV
df.to_csv('tblob.csv', index=False)
