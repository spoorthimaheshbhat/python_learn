# Attendance Stream Reader

# .csv converted to .txt file contains attendance records with format name,status
def read_records():
    with open("employee_records.txt", "r") as file:
        contents = file.read().lower().split(",")
        records = list(zip(contents[0::2],contents[1::2]))
        return records

# print(read_records())  # - behaviour checkpoint

def get_individual_record(given_records):
    record = iter(given_records)

    while True:
        try:
            employee = iter(next(record))

            print(f"{next(employee).title()}, {next(employee).title()}\n")

        except StopIteration:
            print("All records displayed")
            return

employee_records = read_records()
get_individual_record(employee_records)





