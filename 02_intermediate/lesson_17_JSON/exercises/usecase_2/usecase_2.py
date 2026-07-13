# Test Execution Report
#
# Build a QA test report system.

import json
from json import JSONDecodeError

# decorator function
def wrap_report_generation(func):
    def inner(*args):

        func(*args)
        print("Test report updated...open 'test_report.json' to view report.")

    return inner

# get test execution data from user,
# since no test automation module exists currently to fetch execution data directly.
def get_execution_data():
    test_data = {}
    while True:
        try:
            test_id = input("Enter the test ID: ").upper()
            test_data["test_id"] = test_id

            test_feature = input("Enter the test feature: ").title()
            test_data["test_feature"] = test_feature

            test_status = input("Enter the test status (Pass/Fail/Deffered): ").upper()
            test_data["test_status"] = test_status

            test_time = int(input("Enter test execution time in seconds: "))
            test_data["test_execution_time"] = test_time

            tester = input("Enter tester name: ").title()
            test_data["tester"] = tester

            break

        except ValueError:
            print("Invalid input. Try Again!")

    return test_data

@wrap_report_generation
def report_generator(execution_result):
    # when test_report.json does not exist, a+ mode will create it
    with open("test_report.json", "a+") as file:
        file.seek(0)
        try:
            test_report = json.load(file)
        except JSONDecodeError:
            test_report = []

        test_report.append(execution_result)

        file.seek(0)
        file.truncate()
        json.dump(test_report, file, indent=4)

def main():
    execution = get_execution_data()
    report_generator(execution)

if __name__ == "__main__":
    main()