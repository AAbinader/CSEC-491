import requests
import json
import csv
import os

question_code = "YC401"
output_file = "skills_raw.csv"
response_type = "Skills"
column_name = "skills"

# Read the course_numbers from our CSV into a list
course_ids= list()
with open('course_ids.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for row in reader:
        course_ids.extend([int(num) for num in row])

# URL for the GraphQL endpoint to CourseTable data
url = 'https://api.coursetable.com/ferry/v1/graphql'

# Get cookie signature from the cookie file
cookie_file_path = 'cookie_value.txt'
with open(cookie_file_path, 'r') as file:
    cookie_value = file.read().strip()

# Use 'Cookie' copy pasted from browser as authentication for the API call
headers = {
    'Content-Type': 'application/json',
}

headers['Cookie'] = cookie_value

evaluations_query = """
  {{
    evaluation_narratives(where: {{ question_code:{{_eq: {question_code}}} course_id: {{ _eq: {course_id} }} }}) {{
      comment 
    }}
  }}
"""

successes = 0
num_responses = 0
comments_by_course = dict()

# Write to the CSV file
with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    col_names = ["course_id", column_name]
    writer.writerow(col_names)

# Loop through each course ID and create the query
for course_id in course_ids:
    query = evaluations_query.format(course_id=course_id, question_code=question_code)

    # Convert the query to JSON format
    json_data = json.dumps({
        'query': query
    })

    # Make the POST request
    response = requests.post(url, headers=headers, data=json_data)

    # Check number of successful calls
    if response.status_code == 200:
        file_name = 'reviews.json'
        with open(file_name, 'w') as file:
            json.dump(response.json(), file)        
        successes += 1

    # Open the new json file and extract the data
    with open('reviews.json', 'r') as json_file:
        jsondata = json.load(json_file)

    # Read the course reviews into an object and then delete the file to be reused on the next call
    course_responses = jsondata['data']['evaluation_narratives']
    os.remove('reviews.json')

    with open(output_file, 'a', newline='', encoding='utf-8') as file:

        writer = csv.writer(file)
        for review in course_responses:

            comment = review['comment']
            num_responses += 1
            writer.writerow([course_id, comment])

# Print total number of calls and reviews
print("Successful Calls: " + str(successes))
print("Total " + response_type + ": " + str(num_responses))
