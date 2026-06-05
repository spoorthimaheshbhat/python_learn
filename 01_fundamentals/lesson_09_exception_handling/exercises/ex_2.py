def enter_input():
    while True:
        try:
            number_1 = int(input("Enter number: "))
            number_2 = int(input("Enter another number: "))
            return number_1, number_2

        except ValueError:
            print("Please enter valid integers.")

def divide(numerator, denominator):
    try:
        return numerator / denominator

    except ZeroDivisionError:
        print("Cannot divide by zero!")

while True:
    num1, num2 = enter_input()
    result = divide(num1, num2)
    if result is not None:
        print(f"{num1} / {num2} = {result}")
        break

