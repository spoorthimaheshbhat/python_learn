# Given:

def letters():
    yield "A"
    yield "B"
    yield "C"

letter = letters()
while True:
    try:
        print(next(letter))

    except StopIteration:
        break