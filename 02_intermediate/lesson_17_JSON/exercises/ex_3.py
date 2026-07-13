import json
from unittest import result


def wrap(func):
    def inner():
        print("Writing data into 'student.json'")

        results = func()

        print("Write Complete.")

        return results

    return inner()


@wrap
def put_details():
    student_details = [{
        "name":"John",
        "course":"Python",
        "marks":95
        },
        {
            "name": "Jinny",
            "course": "SQL",
            "marks": 85
        },
        {
            "name": "Joslynn",
            "course": "Playwright",
            "marks": 96.8
        }
    ]

    with open("student.json", "w+") as json_file:
        json_file.seek(0)
        json.dump(
            student_details,
            json_file,
            indent = 4
        )
        json_file.truncate()

