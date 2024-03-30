import warnings
import time
import pandas as pd
from keybert import KeyBERT

"""KeyBERT Keyword Extraction"""

warnings.filterwarnings('ignore')

start_time = time.time()
df = pd.read_csv('../data/skills_raw.csv')
aggregated_reviews = df.groupby('course_id')['skills'].apply(lambda x: ' '.join(x.astype(str))).reset_index()

kw_model = KeyBERT()

for index, row in aggregated_reviews.iterrows():
    course_id = int(row['course_id'])
    rp_df = pd.read_csv('../data/skills_raw.csv')
    response_count = rp_df[rp_df['course_id'] == course_id]['course_id'].value_counts()

    num_keywords = max(int(response_count.iloc[0] / 10), 4)
    skills_text = row['skills']
    keywords = kw_model.extract_keywords(skills_text, keyphrase_ngram_range=(1, 4), stop_words='english', top_n=num_keywords)

    print(f"Course ID: {course_id}")
    for kw, score in keywords:
        print(f"{kw} (Score: {score})")
    print("\n" + "-"*80 + "\n")

end_time = time.time()
total_time = end_time - start_time
print("KeyBERT Model Time: %.2fs" % (total_time))
print()

# This one is not very good at all...