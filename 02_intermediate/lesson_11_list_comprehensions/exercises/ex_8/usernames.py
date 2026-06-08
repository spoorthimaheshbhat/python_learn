def add_username():
    username = input("Enter your username: ")
    try:
        with open("usernames.txt", "a") as f:
            f.write("," + username)

    except FileNotFoundError:
        print("Usernames file not found")

add_username()
