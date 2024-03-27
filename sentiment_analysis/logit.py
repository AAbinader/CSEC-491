import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

"""Logistic Regression"""

# Function that runs the logit model using the supplied data
def logit_model(data, display_time=False, display_advanced=False):

    start_time = time.time()
    df = pd.read_csv(data)
    x_train, x_test, y_train, y_test = train_test_split(df['reviews'], df['sentiment'], test_size=0.2)

    pipeline = Pipeline([
    ('vect', CountVectorizer(lowercase=False, token_pattern=r'(?u)\b\w+\b|!')),
    ('tfidf', TfidfTransformer()),
    ('clf', LogisticRegression(multi_class='multinomial', solver='lbfgs'))
    ])

    pipeline.fit(x_train, y_train)
    predictions = pipeline.predict(x_test)
    end_time = time.time()

    if display_time:
        total_time = end_time - start_time
        print("Logit Model Time: %fs" % (total_time))
        print()

    if display_advanced:
        print("\nClassification Report:\n", classification_report(y_test, predictions))

    print("Accuracy: " + str(round(accuracy_score(y_test, predictions) * 100, 2)) + "%")

print("OG Data") 
logit_model('../data/reviews_labeled.csv')

print()
print("New Data (Short)")
logit_model('../data/reviews_relabeled_short.csv')

print()
print("New Data (Long)")
logit_model('../data/reviews_relabeled.csv')
