import time
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

"""TFIDF Keyword Extraction"""

start_time = time.time()
df = pd.read_csv('../data/skills_raw.csv')
reviews_by_course = df.groupby('course_id')['skills'].apply(list).to_dict()

def preprocess_reviews(reviews):
    return [str(review).lower() for review in reviews if pd.notnull(review)]

vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(2,4))

for course_id, reviews in reviews_by_course.items():
    preprocessed_reviews = preprocess_reviews(reviews)
    
    tfidf_matrix = vectorizer.fit_transform(preprocessed_reviews)
    feature_names = vectorizer.get_feature_names_out()
    
    avg_tfidf_scores = np.mean(tfidf_matrix.toarray(), axis=0)
    top_indices = avg_tfidf_scores.argsort()[-5:][::-1]
    
    keywords = [feature_names[index] for index in top_indices]
    print(f"Course ID: {course_id}")
    for kw in keywords:
        print(kw)
    print("\n" + "-"*80 + "\n")

end_time = time.time()
total_time = end_time - start_time
print("TFIDF Model Time: %.2fs" % (total_time))
print()
