import random
import pandas as pd
from openai import OpenAI

"""ChatGPT API Keyword Extraction"""

df = pd.read_csv('../data/skills_raw.csv')
skills_by_course = df.groupby('course_id')['skills'].apply(list).to_dict()
# print(len(skills_by_course)) 140 courses

# We will take a random sample of 15 reviews to pass to the ChatGPT API. With a more advanced
# model, we wouldn't need to worry about these token limits, however.
for id, reviews in skills_by_course.items():

    if len(reviews) > 20:
        skills_by_course[id] = random.sample(reviews, 20)

"""   
for id, reviews in skills_by_course.items():

    print(f"Course ID: {id}, Number of Reviews: {len(reviews)}")
    tokens = sum(len(review) for review in reviews)
    print(f"Tokens: {tokens}")

    On average, if there are 15 reviews sampled we get ~3000 tokens
"""

# Collapse the list into a string format suitable for ChatGPT
test_id = random.choice(list(skills_by_course.keys()))
skills = skills_by_course[test_id]
skills_string = '\n'.join(f"Review {index + 1}: {skill}" for index, skill in enumerate(skills))

# This is a security risk. My account only has $5 though :)
client = OpenAI(
    api_key = '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'
)

# This prompt works super well! DO NOT TOUCH!
prompt = f"The following are a set of student responses to this end of semester survey question: 'What knowledge, skills, and insights did you develop by taking this course?' I would like for you to read through the responses and summarize the key knowledge, skills, and insights in a list. These can be words or SHORT phrases on broader topics and please order them by importance. Only list 4 to 7 items! Here are the responses: \n{skills_string}"
print(prompt)
print("\n\n")

response = client.completions.create(
    prompt=prompt,
    model="gpt-3.5-turbo-instruct",
    max_tokens=100,
    temperature=0.2
)

response_text = response.choices[0].text
print(response_text)