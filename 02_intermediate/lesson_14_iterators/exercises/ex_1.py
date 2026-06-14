# given:

colors = ["red","green","blue"]

def print_each(colours):
    iterator = iter(colours)

    while True:
        try:
            print(next(iterator))

        except StopIteration:
            return

print_each(colors)
