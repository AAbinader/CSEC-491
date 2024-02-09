import requests
import json
import csv

# URL for the GraphQL endpoint to CourseTable data
url = 'https://api.coursetable.com/ferry/v1/graphql'

# Query to get a list of courses with lots of information. Courses are from Spring 2023 and had at least 30 enrolled students
courses_query = """
{
  computed_listing_info(where: { season_code: {_eq: "202301"}, last_enrollment:{_gt: 30}, credits:{_eq: 1}, school:{_eq: "YC"}}) {
    course_id
    crn
    all_course_codes
    course_code
    credits
    professor_names
    title
    average_rating
    average_professor
    average_workload
    average_rating_same_professors
    average_workload_same_professors
    school
    areas
    skills
    last_enrollment
  }
}
"""

cookie_file_path = 'cookie_value.txt'
with open(cookie_file_path, 'r') as file:
    cookie_value = file.read().strip()

# Use 'Cookie' copy pasted from browser as authentication for the API call
headers = {
    'Content-Type': 'application/json',
}

headers['Cookie'] = cookie_value

# Convert the query to JSON format
json_data = json.dumps({
    'query': courses_query
})

# Make the POST request
response = requests.post(url, headers=headers, data=json_data)

# Check if the call was successful and output the json data to a file
if response.status_code == 200:
    print("Success!")
    file_name = 'courses.json'
    with open(file_name, 'w') as file:
        json.dump(response.json(), file)
else:
    print("Error:")
    print(response.text)

# Open the new json file and extract the data
with open('courses.json', 'r') as json_file:
    jsondata = json.load(json_file)

computed_listing_info = jsondata['data']['computed_listing_info']
 
# Write the data to a csv file
data_file = open('courses_raw.csv', 'w', newline='')
csv_writer = csv.writer(data_file)
 
count = 0
for data in computed_listing_info:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())
 
# This csv file is now ready for R
data_file.close()
