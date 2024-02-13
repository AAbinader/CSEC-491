import nltk
import pandas as pd
from transformers import AutoTokenizer
from transformers import AutoModelForSequenceClassification
from scipy.special import softmax

# RoBERTa: https://huggingface.co/cardiffnlp/twitter-roberta-base-sentiment

file_path = '../data/reviews_raw.csv'
df = pd.read_csv(file_path)

"""RoBERTa - Significantly more advanced than VADER. Trained on a large collection of data."""

source = f"cardiffnlp/twitter-roberta-base-sentiment"
tokenizer = AutoTokenizer.from_pretrained(source)
model = AutoModelForSequenceClassification.from_pretrained(source)


