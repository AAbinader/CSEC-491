import time
import gc
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, classification_report, accuracy_score
from sklearn.metrics import precision_score, recall_score
from sklearn.metrics import ConfusionMatrixDisplay
from matplotlib import pyplot as plt

def random_forest_model(data, display_time=False, display_advanced=False):

    start_time = time.time()
    df = pd.read_csv(data)
    df = df.dropna()
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
    end_time = time.time()

    if display_time:
        total_time = end_time - start_time
        print("RF Model Time: %fs" % (total_time))

    if display_advanced:
        report = classification_report(df_test['sentiment'], y_pred, output_dict=True, zero_division=1)
        print(report)
        # Plot and save confusion matrix using ConfusionMatrixDisplay
        fig, ax = plt.subplots(figsize=(10, 10))

    accuracy = accuracy_score(df_test['sentiment'], y_pred)
    print("Accuracy: " + str(round(accuracy*100, 2)) + "%")

    # Calculate and print weighted precision, recall, and F1 score
    precision = precision_score(df_test['sentiment'], y_pred, average='weighted')
    recall = recall_score(df_test['sentiment'], y_pred, average='weighted')
    f1 = f1_score(df_test['sentiment'], y_pred, average='weighted')
    
    print("Weighted Precision: " + str(round(precision*100, 2)) + "%")
    print("Weighted Recall: " + str(round(recall*100, 2)) + "%")
    print("Weighted F1 Score: " + str(round(f1*100, 2)) + "%")

# Example usage
print("OG Data")
random_forest_model('../data/reviews_labeled.csv', True, True)

print()
print("New Data (Short)")
random_forest_model('../data/reviews_relabeled_short.csv', True, True)

print()
print("New Data (Long)")
random_forest_model('../data/reviews_relabeled.csv', True, True)
