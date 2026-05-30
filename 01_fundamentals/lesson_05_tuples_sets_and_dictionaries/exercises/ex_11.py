# Check whether: "name" and "salary" exists in dictionary

student = {
    "name": "Alice",
    "age": 21,
    "course": "Python"
}

if student.get("name"):
    print(f"\"name\" exists in the dictionary")
else:
    print(f"\"name\" does not exist in the dictionary")

if student.get("salary"):
    print(f"\"salary\" exists in the dictionary")
else:
    print(f"\"salary\" does not exist in the dictionary")
