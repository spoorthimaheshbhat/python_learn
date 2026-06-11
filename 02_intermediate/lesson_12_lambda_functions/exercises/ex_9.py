# Given list

students = [
    ("Alice", 90),
    ("Bob", 75),
    ("Charlie", 85),
    ("David", 95)
]

# sorts in descending order of marks
sorted_list_student = sorted(students, key = lambda x: x[1], reverse = True)
print(sorted_list_student)