import json
from json import JSONDecodeError


class Student:

    def __init__(self, name, marks, result):
        self.name = name
        self.marks = marks
        self.result = result

    def get_results(self):
        print(f"{self.name} has scored {self.marks}: Result -> {self.result}")


def main():
    student_id = input("Enter student ID: ").upper()
    try:
        with open("student_records.json", "r") as file:
            student_record = json.load(file)
            found = False
            for student in student_record:
                if student["student_ID"] == student_id:
                    results = Student(student["student_name"], student["marks"], student["result"])
                    results.get_results()
                    found = True
                    break

            if not found:
                print("No Records Found. Student ID Does Not Exist.")

    except (JSONDecodeError, FileNotFoundError):
        print("No Records Found. Internal Error.")

if __name__ == "__main__":
    main()


