import random
import re
from openai import OpenAI

def extract_skills(skills): 

    num_skills = min(20, len(skills))
    skills = random.sample(skills, num_skills)
    skills_string = '\n'.join(f"Review {index + 1}: {skill}" for index, skill in enumerate(skills))

    # This is a security risk. My account only has $5 though :)
    client = OpenAI(
        api_key = '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'
    )

    # This prompt works super well! DO NOT TOUCH!
    prompt = f"The following are a set of student responses to this end of semester survey question: 'What knowledge, skills, and insights did you develop by taking this course?' I would like for you to read through the responses and summarize the key knowledge, skills, and insights in a list. These can be words or SHORT phrases on broader topics and please order them by importance. Only list 4 to 7 items! Here are the responses: \n{skills_string}"

    response = client.completions.create(
        prompt=prompt,
        model="gpt-3.5-turbo-instruct",
        max_tokens=100,
        temperature=0.2
    )

    response_text = response.choices[0].text

    split_skills = re.split(r'(?m)^\d+\.\s*', response_text)
    split_skills = [skill.strip() for skill in split_skills if skill.strip()]

    if split_skills[0] == '.':
        split_skills = split_skills[1:]

    if len(split_skills) <= 7:
        return split_skills
    else:
        return split_skills[0:6]


def extract_swi(swis): 

    num_swi = min(20, len(swis))
    swis = random.sample(swis, num_swi)
    swi_string = '\n'.join(f"Review {index + 1}: {swi}" for index, swi in enumerate(swis))

    # This is a security risk. My account only has $5 though :)
    client = OpenAI(
        api_key = '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'
    )

    # This prompt works super well! DO NOT TOUCH!
    prompt = f"The following are a set of student responses to this end of semester survey question: 'What are the strengths and weaknesses of this course and how could it be improved?' I would like for you to read through the responses and summarize the key strengths, weaknesses, and improvements in 3 separate lists. These can be words or SHORT phrases. Only list 3 to 5 items for each list! Here are the responses: \n{swi_string}"

    response = client.completions.create(
        prompt=prompt,
        model="gpt-3.5-turbo-instruct",
        max_tokens=250,
        temperature=0.2
    )

    response_text = response.choices[0].text

    strengths_text = re.search(r"Strengths:\s*(.+?)\s*\n(?=Weaknesses:|$)", response_text, re.S)
    weaknesses_text = re.search(r"Weaknesses:\s*(.+?)\s*\n(?=Improvements:|$)", response_text, re.S)
    improvements_text = re.search(r"Improvements:\s*(.+?)\s*$", response_text, re.S)

    # Function to split section content into list items
    def split_items(section_text):
        if not section_text:
            return []
        # Clean the text and split by numbers that mark new list items
        items = re.split(r'(?m)^\d+\.\s*', section_text.group(1).strip())
        return [item.strip() for item in items if item.strip()]

    # Apply the function to each section
    strengths = split_items(strengths_text)
    weaknesses = split_items(weaknesses_text)
    improvements = split_items(improvements_text)

    if len(strengths) > 5:
        strengths = strengths[0:4]
    if len(weaknesses) > 5:
        weaknesses = weaknesses[0:4]
    if len(improvements) > 5:
        improvements = improvements[0:4]

    return strengths, weaknesses, improvements