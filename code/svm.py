import time
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Support Vector Machine

file_path = '../data/reviews_labeled.csv'
df = pd.read_csv(file_path)

print("Shuffling")

df_shuffled = shuffle(df)
split_idx = int(len(df_shuffled) * 0.80)

print("Performing Cross-Validation")

df_train = df_shuffled[:split_idx]
df_test = df_shuffled[split_idx:]

print("Extracting Key Features")

vectorizer = TfidfVectorizer(min_df = 5,
                             max_df = 0.8,
                             sublinear_tf = True,
                             use_idf = True)
train_vec = vectorizer.fit_transform(df_train['reviews'])
test_vec = vectorizer.transform(df_test['reviews'])

print("Creating SVM Model")

classifier_linear = svm.SVC(kernel='linear')
t0 = time.time()
classifier_linear.fit(train_vec, df_train['sentiment'])
t1 = time.time()
prediction_linear = classifier_linear.predict(test_vec)
t2 = time.time()
time_linear_train = t1-t0
time_linear_predict = t2-t1

print()

print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
report = classification_report(df_test['sentiment'], prediction_linear, output_dict=True)
print('positive: ', report['pos'])
print('negative: ', report['neg'])
print('neutral: ', report['neu'])
print()
print("Accuracy: " + str(round(report['accuracy']*100, 2)) + "%")

# Roughly 84% accuracy! Only takes about 5 seconds to run.
