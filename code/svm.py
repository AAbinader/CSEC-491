import time
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

"""Support Vector Machine"""

# Function that takes a dataframe and splits it into training and testing data
def cross_validation(file_path):

    df = pd.read_csv(file_path)

    df_shuffled = shuffle(df)
    split_idx = int(len(df_shuffled) * 0.80)

    df_train = df_shuffled[:split_idx]
    df_test = df_shuffled[split_idx:]

    return df_train, df_test

# Function that runs the svm model using the supplied data and kernel
def svm_model(data, kernel, degree=None, display_time=False, display_advanced=False):

    df_train, df_test = cross_validation(data)
    vectorizer = TfidfVectorizer(min_df = 1,
                                max_df = 0.6,
                                sublinear_tf = True,
                                use_idf = False,
                                lowercase=False,
                                token_pattern=r'(?u)\b\w+\b|!')
    train_vec = vectorizer.fit_transform(df_train['reviews'])
    test_vec = vectorizer.transform(df_test['reviews'])

    if degree is None:
        classifier_linear = svm.SVC(kernel=kernel)
    else:
        classifier_linear = svm.SVC(kernel=kernel, degree=degree)


    t0 = time.time()
    classifier_linear.fit(train_vec, df_train['sentiment'])
    t1 = time.time()
    prediction_linear = classifier_linear.predict(test_vec)
    t2 = time.time()
    time_linear_train = t1 - t0
    time_linear_predict = t2 - t1

    if display_time:
        print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
        print()

    report = classification_report(df_test['sentiment'], prediction_linear, output_dict=True, zero_division=1)

    if display_advanced:
        print(report)
        print()

    if degree == None:
        degree = ''

    print("Kernel: " + str(kernel) + str(degree) + ", Accuracy: " + str(round(report['accuracy'] * 100, 2)) + "%")

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
