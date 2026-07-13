# Employee Database (JSON)
#
# Build a simple employee management system.

import json
from json import JSONDecodeError


# Create a function to get user request
def get_user_request():
    file = open("employee.json", "a+")

    while True:

        print("Request Items:\n"
              "1. Add a new employee.\n"
              "2. Read all employees.\n"
              "3. Display employee count.\n"
              "4. Exit\n")
        try:
            request = int(input("Enter your request number: "))

            if request == 1:

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



            elif request == 2:
                file.seek(0)
                try:
                    emp_details = json.load(file)

                    for emp in emp_details:
                        print(f"\n{emp}\n")
                except JSONDecodeError:
                    print("\nNo Records Found\n")

            elif request == 3:
                file.seek(0)
                try:
                    employee_list = json.load(file)
                    print(f"\nNumber of employee records: {len(employee_list)}\n")

                except JSONDecodeError:
                    print(f"\nNumber of employee records: {0}\n")

            elif request == 4:
                print("\nExiting application. Thank you!")
                file.close()
                return None

            else:
                print("Invalid Input! Try again")

        except ValueError:
            print("Invalid Input.")



def main():
    get_user_request()

if __name__ == "__main__":
    main()