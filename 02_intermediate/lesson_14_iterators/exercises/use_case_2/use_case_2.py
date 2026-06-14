# Use Case 2 — Transaction Processor
# given that transactions are recorded as positive integer for "Processed" negative integer for "Failed"
# .csv file converted to transactions.txt file contains all transaction separated by commas

def get_transactions():
    try:
        with open("transactions.txt", "r") as file:
            transaction_records = file.read().split(",")
            return transaction_records

    except FileNotFoundError:
        print("transactions.txt file does not exist")

def get_each_record(records):
    record = iter(records)
    while True:
        try:
            rec = float(next(record))
            if rec >=  0:
                print(f"Processed: {rec}")
            else:
                print(f"Failed: {rec * -1}")  # show without negative symbol (amount deducted only)

        except StopIteration:
            print("All transactions displayed.")
            return

        except ValueError:
            print("Invalid transaction")
            continue

def main():
    transaction_records = get_transactions()
    get_each_record(transaction_records)

if __name__ == "__main__":
    main()




