import time
import pandas as pd
from yake import KeywordExtractor

"""Yet Another Keyword Extractor"""

start_time = time.time()
df = pd.read_csv('../data/skills_raw.csv')
aggregated_reviews = df.groupby('course_id')['skills'].apply(lambda x: ' '.join(x.astype(str))).reset_index()

language = "en"
max_ngram_size = 3
deduplication_threshold = 0.9

for index, row in aggregated_reviews.iterrows():

    course_id = int(row['course_id'])
    rp_df = pd.read_csv('../data/skills_raw.csv')
    response_count =rp_df[rp_df['course_id'] == course_id]['course_id'].value_counts()

    num_keywords = max(int(response_count.iloc[0] / 10), 4)
    skills_text = row['skills']

    kw_extractor = KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_threshold, top=num_keywords, features=None)
    keywords = kw_extractor.extract_keywords(skills_text)
    
    print(f"Course ID: {course_id}")
    for kw in keywords:
        print(kw)
    print("\n" + "-"*80 + "\n")

end_time = time.time()
total_time = end_time - start_time
print("YAKE Model Time: %.2fs" % (total_time))
print()

# This is pretty interesting but not very good for now. Will revisit!
