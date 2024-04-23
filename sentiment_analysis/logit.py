import time
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score

"""Logistic Regression"""

# Function that runs the logit model using the supplied data
def logit_model(data, display_time=False, display_advanced=False):

    start_time = time.time()
    df = pd.read_csv(data)
    df = df.dropna()
    df['reviews'] = df['reviews'].fillna('')
    df['sentiment'] = df['sentiment'].astype(str)
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
        print("Logit Model Time: %fs" % total_time)
        print()

    if display_advanced:
        print("\nClassification Report:\n", classification_report(y_test, predictions, zero_division=0))
        # Calculate and print weighted precision, recall, and F1 score
        precision = precision_score(y_test, predictions, average='weighted')
        recall = recall_score(y_test, predictions, average='weighted')
        f1 = f1_score(y_test, predictions, average='weighted')
        
        print("Weighted Precision: {:.2f}%".format(precision * 100))
        print("Weighted Recall: {:.2f}%".format(recall * 100))
        print("Weighted F1 Score: {:.2f}%".format(f1 * 100))

    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: " + str(round(accuracy * 100, 2)) + "%")

# Example usage
print("OG Data")
logit_model('../data/reviews_labeled.csv', True, True)

print()
print("New Data (Short)")
logit_model('../data/reviews_relabeled_short.csv', True, True)

print()
print("New Data (Long)")
logit_model('../data/reviews_relabeled.csv', True, True)
