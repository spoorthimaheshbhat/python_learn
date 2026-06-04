#Calculator using functions

def input_nums():
    num1 = int(input("Enter first numbers: "))
    num2 = int(input("Enter second numbers: "))
    return num1, num2

x, y = input_nums()

def calculator(a, b, act):
    if act == "add":
        return a + b
    elif act == "subtract":
        return a - b
    elif act == "multiply":
        return a * b
    elif act == "divide":
        if b == 0:
            print("Cannot perform division.")
            exit()
        else:
            return a / b
    else:
        print("Invalid action")
        exit()


action = input("Enter action (add, subtract, multipy, divide): ").lower()

result = calculator(x, y, action)
print(f"Result: {result}")


