def log_audit(any_function):
    # Use *args and **kwargs so the decorator can accept ANY combination of arguments
    def inner(*args, **kwargs):
        result = any_function(*args, **kwargs)

        # Filters out unfavorable results (None and False)
        if result is not None:
            print("\nLog Updated Successfully")
        return result  # Must return the result back to main()
    return inner

def get_users():
    dict_user_data = {}
    try:
        with open("registartion_log.txt", 'r') as reg_file:
            for line in reg_file:
                clean_line = line.strip()
                if "," in clean_line:
                    username, password = clean_line.split(",", 1)
                    dict_user_data[username.strip()] = password.strip()
    except FileNotFoundError:
        pass

    return dict_user_data


@log_audit
def register_attempt(user_dict):
    username = input("Enter your username to register: ").lower()

    if username not in user_dict:
        password = input("Enter a password of your choice: ")
        with open("registartion_log.txt", 'a') as reg_file:
            reg_file.write(f"{username},{password}\n")
            print("Registration complete")

        # Keep our in-memory dictionary up to date!
        user_dict[username] = password

        with open("log.txt", "a") as log_file:
            log_file.write("Registration,Success\n")
            return True
    else:
        print("Registration unsuccessful. User already exists")
        return None


@log_audit
def login_attempt(user_dictionary):
    user_name = input("Enter your username: ")

    if user_name in user_dictionary.keys():
        pass_word = input("Enter your password: ")
        log_file = open("log.txt", "a")
        if user_dictionary[user_name] == pass_word:

            log_file.write("Login,Success\n")
            print("\nUser Logged In.")
            log_file.close()
            return True

        else:
            print("Login unsuccessful. Incorrect Password")
            log_file.write("Login,Fail\n")
            log_file.close()
            return False

    else:
        print("User does not exist.")
        return None

@log_audit
def logout_attempt(file):
    with open(file, "a") as out_file:
        out_file.write("Logout,Success\n")
        return True


def main():
    users_data = get_users()
    while True:
        login = login_attempt(users_data)
        if login is None:
            registration = register_attempt(users_data)
            if registration:
                print("\nRedirecting to Login...\n")

        elif login:
            while True:
                user_request = input("Do you wish to logout? y/n: ").lower()
                if user_request == "y":
                    logout_attempt("log.txt")
                    print("\nUser Logged out.")
                    return None

                elif user_request == "n":
                    print("Enjoy your stay.")
                    return None

                else:
                    print("Invalid input.")
        else:
            return None


if __name__ == "__main__":
    main()

