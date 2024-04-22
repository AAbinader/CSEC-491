import pandas as pd
from sklearn.utils import shuffle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm

# Function that takes a dataframe and cleans it for model training
def clean_data(file_path):

    df = pd.read_csv(file_path)
    df = df.dropna()
    return df

# Function that trains the SVM model using the supplied data and kernel
def train_svm_model(data_path, kernel='linear', degree=None):

    df_train = clean_data(data_path)
    vectorizer = TfidfVectorizer(min_df=1, max_df=0.6, sublinear_tf=True, use_idf=False, lowercase=False, token_pattern=r'(?u)\b\w+\b|!')
    train_vec = vectorizer.fit_transform(df_train['reviews'])

    if degree is None:
        classifier = svm.SVC(kernel=kernel)
    else:
        classifier = svm.SVC(kernel=kernel, degree=degree)

    classifier.fit(train_vec, df_train['sentiment'])
    return classifier, vectorizer

# Function to classify new incoming data
def classify_new_data(texts, classifier, vectorizer):
    text_vec = vectorizer.transform([texts])
    prediction = classifier.predict(text_vec)
    return prediction[0]

# Returns the proportions of sr, r, neu, dr, and sdr to the server
def classify_reviews(reviews):

    data_path = '../data/reviews_relabeled.csv'
    svm_classifier, vectorizer = train_svm_model(data_path)

    label_counts = {'sr': 0, 'r': 0, 'neu': 0, 'dr': 0, 'sdr': 0}
    for review in reviews:

        label = classify_new_data(review, svm_classifier, vectorizer)
        if label in label_counts:
            label_counts[label] += 1
        else:
            label_counts[label] = 1

    return label_counts
