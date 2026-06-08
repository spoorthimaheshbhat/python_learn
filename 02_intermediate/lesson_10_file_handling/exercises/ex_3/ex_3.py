with open("log.txt", "w") as file:
    file.write("Program Execution Log:")

def execution_log(run_status):
    with open("log.txt", "a") as log_file:
        log_file.write(f"\n{run_status}")

def action(file_name):
    status = "Read fail"
    try:
        with open(file_name, "r") as read_file:
            read_file.read()
            # print(addition)
            status = "Read Success"
            return status

    except FileNotFoundError:
        return status

run_times = 10
while run_times != 0:
    status_run = action("log.txt")
    run_times -= 1
    execution_log(status_run)

print("Execution log fully updated!")

