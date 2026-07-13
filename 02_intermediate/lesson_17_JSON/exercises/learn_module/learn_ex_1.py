import json

def update_process(func):

    def inner(*args, **kwargs):
        print(f"Updating record...")

        result = func(*args, **kwargs)

        print("\nRecord Updated Successfully.")

        return result

    return inner()


@update_process
def json_update():
    with open("employee.json", "r+") as file:
        employee = json.load(file)

        for emp in employee:
            if emp["employee_number"] == 12300910:
                emp["employee_dept"] = "Fin_11"

            if emp["employee_number"] == 12300912:
                emp["employee_dept"] = "SWE_07"

            if emp["employee_number"] == 12300910:
                emp["employee_dept"] = "HR_05"

        file.seek(0)

        json.dump(
            employee,
            file,
            indent = 4
        )

        file.truncate()

