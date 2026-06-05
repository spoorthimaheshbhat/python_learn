def enter_num():
    while True:
        try:
            user_input = int(input("Please enter a number: "))
            return user_input

        except ValueError:
            print("Please enter a valid integer.")

print(enter_num())