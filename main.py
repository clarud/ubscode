import json




# Read the input JSON
with open('input.json', 'r') as f:
    input_data = json.load(f)

# Allocate students to school
output_data = allocate_students(input_data)

# Write the output JSON
with open('output.json', 'w') as f:
    json.dump(output_data, f, indent = 4)