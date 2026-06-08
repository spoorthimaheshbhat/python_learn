def update_transactions(amount):
    try:
        with open('transactions.txt', 'a') as file:
            file.write("," + str(amount))
            return True

    except FileNotFoundError:
        print("File 'transactions.txt' was not found.")
        return False

def get_transactions():
    try:
        transaction = int(input("Enter transaction amount: "))
        return transaction

    except ValueError:
        print("Invalid input. Enter transaction amount as integer.")
        return None

def done_validation():
    while True:
        done = input("Do you want to continue? (y/n): ")
        if done == "y":
            return True
        elif done == "n":
            print("Closing Transactions. Thank you!")
            return False
        else:
            print("Invalid input. Enter y/n")


is_done = True
while is_done:
    transaction_amount = get_transactions()
    if transaction_amount is not None:
        update_transactions(transaction_amount)
        is_done = done_validation()











