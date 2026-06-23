def countdown(y):
    for x in range(y, 0, -1):
        yield x

try:
    n = int(input("Enter an integer to begin countdown: "))
    if n > 0:
        number = countdown(n)

        for num in number:
            print(num)

    else:
        print("Invalid number")

except ValueError:
    print("Invalid Input")

