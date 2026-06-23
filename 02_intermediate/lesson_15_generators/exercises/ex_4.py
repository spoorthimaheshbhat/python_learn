def get_evens(top):
    for x in range(2, top + 1, 2):
        yield x


try:
    top_value = int(input("Enter top value to count even numbers: "))
    if top_value > 0:
        # Create the generator instance once
        even_generator = get_evens(top_value)

        # Loop through the generator directly
        for n in even_generator:
            print(n)

    else:
        print("Invalid Input")

except ValueError:
    print("Invalid Input")


