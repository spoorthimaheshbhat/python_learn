def fruits():
    yield "apple"
    yield "banana"
    yield "mango"

fruit = fruits()
while True:
    try:
        print(next(fruit))

    except StopIteration:
        break
