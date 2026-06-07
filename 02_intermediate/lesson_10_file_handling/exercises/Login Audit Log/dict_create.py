credentials_dict = {}

try:
    with open("../../user_login/credentials.txt", "r") as file:
        for line in file:
            # Strip removes hidden newlines (\n), split(",") separates user and pass
            cleaned_line = line.strip()

            # Skip empty lines if there are any
            if not cleaned_line:
                continue

            username, password = cleaned_line.split(",")

            # Assign to dictionary: {username: password}
            credentials_dict[username] = password

    print("Resulting Dictionary:")
    print(credentials_dict)

except FileNotFoundError:
    print("The file was not found.")