def is_prime(number):
    count = 0
    if number == 1 or number == 0:
        return None
    else:
        for i in range(1, number + 1):
            if number % i == 0:
                count += 1
    if count == 2:
        return True
    else:
        return False

num = int(input("Enter a number: "))
result = is_prime(num)
if result is None:
    print(f"{num} is a neither a prime nor a composite number")
elif result:
    print(f"{num} is a prime number")
else:
    print(f"{num} is a composite number")
