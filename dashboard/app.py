import requests
import json
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/submit', methods=['POST'])
def submit_course_info():
    data = request.json
    course_name = data.get('courseName')
    season = data.get('season')
    year = data.get('year')

    codes = {"Spring": 1, "Summer": 2, "Fall": 3}
    season_code = str(year) + "0" + str(codes[season])
    
    course_id = get_course_id(course_name, season_code)
    if course_id == -1:
        return jsonify({"message": "Unable to process course information."}), 200
    
    reviews = get_course_reviews(course_id, "YC409")
    if reviews == -1:
        return jsonify({"message": "Unable to process course information."}), 200
    
    skills = get_course_reviews(course_id, "YC401")
    if skills == -1:
        return sonify({"message": "Unable to process course information."}), 200
    
    print(reviews)
    print(skills)

    return jsonify({"message": "Course information submitted successfully"}), 200

# Function to retrive a course id given the season code and course name
def get_course_id(course_name, season_code):

    url = 'https://api.coursetable.com/ferry/v1/graphql'

    course_query = f"""
    {{
        computed_listing_info(where: {{ season_code: {{_eq: "{season_code}"}}, course_code: {{_eq: "{course_name}"}} }}) {{
            course_id
        }}
    }}
    """

    cookie_file_path = '../data/cookie_value.txt'
    with open(cookie_file_path, 'r') as file:
        cookie_value = file.read().strip()

    headers = {
        'Content-Type': 'application/json',
    }

    headers['Cookie'] = cookie_value
    json_data = json.dumps({
        'query': course_query
    })

    response = requests.post(url, headers=headers, data=json_data)

    if response.status_code == 200:

        print("Success!")
        data = response.json()
        computed_listing_info = data['data']['computed_listing_info']

        if len(computed_listing_info) == 0:
            print("No valid course id.")
            return -1

        first_course_id = computed_listing_info[0]['course_id']
        return first_course_id

    else:
        print("Bad API Call")
        return -1
    
# Function to retrieve course reviews given a course id and question code
def get_course_reviews(course_id, question_code):

    course_id = course_id
    url = 'https://api.coursetable.com/ferry/v1/graphql'

    cookie_file_path = '../data/cookie_value.txt'
    with open(cookie_file_path, 'r') as file:
        cookie_value = file.read().strip()

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
    query = evaluations_query.format(course_id=course_id, question_code=question_code)

    json_data = json.dumps({
        'query': query
    })
    response = requests.post(url, headers=headers, data=json_data)

    if response.status_code == 200:

        print("Success!")
        data = response.json()
        reviews = data['data']['evaluation_narratives']

        if len(reviews) == 0:
            print("No course reviews.")
            return -1

        return reviews

    else:
        print("Bad API Call")
        return -1

if __name__ == '__main__':
    app.run(debug=True)
