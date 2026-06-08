def create_credentials_dict():
    credentials_dict = {}
    try:
        with open("credentials.txt", "r") as file:
            for line in file:
                cleaned_line = line.strip()

                if not cleaned_line:
                    continue

                username, password = cleaned_line.split(",")

                credentials_dict[username] = password

        return credentials_dict

    except FileNotFoundError:
        print("The file was not found.")

credentials_list = create_credentials_dict()
if credentials_list:
    print([username for username in credentials_list.keys()])
else:
    print("Usernames not found.")