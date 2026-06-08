def get_all_logs():
    try:
        with open("login_log.txt", "r") as file:
            logs = file.read().splitlines()
            return logs

    except FileNotFoundError:
        print("Logs file not found")
        return []

def get_fail_logs(all_logs):
    fail_logs = [log for log in all_logs if "FAILED" in log]
    return fail_logs

def get_success_logs(all_logs):
    success_logs = [log for log in all_logs if "SUCCESS" in log]
    return success_logs

def request_logs(all_logs_list):
    while True:
        log_type = input("Please enter log type (Failed/Success): ").lower()
        if log_type == "failed":
            print(f"Log type failed includes:\n\n{get_fail_logs(all_logs_list)}")
            break

        elif log_type == "success":
            print(f"Log type success includes:\n\n{get_success_logs(all_logs_list)}")
            break

        else:
            print(f"Log type incorrect\n")

logs_list = get_all_logs()
if logs_list:
    request_logs(logs_list)


