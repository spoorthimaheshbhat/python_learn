def safe_add():
    try:
        a = int(input("Enter a number: "))
        b = int(input("Enter another number: "))
        return a + b

    except ValueError:
        print("Invalid input.")

result = safe_add()
if result is not None:
    print(result)

