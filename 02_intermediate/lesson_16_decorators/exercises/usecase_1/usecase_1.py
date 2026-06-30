# decorator

def report_logger(func):

    def inner(user, num, val1, val2):
        print("\nGenerating Attendance Report...\n")

        func(user, num, val1, val2, )

        print("\nOpen \"report.txt\" for attendance report.")

    return inner

# report generator function

@report_logger
def get_report(name, emp_id, in_val, out_val):

    report = open("report.txt", "a")
    report.write(f"NAME: {name}\nEMPLOYEE NUMBER: {emp_id}\n")
    if in_val:
        report.write("Punch In successful\n")
        if out_val:
            report.write("Punch Out successful\n\n")

        else:
            report.write("Punch Out Missed\n\n")

    else:
        report.write("Punch In missed\n\n")

    report.close()


def get_employee_data():
    while True:
        try:
            e_name = input("Enter your name: ").title()

            e_num = int(input("Enter your employee number: "))

            return e_name, e_num

        except ValueError:
            print("\nInvalid Input. Try again...\n")

def punch_attendance():

    punch_in = input("Click '+' to Punch In: ")
    out_value = False

    if punch_in == "+":
        print("Punched In successfully.\n")
        in_value = True

        punch_out = input("Click '-' to Punch Out: ")
        if punch_out == "-":
            print("Punched out successfully.\n")
            out_value = True

        else:
            print("Invalid Input.")
            out_value = False

    else:
        print("Invalid Input")
        in_value = False

    return in_value, out_value

def main():

    employee_name, employee_num = get_employee_data()
    punch_in_val, punch_out_val = punch_attendance()
    get_report(employee_name, employee_num, punch_in_val,punch_out_val)

if __name__ == "__main__":
    main()
