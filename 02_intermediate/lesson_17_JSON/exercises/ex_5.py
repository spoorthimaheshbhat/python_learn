import json


def wrap_func(func):
    def inner():
        print("Initiated execution...")

        result = func()

        print("\nExecution Complete.")

        return result

    return inner()

@wrap_func
def post_info():
    with open("student.json", "r+") as f:
        student_data = json.load(f)

        for student in student_data:
            if student["course"] == "Python":
                student["city"] = "NY"

            else:
                student["city"] = "LA"

        f.seek(0)

        json.dump(
            student_data,
            f,
            indent = 4
        )

        f.truncate()

