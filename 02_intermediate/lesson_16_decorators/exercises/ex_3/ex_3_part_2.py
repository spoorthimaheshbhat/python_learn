def audit_log(func):

    def inner(users):

        func(users)

        print(f"\nAudit Entry Created")

    return inner

@audit_log
def login_log(dict_usernames):
    count = 1
    login_file = open("login_audit_log.txt", "a")
    while True:
        user_name = input("Enter username: ").lower()

        if user_name in dict_usernames.keys():
            while True:
                pass_word = input("Enter password: ")

                if dict_usernames[user_name] == pass_word:
                    print(f"\nLogin Successful!")

                    # create an entry in the login audit log
                    login_file.write(f"{user_name},SUCCESS\n")
                    return

                elif count < 3:
                    print("Invalid password, Try Again.")
                    count += 1

                else:
                    print("Login Attempt Failed.")
                    login_file.write(f"{user_name},FAIL\n")

                    return

        else:
            print("Username does not exist. Register to login.")
            login_file.write(f"{user_name},FAIL\n")
            return

    login_file.close()

def get_users():
    dict_user_data ={}
    try:
        with open("registartion_log.txt", 'r') as reg_file:
            for line in reg_file:
                username = line.split(",")[0].strip("\n")
                password = line.split(",")[1].strip("\n")
                dict_user_data[username] = password

    except FileNotFoundError:
        pass

    return dict_user_data

def main():
    dict_users = get_users()
    login_log(dict_users)

if __name__ == "__main__":
    main()
