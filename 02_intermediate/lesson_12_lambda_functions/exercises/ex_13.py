# given
transactions = [
    ("TXN001", 500),
    ("TXN002", 2500),
    ("TXN003", 150),
    ("TXN004", 4000),
    ("TXN005", 750)
]

# A list of transactions above 1000 using filter().
def high_transactions(transactions_list):
    return list(
        filter(
            lambda x: x[1] > 1000, transactions_list
        )
    )


# Sort them by amount descending using a lambda.
def sort_transactions(list_transactions):
    return sorted(
        list_transactions, key = lambda amt: amt[1], reverse =  True
    )

# Print the final result.
transaction_high = high_transactions(transactions)
print(f"Transactions above 1000 are: {transaction_high}"
      f"\nTransactions high-to-low: {sort_transactions(transaction_high)}")