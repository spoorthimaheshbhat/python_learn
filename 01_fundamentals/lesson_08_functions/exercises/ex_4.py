def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

num = int(input("Enter a number: "))
result = is_even(num)

if result:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")