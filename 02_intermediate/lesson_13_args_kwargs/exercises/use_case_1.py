def checkout(customer, *items):

    print(f"Customer: {customer}")

    print(f"\nItems Purchased:")
    for item in items:
        print(item)

checkout(
    "Alice",
    "Laptop",
    "Mouse",
    "Keyboard"
)