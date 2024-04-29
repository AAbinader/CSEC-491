import csv
import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Function that takes a dataframe and splits it into training and testing data
def cross_validation(df):

    df = df.dropna()
    df_shuffled = shuffle(df)
    split_idx = int(len(df_shuffled) * 0.80)
    df_train = df_shuffled[:split_idx]
    df_test = df_shuffled[split_idx:]
    return df_train, df_test

# Function that runs the SVM model using the supplied data and kernel
def svm_model(df, kernel, degree=None):

    df_train, df_test = cross_validation(df)
    vectorizer = TfidfVectorizer(min_df=1, max_df=0.6, sublinear_tf=True, use_idf=False, lowercase=False, token_pattern=r'(?u)\b\w+\b|!')
    train_vec = vectorizer.fit_transform(df_train['reviews'])
    test_vec = vectorizer.transform(df_test['reviews'])

    if degree is None:
        classifier = svm.SVC(kernel=kernel)
    else:
        classifier = svm.SVC(kernel=kernel, degree=degree)

    classifier.fit(train_vec, df_train['sentiment'])
    prediction = classifier.predict(test_vec)

    report = classification_report(df_test['sentiment'], prediction, output_dict=True, zero_division=1)
    accuracy = report['accuracy'] * 100
    weighted_avg = report['weighted avg']
    print(f"Kernel: {kernel}, Accuracy: {accuracy:.3f}%, Precision: {weighted_avg['precision']:.3f}, Recall: {weighted_avg['recall']:.3f}, F1-Score: {weighted_avg['f1-score']:.3f}")


stem_course_ids= list()
with open('../data/stem_course_ids.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        stem_course_ids.extend([int(num) for num in row])

social_course_ids= list()
with open('../data/social_course_ids.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        social_course_ids.extend([int(num) for num in row])

humanities_course_ids= list()
with open('../data/humanities_course_ids.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        humanities_course_ids.extend([int(num) for num in row])


df = pd.read_csv('../data/reviews_relabeled_short.csv')
stem_df = df[df['course_id'].isin(stem_course_ids)]
social_df = df[df['course_id'].isin(social_course_ids)]
humanities_df = df[df['course_id'].isin(humanities_course_ids)]

print(len(stem_df), len(social_df), len(humanities_df))

print("STEM Short")
svm_model(stem_df, 'linear')
print()

print("Social Short")
svm_model(social_df, 'linear')
print()

print("Humanities Short")
svm_model(humanities_df, 'linear')
print()

print()
print("*******************************************************")
print()

df = pd.read_csv('../data/reviews_relabeled.csv')
stem_df = df[df['course_id'].isin(stem_course_ids)]
social_df = df[df['course_id'].isin(social_course_ids)]
humanities_df = df[df['course_id'].isin(humanities_course_ids)]

print("STEM Long")
svm_model(stem_df, 'linear')
print()

print("Social Long")
svm_model(social_df, 'linear')
print()

print("Humanities Long")
svm_model(humanities_df, 'linear')
print()

# There actually is a noticable different. Humanities more accurate for 3-label but likely not
# enough observations to adequately train the model for the 5-label dataset.