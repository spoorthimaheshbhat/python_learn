# enhanced version to visualize real cases
# Use Case 1 - Employee Management System (OOP)
import json
from json import JSONDecodeError

def complete_status(func):

    def inner():
        print("\nExecuting Request...\n")

        func()

        print("\nRequest Completed!\n")

    return inner

class Employee:

    def __init__(self, name, emp_id, department, status):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.status = status

    def to_dict(self):
        employee = {}
        employee["employee_name"] = self.name
        employee["employee_ID"] = self.emp_id
        employee["department"] = self.department
        employee["status"] = self.status

        return employee

@complete_status
def create_employee_record():
    emp_name = input("Enter employee name: ").title()
    e_id = input("Enter employee ID: ").upper()
    emp_dept = input("Enter employee department: ").upper()
    emp_status = input("Enter employee status (Active/Inactive): ").upper()

    employee_record = Employee(emp_name, e_id, emp_dept, emp_status)

    with open("employee_records.json", "a+") as file:
        file.seek(0)
        try:
            employees = json.load(file)
        except JSONDecodeError:
            employees = []

        employees.append(employee_record.to_dict())

        file.seek(0)
        file.truncate()
        json.dump(employees, file, indent=4)

@complete_status
def view_all_employees():
    try:
        with open("employee_records.json", "r") as file:
            file.seek(0)
            employees = json.load(file)
            for emp in employees:
                print(f"Name: {emp['employee_name']}\n"
                      f"ID: {emp['employee_ID']}\n"
                      f"Department: {emp['department']}\n"
                      f"Status: {emp['status']}\n\n")

    except JSONDecodeError:
        print("No Records Found. Check 'employee_records.json' file.")

    except FileNotFoundError:
        print("No Records Found. 'employee_records.json' file does not exist.")

@complete_status
def view_active_employees():
    try:
        with open("employee_records.json", "r") as file:
            file.seek(0)
            employees = json.load(file)

            found = False
            for emp in employees:
                if emp["status"] == "ACTIVE":
                    found = True
                    print(f"Name: {emp['employee_name']}\n"
                          f"ID: {emp['employee_ID']}\n"
                          f"Department: {emp['department']}\n"
                          f"Status: {emp['status']}\n\n")

            if not found:
                print("No Records Found.")

    except JSONDecodeError:
        print("No Records Found. Check 'employee_records.json' file.")

    except FileNotFoundError:
        print("No Records Found. 'employee_records.json' file does not exist.")

@complete_status
def view_inactive_employees():
    try:
        with open("employee_records.json", "r") as file:
            file.seek(0)
            employees = json.load(file)

            found = False
            for emp in employees:
                if emp["status"] == "INACTIVE":
                    found = True
                    print(f"Name: {emp['employee_name']}\n"
                          f"ID: {emp['employee_ID']}\n"
                          f"Department: {emp['department']}\n"
                          f"Status: {emp['status']}\n\n")

            if not found:
                print("No Records Found.")

    except JSONDecodeError:
        print("No Records Found. Check 'employee_records.json' file.")

    except FileNotFoundError:
        print("No Records Found. 'employee_records.json' file does not exist.")

@complete_status
def search_by_id():
    search_id = input("Enter employee ID: ").upper()

    try:
        with open("employee_records.json", "r") as file:
            file.seek(0)
            employees = json.load(file)

            found = False
            for emp in employees:
                if emp["employee_ID"] == search_id:
                    print("Employee Found!\n\n")
                    found = True

                    print(f"Name: {emp['employee_name']}\n"
                          f"ID: {emp['employee_ID']}\n"
                          f"Department: {emp['department']}\n"
                          f"Status: {emp['status']}\n\n")
                    break

            if not found:
                print("No Records Found. Employee Does Not Exist.")

    except JSONDecodeError:
        print("No Records Found. Check 'employee_records.json' file.")

    except FileNotFoundError:
        print("No Records Found. 'employee_records.json' file does not exist.")

def main():
    while True:
        try:
            print("Request List:\n"
                  "1. Create a new employee record\n"
                  "2. View all employee records\n"
                  "3. Search employee records by employee ID\n"
                  "4. View all active employees\n"
                  "5. View all inactive employees\n"
                  "6. Exit application\n")

            request = int(input("Enter your request number (1-6): "))

            if request == 1:
                create_employee_record()
                continue

            elif request == 2:
                view_all_employees()
                continue

            elif request == 3:
                search_by_id()
                continue

            elif request == 4:
                view_active_employees()
                continue

            elif request == 5:
                view_inactive_employees()
                continue

            elif request == 6:
                print("Thank you. See you again!")
                break

            else:
                print("Invalid Input. Try Again.")

        except ValueError:
            print("Invalid Input. Try Again.")

if __name__ == "__main__":
    main()
