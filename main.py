import json
import math

# Returns the euclidean distance between 2 points
def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define method to allocate students
def allocate_students(input_data):
    school_allocation = defaultdict(list)

    # Calculate weightage score for each student for each school
    weightage_score = []
    for student in input_data['students']:

# Read the input JSON
with open('input.json', 'r') as f:
    input_data = json.load(f)

# Allocate students to school
output_data = allocate_students(input_data)

# Write the output JSON
with open('output.json', 'w') as f:
    json.dump(output_data, f, indent = 4)