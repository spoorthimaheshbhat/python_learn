with open("greeting.txt", "w") as file:
    file.write("Hello Python")

def greet_user(greet_file):
    try:
        with open(greet_file, "r") as file:
            greeting = file.read()
            return greeting

    except FileNotFoundError:
        print("File not found")

print(greet_user("greeting.txt"))