get_number = int(input("Enter a number: "))

is_even = lambda x: x % 2 == 0

if is_even(get_number):
    print("Even")
else:
    print("Odd")