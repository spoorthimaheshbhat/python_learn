def read_usernames():
    try:
        with open("usernames.txt", "r") as file:
            usernames = file.read().split(",")
            return usernames

    except FileNotFoundError:
        print("Usernames file not found")

def long_usernames(user_names):
    return [user for user in user_names if len(user) > 5]

usernames_list = read_usernames()
# null_list = []
long_usernames_list = long_usernames(usernames_list)
if long_usernames_list:
    print(f"All usernames with more than 5 characters are:\n\n{long_usernames_list}")
else:
    print("Usernames file empty")