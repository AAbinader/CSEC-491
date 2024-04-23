import random
import pandas as pd
from openai import OpenAI

"""ChatGPT API Keyword Extraction"""

df = pd.read_csv('../data/swi_raw.csv')
swi_by_course = df.groupby('course_id')['streng_weak_improv'].apply(list).to_dict()
# print(len(skills_by_course)) 140 courses

# We will take a random sample of 15 reviews to pass to the ChatGPT API. With a more advanced
# model, we wouldn't need to worry about these token limits, however.
for id, reviews in swi_by_course.items():

    if len(reviews) > 20:
        swi_by_course[id] = random.sample(reviews, 20)

"""   
for id, reviews in skills_by_course.items():

    print(f"Course ID: {id}, Number of Reviews: {len(reviews)}")
    tokens = sum(len(review) for review in reviews)
    print(f"Tokens: {tokens}")

    On average, if there are 15 reviews sampled we get ~3000 tokens
"""

# Collapse the list into a string format suitable for ChatGPT
test_id = random.choice(list(swi_by_course.keys()))
swis = swi_by_course[test_id]
swi_string = '\n'.join(f"Review {index + 1}: {swi}" for index, swi in enumerate(swis))

# This is a security risk. My account only has $5 though :)
client = OpenAI(
    api_key = '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'
)

# This prompt works super well! DO NOT TOUCH!
prompt = f"The following are a set of student responses to this end of semester survey question: 'What are the strengths and weaknesses of this course and how could it be improved?' I would like for you to read through the responses and summarize the key strengths, weaknesses, and improvements in 3 separate lists. These can be words or SHORT phrases. Only list 3 to 5 items for each list! Here are the responses: \n{swi_string}"
print(prompt)
print("\n\n")

response = client.completions.create(
    prompt=prompt,
    model="gpt-3.5-turbo-instruct",
    max_tokens=150,
    temperature=0.2
)

response_text = response.choices[0].text
print(response_text)
