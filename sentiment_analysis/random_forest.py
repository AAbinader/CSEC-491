import time
import gc
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt

"""Random Forest"""

# Function that runs the random forest model using the supplied data
def random_forest_model(data, display_time=False, display_advanced=False):

    start_time = time.time()
    df = pd.read_csv(data)
    df_shuffled = shuffle(df)
    split_idx = int(len(df_shuffled) * 0.80)

    df_train = df_shuffled[:split_idx]
    df_test = df_shuffled[split_idx:]

    vectorizer = HashingVectorizer(lowercase=False, token_pattern=r'(?u)\b\w+\b|!')

    train_matrix = vectorizer.transform(df_train['reviews'].values.astype('U'))
    test_matrix = vectorizer.transform(df_test['reviews'].values.astype('U'))

    gc.collect()
    clf = RandomForestClassifier()
    rf = clf.fit(train_matrix, df_train['sentiment'])

    y_pred = rf.predict(test_matrix)
    f1_score(y_pred, df_test.sentiment, average='weighted')
    end_time = time.time()

    if display_time:
        total_time = end_time - start_time
        print("RF Model Time: %fs" % (total_time))

    if display_advanced:
        report = classification_report(df_test['sentiment'], y_pred)
        print(report)

    accuracy = accuracy_score(df_test['sentiment'], y_pred)
    print("Accuracy: " + str(round(accuracy*100, 2)) + "%")

# Random forest takes about 5 minutes to run
    
print("OG Data")
random_forest_model('../data/reviews_labeled.csv', True, False)

print()
print("New Data (Short)")
random_forest_model('../data/reviews_relabeled_short.csv', True, False)

print()
print("New Data (Long)")
random_forest_model('../data/reviews_relabeled.csv', True, False)
