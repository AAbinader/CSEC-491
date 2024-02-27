import time
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Logistic Regression

file_path = '../data/reviews_labeled.csv'
df = pd.read_csv(file_path)

print("Shuffling")

df_shuffled = shuffle(df)
split_idx = int(len(df_shuffled) * 0.80)

print("Performing Cross-Validation")

df_train = df_shuffled[:split_idx]
df_test = df_shuffled[split_idx:]
