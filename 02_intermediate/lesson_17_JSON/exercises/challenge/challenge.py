# Employee Database (JSON)
#
# Build a simple employee management system.

import json
from json import JSONDecodeError

def add_employee():
    with open("employee.json", "a+") as file:
        add_dict = {}
        file.seek(0)

        try:
            employee = json.load(file)
        except JSONDecodeError:
            employee = []

        e_name = input("Enter Employee Name: ").title()
        add_dict["employee_name"] = e_name
        e_id = int(input("Enter Employee ID: "))
        add_dict["employee_ID"] = e_id
        e_dept = input("Enter Employee Department: ").upper()
        add_dict["employee_department"] = e_dept
        e_type = int(input("Enter Employee Type Code(11 - Part Time/1- Full Time/21 - Contract): "))
        add_dict["employee_type"] = e_type
        e_status = input("Enter Employee Status (Active/Inactive): ").title()
        add_dict["employee_status"] = e_status

        employee.append(add_dict)

        file.seek(0)
        file.truncate()
        json.dump(employee, file, indent=4)

        print("Employee added to record.")


def get_employee_names():
    with open("employee.json", "a+") as file:
        file.seek(0)
        try:
            emp_details = json.load(file)

            for emp in emp_details:
                print(f"{emp["employee_name"]}\n")

        except JSONDecodeError:
            print("\nNo Records Found\n")

def get_active_employees():
    with open("employee.json", "a+") as file:
        file.seek(0)
        try:
            employee_list = json.load(file)
            active_employees = [emp for emp in employee_list if emp["employee_status"].lower() == "active"]
            if active_employees:
                print(f"\nNumber of active employee records: {len(active_employees)}\n")

            else:
                print(f"\nNumber of active employee records: {0}\n")

        except JSONDecodeError:
            print(f"\nNumber of active employee records: {0}\n")

def get_inactive_employees():
    with open("employee.json", "a+") as file:
        file.seek(0)
        try:
            employee_list = json.load(file)
            active_employees = [emp for emp in employee_list if emp["employee_status"].lower() == "inactive"]
            if active_employees:
                print(f"\nNumber of inactive employee records: {len(active_employees)}\n")

            else:
                print(f"\nNumber of inactive employee records: {0}\n")

        except JSONDecodeError:
            print(f"\nNumber of inactive employee records: {0}\n")

def search_by_id():
    try:
        search_id = int(input("Enter search id: "))

        with open("employee.json", "r") as file:
            file.seek(0)
            emp_details = json.load(file)

            found = False
            for employee in emp_details:
                if employee["employee_ID"] == search_id:
                    print("\nEmployee Found:")
                    print(f"ID: {search_id}")

                    for key, value in employee.items():
                        # Format keys like 'employee_name' to 'Employee Name'
                        clean_key = key.replace("_", " ").title()
                        print(f"{clean_key}: {value}\n")

                    found = True
                    break

            if not found:
                print("\nEmployee ID not found.\n")


    except (JSONDecodeError, FileNotFoundError):
        print("\nNo Records Found\n")

    except ValueError:
        print("Invalid Input.")

# Create a function to get user request
def get_user_request():

    while True:

        print("Request Items:\n"
              "1. Add a new employee.\n"
              "2. View all employees.\n"
              "3. Display active employee(s) count.\n"
              "4. Display inactive employee(s) count.\n"
              "5. Search employee by user ID.\n"
              "6. Exit\n")
        try:
            request = int(input("Enter your request number: "))

            if request == 1:
                add_employee()

            elif request == 2:
                get_employee_names()

            elif request == 3:
                get_active_employees()

            elif request == 4:
                get_inactive_employees()

            elif request == 5:
                search_by_id()

            elif request == 6:
                print("\nExiting application. Thank you!")
                return None

            else:
                print("Invalid Input! Try again")

        except ValueError:
            print("Invalid Input.")



def main():
    get_user_request()

if __name__ == "__main__":
    main()