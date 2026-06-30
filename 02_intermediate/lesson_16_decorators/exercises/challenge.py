def execution_counter(func):

    def inner(count):
        print(f"Function called {count} time(s)")

        func(count)

    return inner

# caller function
@execution_counter
def function_call(num):
    print(f"{num} Execution(s) completed")

def main():
    cnt = 1
    while True:
        user_input = int(input("1. Call function\n"
                               "2. Exit function\n"
                               "Enter your choice (1 or 2): "))
        if user_input == 1:
            function_call(cnt)
            cnt += 1

        elif user_input == 2:
            print("Exiting Function.")
            return None

        else:
            print("Invalid Input.")

if __name__ == "__main__":
    main()