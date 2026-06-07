def input_credentials():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    return username, password

def create_credentials_dict():
    credentials_dict = {}
    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                lines = line.strip()

                if not lines:
                    continue

                username, password = lines.split(",")

                username = username.strip()
                password = password.strip()

                credentials_dict[username] = password

            return credentials_dict

    except FileNotFoundError:
        print("Credentials file was not found")
        return credentials_dict

def check_credentials(creds_dict, username, password):
    if username in creds_dict and creds_dict[username] == password:
        return True
    else:
        return False


credentials = create_credentials_dict()

attempt = 0
while attempt < 3:
    user_name, pass_word = input_credentials()
    if check_credentials(credentials, user_name, pass_word):
        print("Login successful!")
        try:
            with open("login_log.txt", "a") as file:
                file.write(f"SUCCESS: {user_name}\n")

        except FileNotFoundError:
            print("Log file not found.")
        break

    else:
        print("Login failed!")
        try:
            with open("login_log.txt", "a") as file:
                file.write(f"FAILED: {user_name}\n")

        except FileNotFoundError:
            print("Log file not found.")

        attempt += 1

if attempt == 3:
    print("Account locked")

