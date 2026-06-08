def get_transactions_list():
    try:
        with open("transactions.txt", "r") as file:
            transactions = file.read().split(",")
            return [int(amount) for amount in transactions if amount != ""]

    except FileNotFoundError:
        print("No transactions file found.")
        return None

    except ValueError:
        print("List contains non-numeric values.")
        return None

def check_credits(transactions_list):
    return [credit for credit in transactions_list if credit > 0]

def check_debits(transactions_list):
    return [debit for debit in transactions_list if debit < 0]

def get_request():
    while True:
        try:
            request = int(input("1. Check Credits"
                        "\n2. Check Debits"
                        "\n3. Exit"
                        "\nPlease enter your request (1, 2, or 3): "))
            if request == 1:
                print(f"{check_credits(get_transactions_list())}\n")

            elif request == 2:
                print(f"{check_debits(get_transactions_list())}\n")

            elif request == 3:
                print("Thank you! Have a good day!")
                return None

            else:
                print("Invalid input. Enter 1, 2, or 3.\n")

        except ValueError:
            print("Invalid input! Try again.\n")


get_request()


