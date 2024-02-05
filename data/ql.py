import requests
import json

# URL for the GraphQL endpoint
url = 'https://api.coursetable.com/ferry/v1/graphql'

# Your GraphQL query
query = """
{
  evaluation_narratives(where: { question_code:{_eq: "YC409"} course_id: { _eq: 98156 } }) {
    course_id
    comment
    evaluation_question{question_text}
    question_code
    
  }
}
"""

# Headers, adjust as needed (e.g., add Authorization if required)
headers = {
    'Content-Type': 'application/json',
    'Cookie': 'express:sess=eyJwYXNzcG9ydCI6eyJ1c2VyIjoiYWphNjkifX0=; express:sess.sig=JOSXuMX2mbWXx23AU2pDVxZWsUs; ph_JBthuPpdaiJJGwHtoETN0Shc08K5b3VhSG2TweKm6nc_posthog=%7B%22%24user_state%22%3A%22identified%22%2C%22%24sesid%22%3A%5B1696735017720%2C%22018b0d49-3809-7c51-a76f-ab0e1b1cf3fa%22%2C1696734984201%5D%2C%22distinct_id%22%3A%22aja69%22%2C%22%24device_id%22%3A%22183aaa045bb48c-04d9ad351297cd-1a525635-13c680-183aaa045bc772%22%2C%22%24user_id%22%3A%22aja69%22%2C%22%24stored_person_properties%22%3A%7B%7D%7D; session=eyJwYXNzcG9ydCI6eyJ1c2VyIjoiYWphNjkifX0=; session.sig=DA68AytIC64xT3toZ13kqaHZvdw; G_ENABLED_IDPS=google'
}

# Convert the query to JSON format
json_data = json.dumps({
    'query': query
})

# Make the POST request
response = requests.post(url, headers=headers, data=json_data)

# Check and print the response
if response.status_code == 200:
    print("Success:")
    print(response.json())
else:
    print("Error:")
    print(response.status_code)
    print(response.text)
