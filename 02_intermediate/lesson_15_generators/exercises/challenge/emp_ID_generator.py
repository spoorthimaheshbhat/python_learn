def generate_empid(emp_list):

    # determines the latest number of new employee added, stored as string for ID
    last_string = str(len(emp_list))

    if len(emp_list) < 10:
        yield "EMP00" + last_string

    elif 100 > len(emp_list) >= 10:
        yield "EMP0" + last_string

    else:
        yield "EMP" + last_string


def get_new_emp():
    new_emp = []
    while True:
        new_emp += [input("Enter new employee name: ").lower()]
        yield new_emp

def main():
    new_employee_record = {}
    new_employee_list = []
    while True:
        request = input("Do you want to add new employee? (y/n): ").lower()
        if request == "y":
            new_employee = get_new_emp()
            new_employee_list += next(new_employee)

            new_empid = generate_empid(new_employee_list)
            new_employee_record[new_employee_list[-1].title()] = next(new_empid)

            print(new_employee_record)
            # print(new_employee_list)

        elif request == "n":
            print("Closing Employee ID Generator. Thank you!")
            break

        else:
            print("Invalid Request")

if __name__ == "__main__":
    main()



