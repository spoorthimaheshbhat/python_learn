# decorator

def audit_transaction(func):

    def inner(c, d):
        print("Transaction Audit Started...\n")
        func(c, d)
        print("Transaction Audit Completed\n")
        print("Open 'transactions_log.txt' to view transactions.")

    return inner

@audit_transaction
def transactions_report(cred, deb):
    transactions_log = open("transactions_log.txt", "a")
    transactions_log.write("Current Transactions:\n")
    if cred:
        for c_amount in cred:
            transactions_log.write(f"Credited: {c_amount}\n")

    if deb:
        for d_amount  in deb:
            transactions_log.write(f"Debited: {d_amount}\n")


def get_transactions():
    credit_amt = []
    debit_amt = []
    while True:
        try:
            user_request = int(input("1. Credit Amount Entry\n"
                                 "2. Debit Amount Entry\n"
                                 "3. Exit\n"
                                 "Enter your request number: "))

            if user_request == 1:
                c_amt = float(input("Enter Credit Amount: "))
                credit_amt.append(round(c_amt, 2))
            elif user_request == 2:
                d_amt = float(input("Enter Debit Amount: "))
                debit_amt.append(round(d_amt, 2))
            elif user_request == 3:
                print("Closing Transactions. Thank you!\n")
                return  credit_amt, debit_amt
            else:
                print("\nInvalid Input. Try again...\n")

        except ValueError:
            print("Invalid Input. Try again.")

def main():
    credit_transaction, debit_transaction = get_transactions()
    transactions_report(credit_transaction,debit_transaction)

if __name__ == "__main__":
    main()

