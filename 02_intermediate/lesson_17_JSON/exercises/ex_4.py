import json


def wrap_info(func):
    def inner():
        print("Reading 'student.json' - ")

        res = func()

        print("\nReading Complete.")

        return res

    return inner()

@wrap_info
def get_info():
    with open("student.json", "r") as file:
        student_info = json.load(file)

        print(student_info)
        for student in student_info:
            print(f"{student["name"]} - {student["marks"]}")
