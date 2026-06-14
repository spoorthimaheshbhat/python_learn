def create_file(given_notes):
    # Use "w+" to automatically create the file if it doesn't exist and also read it
    with open("notes.txt", "w+") as file:
        file.write(given_notes)

        # reset file pointer to the beginning of the file
        file.seek(0)
        contents = file.read().splitlines()
        return contents

def input_notes():
    print("Enter your multi-line notes (click enter on empty line to complete): ")
    lines = []

    # loop through the input task until user clicks enter on a blank line
    while True:
        line = input()
        if line == "":
            break
        lines.append(line) # each line is a string element in the list lines

    note = "\n".join(lines)

    print("--- Saved Notes ---\n")
    return note


def iter_through_file(content):
    iterator = iter(content)
    while True:
        try:
            print(next(iterator))

        except StopIteration:
            break

notes = input_notes()
# print(notes) # just checking
file_notes = create_file(notes)
# print(file_notes) #just checking
print("File iteration output:")
iter_through_file(file_notes)

