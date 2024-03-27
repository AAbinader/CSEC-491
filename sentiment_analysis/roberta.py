import numpy as np
import pandas as pd
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

# This file takes about 10 minutes to fully run

# RoBERTa: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment

file_path = '../data/reviews_raw.csv'
df = pd.read_csv(file_path)

"""RoBERTa - Significantly more advanced than VADER. Trained on a large collection of data. Captures relationships between words."""

source = f"cardiffnlp/twitter-roberta-base-sentiment" # this source can be changed (this is a database of Twitter tweets)
tokenizer = AutoTokenizer.from_pretrained(source)
model = AutoModelForSequenceClassification.from_pretrained(source)

# Go row by row and populate the RoBERTa sentiment column
progress = 0
for index, row in df.iterrows():
    review = row['reviews']
    encoded_text = tokenizer(review, return_tensors='pt')
    try:
        sentiment = model(**encoded_text)
    except:
        print("Exception")
        continue
    scores = sentiment[0][0].detach().numpy()
    scores = softmax(scores)
    scores = scores.tolist()
    scores = [round(num, 3) for num in scores]
    df.at[index, 'sentiment'] = str(scores)
    progress += 1
    print(progress)

# Write these changes to the CSV
df.to_csv('roberta.csv', index=False)
