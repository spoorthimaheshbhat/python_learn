def count_entry():
    try:
        with open("languages.txt", "r") as given_file:
            lines = given_file.read().splitlines()
            return len(lines)

    except FileNotFoundError:
        print("The file was not found!")

    return None

count_lines = count_entry()
print(f"Total lines: {count_lines}")
print(f"Total known languages: {count_lines - 1}")