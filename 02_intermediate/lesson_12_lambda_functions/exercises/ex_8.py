# given list

products = [
    ("Laptop", 50000),
    ("Mouse", 500),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]

# Creates a new, sorted list without changing the original one.
sorted_products = sorted(products, key=lambda x: x[1])
print(sorted_products)
