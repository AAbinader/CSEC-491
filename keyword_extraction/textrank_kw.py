import time
import pandas as pd
import spacy
import pytextrank

"""TextRank Keyword Extraction"""

start_time = time.time()
nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("textrank")

df = pd.read_csv('../data/skills_raw.csv')
aggregated_reviews = df.groupby('course_id')['skills'].apply(lambda x: ' '.join(x.astype(str))).reset_index()

for index, row in aggregated_reviews.iterrows():
    course_id = int(row['course_id'])
    rp_df = pd.read_csv('../data/skills_raw.csv')
    response_count = rp_df[rp_df['course_id'] == course_id]['course_id'].value_counts()

    num_keywords = max(int(response_count.iloc[0] / 10), 4)
    skills_text = row['skills']

    doc = nlp(skills_text)
    tr_keywords = [(phrase.rank, phrase.text) for phrase in doc._.phrases[:num_keywords]]

    print(f"Course ID: {course_id}")
    for score, kw in tr_keywords:
        print(f"{kw} (Score: {score})")
    print("\n" + "-"*80 + "\n")

end_time = time.time()
total_time = end_time - start_time
print("TextRank Model Time: %.2fs" % (total_time))
print()

# This ones a bit better than RAKE and YAKE. Perhaps could improve them by setting to lowercase before
# running the model and maybe having a large list of manual words to remove or consolidate.