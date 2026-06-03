# Take a number from the user. Determine whether it is: Prime or Not Prime

number = int(input("Enter a positive number: "))
i = 1
count = 0

if number == 0 or number == 1:
    print("Neither prime nor composite number")
elif number < 0:
    print("Invalid number")
else:
    while i <= number:
        if number % i == 0:
            count = count + 1
        i = i + 1

    if count == 2:
        print("Prime number")
    else:
        print("Not a prime number")