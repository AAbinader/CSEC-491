import time
import pandas as pd
from rake_nltk import Rake

"""Rapid Automatic Keyword Extraction"""

start_time = time.time()
df = pd.read_csv('../data/skills_raw.csv')
aggregated_reviews = df.groupby('course_id')['skills'].apply(lambda x: ' '.join(x.astype(str))).reset_index()

max_words = 4
min_words = 1
rake_nltk_var = Rake(max_length=max_words, min_length=min_words)

for index, row in aggregated_reviews.iterrows():

    course_id = int(row['course_id'])
    rp_df = pd.read_csv('../data/skills_raw.csv')
    response_count = rp_df[rp_df['course_id'] == course_id]['course_id'].value_counts()

    num_keywords = max(int(response_count.iloc[0] / 10), 4)
    skills_text = row['skills']

    rake_nltk_var.extract_keywords_from_text(skills_text)
    keywords = rake_nltk_var.get_ranked_phrases_with_scores()[:num_keywords]
    
    print(f"Course ID: {course_id}")
    for score, kw in keywords:
        print(f"{kw} (Score: {score})")
    print("\n" + "-"*80 + "\n")

end_time = time.time()
total_time = end_time - start_time
print("RAKE Model Time: %.2fs" % (total_time))
print()

# This works a little bit better than YAKE. Still not great though!