import gc
import seaborn as sn
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

# Random Forest

file_path = '../data/reviews_labeled.csv'
df = pd.read_csv(file_path)

print("Shuffling")

df_shuffled = shuffle(df)
split_idx = int(len(df_shuffled) * 0.80)

print("Performing Cross-Validation")

df_train = df_shuffled[:split_idx]
df_test = df_shuffled[split_idx:]

print("Vectorizing")

vectorizer = HashingVectorizer()

train_matrix = vectorizer.transform(df_train['reviews'].values.astype('U'))
test_matrix = vectorizer.transform(df_test['reviews'].values.astype('U'))

print("Creating Random Forest Model")

gc.collect()
clf = RandomForestClassifier()
rf = clf.fit(train_matrix, df_train['sentiment'])

y_pred = rf.predict(test_matrix)
f1_score(y_pred, df_test.sentiment, average='weighted')

cm = confusion_matrix(df_test.sentiment, y_pred)
print(cm)

sn.heatmap(cm, annot=True, fmt='d')
plt.xlabel('Predicted')
plt.ylabel('Truth')

accuracy = accuracy_score(df_test['sentiment'], y_pred)
print("Accuracy: " + str(round(accuracy*100, 2)) + "%")

# Roughly 74% accuracy. Takes around 10 minutes to run.
