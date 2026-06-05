def input_nums():
    while True:
        try:
            num1 = int(input("Enter first numbers: "))
            num2 = int(input("Enter second numbers: "))
            return num1, num2

        except ValueError:
            print("Invalid input. Please enter integer values only.")

def calculator(a, b):
    try:
        act = input("Enter action (add, subtract, multiply, divide): ").lower()
        if act == "add":
            return a + b

        elif act == "subtract":
            return a - b

        elif act == "multiply":
            return a * b

        elif act == "divide":
            return a / b

        else:
            print("Invalid action")

    except ZeroDivisionError:
        print("Cannot divide by zero.")


x,y = input_nums()
result = calculator(x, y)
if result is not None:
    print(f"Result is: {result}")
