numbers = [1,2]

iterator = iter(numbers)

while True:
    try:
        print(next(iterator))

    except StopIteration:
        print("End reached")
        break

