def get_positive_integer():
    while True:
        try:
            input_value = int(input("Enter a number: "))
            if input_value <= 0:
                print("Must be positive.")
            else:
                return input_value
        except ValueError:
            print("Invalid input.")

integer = get_positive_integer()
print(f"Your positive number is: {integer}")
