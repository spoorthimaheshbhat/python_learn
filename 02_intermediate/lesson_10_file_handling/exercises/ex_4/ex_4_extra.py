with open("languages.txt", "w") as file:
    file.write("Known Languages:")

def enter_language():
    language = input("Enter language: ")
    return language

def add_to_file(lang):
    try:
        with open("languages.txt", "a") as file:
            file.write(f"\n{lang}")

    except FileNotFoundError:
        print("The file was not found!")

def done_list():
    done = False
    while not done:
        done_answer = input("Do you want to add another language? (Y/N): ").upper()
        if done_answer == "Y":
            return True

        elif done_answer == "N":
            print("Thank you for your time!")
            return False

        else:
            print("Invalid input.")

    return None


done_adding = True
while done_adding:
    language_entry = enter_language()
    add_to_file(language_entry)
    done_adding = done_list()

