from openai import OpenAI

# Chat GPT API Calls
# Docs: https://platform.openai.com/docs/guides/rate-limits/usage-tiers?context=tier-free
# Docs: https://platform.openai.com/api-keys
# Docs: https://www.geeksforgeeks.org/how-to-use-chatgpt-api-in-python/
# Docs: https://github.com/openai/openai-python/blob/main/README.md

# Set your OpenAI API key here
client = OpenAI(
    api_key = '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'
)

test_review = "i learned a lot about the social and political atmosphere of various issues like the war on drugs, organized crime, police brutality, and more"
prompt = f"Please extract and list the keywords or phrases related to knowledge, skills, and insights mentioned in the following course review: {test_review}"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"{prompt}",
        }
    ],
    model="gpt-3.5-turbo",
    max_tokens=10,
)

response_text = chat_completion.choices[0].message.content
print(response_text)
