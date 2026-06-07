with open("notes.txt", "w") as file:
    file.write("My NoteApp Notes:\n")


def user_request():
    print("Request List:\n")
    done = False
    while not done:
        print("1. Add Note\n"
              "2. View Notes\n"
              "3. Clear All Notes\n"
              "4. Exit"
            )
        request = input("\nPlease enter your request from above list: ").lower()
        if request == "add note" or request == "view notes" or request == "clear all notes" or request == "exit":
            done = True
            return request
        else:
            print("\nInvalid Input! Please enter your request from given list\n")

    return None

def add_note():
    note = input("\nPlease enter your note: ")
    try:
        with open("notes.txt", "a") as given_file:
            given_file.write("\n")
            given_file.write(note)

            print("\nNote Added!\n")

    except FileNotFoundError:
        print("Note file not found!")

def view_notes():
    try:
        with open("notes.txt", "r") as given_file:
            read_notes = given_file.read()

            return read_notes

    except FileNotFoundError:
        print("Note file not found!")


def clear_notes():
    try:
        with open("notes.txt", "w") as given_file:
            given_file.write("My NoteApp Notes:\n")
            print("\nNotes Cleared!\n")

    except FileNotFoundError:
        print("Note file not found!")


def notes_perform():
    do_request = True
    while do_request:
        given_request = user_request()
        if given_request == "add note":
            add_note()

        elif given_request == "view notes":
            print(f"\n{view_notes()}\n\n")

        elif given_request == "clear all notes":
            clear_notes()

        else:
            print("Thank you for using NoteApp! Have a good day!")
            do_request = False

print("Welcome to NoteApp:\nWhat do you want to do today?\n")
notes_perform()