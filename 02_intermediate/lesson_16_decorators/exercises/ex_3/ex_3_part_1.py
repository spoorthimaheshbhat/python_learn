def registration_log(func):

    def inner(reg):

        print("\nRegistration Log Updated!")

        func(reg)

    return inner

def login_register():
    count = 0
    while True:
        user_name = input("Enter User Name: ").lower()
        with open("registartion_log.txt", "a+") as file:

            #Move read pointer to the beginning of the file
            file.seek(0)

            # Read lines and strip out passwords to isolate just usernames
            # file stores data as "username,password", so we split by ','
            contents = [line.split(',')[0].lower() for line in file.read().splitlines()]

            if user_name not in contents:
                pass_word = input("Enter password: ")
                file.write(user_name + "," + pass_word + "\n")
                return user_name

            else:
                print("Username already exists!")
                count +=1
                if count == 3:
                    return None

@registration_log
def login_attempt(register):
    if register is not None:
        print(f"User '{register}' Created!")
    else:
        print("Attempt limit crossed")


def main():
    registration = login_register()
    login_attempt(registration)

if __name__ == "__main__":
    main()
