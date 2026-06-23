def numbers():
    yield 10
    yield 20
    yield 30

# create a generator
num = numbers()

# use generator num in for loop
for value in num:
    print(value)