import json
import math
from collections import defaultdict, OrderedDict

# Returns the euclidean distance between 2 points
def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Return score of student to school
def calculate_weightage(student, school):
    # Calculate distance score
    distance = calculate_euclidean_distance(student['homeLocation'], school['location'])
    distance_score = 1 / (1 + distance)

    # Check for alumni
    is_alumni = 1 if student.get('alumni') == school['name'] else 0

    # Check for volunteer
    is_volunteer = 1 if student.get('volunteer') == school['name'] else 0

    score = 50 * distance_score + 30 * is_alumni + 20 * is_volunteer
    return score

# Define method to allocate students
def allocate_students(input_data):
    school_allocation = defaultdict(list)

    school_capacity = {school['name']: school['maxAllocation'] for school in input_data['schools']}

    # Calculate weightage score for each student for each school
    weightage_score = [] # Store weightage score of each student in a list
    for student in input_data['students']:
        for school in input_data['schools']:
            score = calculate_weightage(student, school)
            weightage_score.append((school['name'], student['id'], score))

    # Sort weightage score
    weightage_score.sort(key = lambda x: (-x[2], x[1])) # Sort be descending score then ascending student id

    # Allocate student to school
    for school_name, student_id, score in weightage_score:
        if school_capacity[school_name] > 0:
            school_allocation[school_name].append(student_id)
            school_capacity[school_name] -= 1

    # Order the output to match json
    ordered_school_allocation = OrderedDict()
    for school in sorted(school_allocation.keys()):
        ordered_school_allocation[school] = school_allocation[school]

    output_data = [{school: students} for school, students in ordered_school_allocation.items()]

    return output_data

# Read the input JSON
with open('input.json', 'r') as f:
    input_data = json.load(f)

# Allocate students to school
output_data = allocate_students(input_data)

# Write the output JSON
with open('output.json', 'w') as f:
    json.dump(output_data, f, indent = 4)