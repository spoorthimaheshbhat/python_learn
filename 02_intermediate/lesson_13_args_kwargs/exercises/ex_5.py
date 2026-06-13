def employee(**kwargs):

    for emp_id, summary in kwargs.items():

        print(f"{emp_id}"
              f"\nName: {summary[0]}"
              f"\nDepartment: {summary[1]}"
              f"\nSalary: {summary[2]}\n")

employee(
    EMP101 = ("John", "IT", 50000),
    EMP102 = ("Neil", "IT", 60000),
    EMP103 = ("Mary", "Fin", 18000),
    EMP104 = ("Ken", "Networks", 120000),
    EMP105 = ("Jane", "IT", 150000),
    EMP106 = ("Anna", "Fin", 20000),
    EMP107 = ("Jenna", "Design", 8000)

)



