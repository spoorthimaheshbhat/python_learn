def get_individual_records():

    with open("attendance_records.txt", "r") as file:

        # attendance_records.txt stores employee data as name, status in each line
        for line in file:
            attendance_stream = line.strip().title() # clean string and format

            # split the line at ',' store name and status separately
            name, status = attendance_stream.split(",")

            # returns a tuple with (name, status)
            yield name, status

def get_record(records):
    while True:
        try:
            next_rec = input("Do you want to view employee record? (Y/N): ").lower()
            if next_rec == "y":
                print(next(records))

            elif next_rec == "n":
                print("Thank you! Exiting records view.")
                break

            else:
                print("Invalid Input! Enter Y or N: ")

        except StopIteration:
            print("End of Records! Thank you.")
            break


def main():
    individual_record = get_individual_records()
    get_record(individual_record)

if __name__ == "__main__":
    main()



