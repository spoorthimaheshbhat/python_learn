# Using:

student = {
    "name": "Alice",
    "age": 21
}

# Print:

print(student.get("age"))
print(student.get("salary"))

# Explain the difference. - get() function safely (without throwing an error) checks if required key-value pair exists in the dictionary or not
# and returns the value if key exists. If not it returns 'None'