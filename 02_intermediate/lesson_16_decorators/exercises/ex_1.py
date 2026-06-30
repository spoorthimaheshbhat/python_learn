def announce(func):

    def inner():
        print("Starting...")

        func()

    return inner

@announce
def say_hello():
    print("Hello")

say_hello()



