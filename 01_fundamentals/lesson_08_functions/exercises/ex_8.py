def print_table(number, x):
    return number * x


enter = int(input("Enter a number: "))
for i in range(1, 11):
    table_val = print_table(enter,i)
    print(f"{enter} x {i} = {table_val}")