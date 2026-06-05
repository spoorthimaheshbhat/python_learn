def enter_integer():
    while True:
        try:
            integer = int(input("Enter an integer: "))
            return integer

        except ValueError:
            print("Invalid input.")

value = enter_integer()
print(f"{value}"
      f"\nAccepted")