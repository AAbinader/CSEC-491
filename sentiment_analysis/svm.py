import time
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Function that takes a dataframe and splits it into training and testing data
def cross_validation(file_path):
    df = pd.read_csv(file_path)
    df = df.dropna()
    df_shuffled = shuffle(df)
    split_idx = int(len(df_shuffled) * 0.80)
    df_train = df_shuffled[:split_idx]
    df_test = df_shuffled[split_idx:]
    return df_train, df_test

# Function that runs the SVM model using the supplied data and kernel
def svm_model(data, kernel, degree=None, display_time=False):
    df_train, df_test = cross_validation(data)
    vectorizer = TfidfVectorizer(min_df=1, max_df=0.6, sublinear_tf=True, use_idf=False, lowercase=False, token_pattern=r'(?u)\b\w+\b|!')
    train_vec = vectorizer.fit_transform(df_train['reviews'])
    test_vec = vectorizer.transform(df_test['reviews'])

    if degree is None:
        classifier = svm.SVC(kernel=kernel)
    else:
        classifier = svm.SVC(kernel=kernel, degree=degree)

    t0 = time.time()
    classifier.fit(train_vec, df_train['sentiment'])
    t1 = time.time()
    prediction = classifier.predict(test_vec)
    t2 = time.time()
    time_train = t1 - t0
    time_predict = t2 - t1

    if display_time:
        print("Training time: {:.2f}s; Prediction time: {:.2f}s".format(time_train, time_predict))

    report = classification_report(df_test['sentiment'], prediction, output_dict=True, zero_division=1)
    accuracy = report['accuracy'] * 100
    weighted_avg = report['weighted avg']
    print("Training time: {:.2f}s; Prediction time: {:.2f}s".format(time_train, time_predict))
    print(f"Kernel: {kernel}, Accuracy: {accuracy:.3f}%, Precision: {weighted_avg['precision']:.3f}, Recall: {weighted_avg['recall']:.3f}, F1-Score: {weighted_avg['f1-score']:.3f}")

    print()
    
print("OG Data")
svm_model('../data/reviews_labeled.csv', 'linear')
svm_model('../data/reviews_labeled.csv', 'rbf')
svm_model('../data/reviews_labeled.csv', 'sigmoid')
svm_model('../data/reviews_labeled.csv', 'poly', 2)
svm_model('../data/reviews_labeled.csv', 'poly', 3)
svm_model('../data/reviews_labeled.csv', 'poly', 4)
svm_model('../data/reviews_labeled.csv', 'poly', 5)
svm_model('../data/reviews_labeled.csv', 'poly', 6)

print()
print("New Data (Short)")
svm_model('../data/reviews_relabeled_short.csv', 'linear')
svm_model('../data/reviews_relabeled_short.csv', 'rbf')
svm_model('../data/reviews_relabeled_short.csv', 'sigmoid')
svm_model('../data/reviews_relabeled_short.csv', 'poly', 2)
svm_model('../data/reviews_relabeled_short.csv', 'poly', 3)
svm_model('../data/reviews_relabeled_short.csv', 'poly', 4)
svm_model('../data/reviews_relabeled_short.csv', 'poly', 5)
svm_model('../data/reviews_relabeled_short.csv', 'poly', 6)

print()
print("New Data (Long)")
svm_model('../data/reviews_relabeled.csv', 'linear')
svm_model('../data/reviews_relabeled.csv', 'rbf')
svm_model('../data/reviews_relabeled.csv', 'sigmoid')
svm_model('../data/reviews_relabeled.csv', 'poly', 2)
svm_model('../data/reviews_relabeled.csv', 'poly', 3)
svm_model('../data/reviews_relabeled.csv', 'poly', 4)
svm_model('../data/reviews_relabeled.csv', 'poly', 5)
svm_model('../data/reviews_relabeled.csv', 'poly', 6)

# Adjusted default settings to take capitalization and exclamation points into account
