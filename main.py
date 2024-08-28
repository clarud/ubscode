import json
import math

# Returns the euclidean distance between 2 points
def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Return score of student to school
def calculate_weightage(student, school):
    # Calculate distance score
    distance = calculate_euclidean_distance(student['homeLocation', school['location']])
    distance_score = 1 / (1 + distance)

    # Check for alumni
    is_alumni = 1 if student.get['alumni'] == school.get['name']) else 0

    # Check for volunteer
    is_volunteer = 1 if student.get['volunteer'] == school.get['name'] else 0

    score = 50 * distance_score + 30 * is_alumni + 20 * is_volunteer
    return score

# Define method to allocate students
def allocate_students(input_data):
    school_allocation = defaultdict(list)

    # Calculate weightage score for each student for each school
    weightage_score = [] # Store weightage score of each student in a list
    for student in input_data['students']:
        for school in input_data['schools']:
            score = calculate_weightage(student, school)
            weightage_score.append((school['name'], student['id'], score)

    # Sort weightage score
    weightage_score.sort(key = lambda x: (-x[2], x[1])) # Sort be descending score then ascending student id


# Read the input JSON
with open('input.json', 'r') as f:
    input_data = json.load(f)

# Allocate students to school
output_data = allocate_students(input_data)

# Write the output JSON
with open('output.json', 'w') as f:
    json.dump(output_data, f, indent = 4)