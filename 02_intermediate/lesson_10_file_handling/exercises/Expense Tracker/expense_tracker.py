with open("expenses.txt", "w") as file:
    file.write("This is an expense tracker\n")

def get_expenses():
    while True:
        try:
            expense_in = int(input("\nEnter expense amount: "))
            if expense_in >= 0:
                return expense_in
            else:
                print("\nInvalid Input! Please enter positive integer\n")

        except ValueError:
            print("\nInvalid Input! Please enter an integer\n")

def add_expenses(add_amount):
    try:
        with open("expenses.txt", "a") as given_file:
            given_file.write(str(add_amount) + "\n")
            print("\nExpense added to file\n")

    except FileNotFoundError:
        print("\nExpenses file unavailable.\n")

    return None


def show_total():
    try:
        with open("expenses.txt", "r") as given_file:
            expenses_content = given_file.read().splitlines()
            total_expense = 0
            for expense in expenses_content[1:]:
                total_expense = total_expense + int(expense)

            return total_expense

    except FileNotFoundError:
        print("\nExpenses file unavailable.\n")

    except ValueError:
        print("\nValue is not an Integer\n")

def get_request():
    while True:
        request = input("Please enter your request (add, show total, or exit): ").lower()
        if request == "exit":
            print("\nThank you for using expense tracker\n")
            break

        elif request == "add":
            amount = get_expenses()
            add_expenses(amount)

        elif request == "show total":
            print(f"\nTotal expense: {show_total()}\n")

        else:
            print("\nInvalid Input! Please enter either 'add', 'show total' or 'exit'\n")


get_request()