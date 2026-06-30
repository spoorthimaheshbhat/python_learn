def surround(func):

    def inner():
        print("Before\n")

        func()

        print("\nAfter")

    return inner

@surround
def greet():
    print("Welcome to My Code")

greet()