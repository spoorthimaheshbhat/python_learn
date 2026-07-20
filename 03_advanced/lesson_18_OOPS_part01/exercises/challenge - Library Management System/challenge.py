# Build a Library Management System.
#
# Create a Book class.

import json
from json import JSONDecodeError


class Book:

    def __init__(self, book_id, title, author, availability):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.availability = availability

    def to_dict(self, dictionary):
        dictionary["book_id"] = self.book_id
        dictionary["title"] = self.title
        dictionary["author"] = self.author
        dictionary["availability"] = self.availability

    def borrow_book(self):
        if self.availability:
            self.availability = False
            print("Book successfully borrowed.")
            return True

        else:
            print("Book not available for borrowing.")
            return False

    def return_book(self):
        if not self.availability:
            self.availability = True
            print("Book successfully returned.")
            return True

        else:
            print("Book cannot be returned.")
            return False

    def display_book_info(self):
        print(f"\nBook ID: {self.book_id}\n"
              f"Title: {self.title}\n"
              f"Author: {self.author}\n"
              f"Availability: {self.availability}\n")


def open_close_json(func):
    def inner(*args, **kwargs):
        try:
            file = open("book_catalogue.json", "r+")
        except FileNotFoundError:
            file = open("book_catalogue.json", "w+")

        file.seek(0)
        try:
            book_list = json.load(file)
        except JSONDecodeError:
            book_list = []

        # Place book_list and file FIRST so they match the function signatures
        result = func(book_list, file, *args, **kwargs)

        file.close()
        return result

    return inner

@open_close_json
def add_book(catalogue, json_file):
    try:
        get_book_id = input("Enter Book ID: ").upper().strip()
        book_title = input("Enter Book Title: ").title().strip()
        book_author = input("Enter Author: ").title().strip()
        avail_input = input("Is the book available? (True/False): ").title().strip()
        if avail_input == "True":
            book_availability = True
        elif avail_input == "False":
            book_availability = False
        else:
            print("Invalid Input. Update Failed")
            return None

        record = {}

        catalogue_record = Book(get_book_id, book_title, book_author, book_availability)
        catalogue_record.to_dict(record)
        catalogue.append(record)

        json_file.seek(0)
        json_file.truncate()


        json.dump(catalogue, json_file, indent=4)

        print("Book added to catalogue.\n")


    except ValueError:
        print("Invalid Input. Update Failed.")


@open_close_json
def search_by_id(catalogue_list, catalogue_file, search_id):
    for book in catalogue_list:
        if book["book_id"] == search_id:
            return Book(book["book_id"], book["title"], book["author"], book["availability"])
    return None

@open_close_json
def modify_book_status(catalogue_list, catalogue_file, target_id, action):
    for book in catalogue_list:
        if book["book_id"] == target_id:
            book_obj = Book(book["book_id"], book["title"], book["author"], book["availability"])

            if action == "borrow":
                was_successful = book_obj.borrow_book()
            elif action == "return":
                was_successful = book_obj.return_book()

            if was_successful:
                book["availability"] = book_obj.availability
                catalogue_file.seek(0)
                catalogue_file.truncate()
                json.dump(catalogue_list, catalogue_file, indent=4)
            return True

    print("Book not found.")
    return False


def main():
    while True:
        try:
            print("List Items: \n"
                  "1. Add Book Information.\n"
                  "2. Display Book Information.\n"
                  "3. Borrow Book.\n"
                  "4. Return Book.\n"
                  "5. Exit Application.\n")

            user_request = int(input("Enter your request number (1-5): "))

            if user_request == 1:
                add_book()

            elif user_request == 2:
                search_book_id = input("Enter search ID: ").upper().strip()
                result = search_by_id(search_book_id)
                if result is not None:
                    result.display_book_info()
                else:
                    print("Book not found.")

            elif user_request == 3:
                borrow_book_id = input("Enter book ID: ").upper().strip()
                modify_book_status(borrow_book_id, "borrow")

            elif user_request == 4:
                borrow_book_id = input("Enter book ID: ").upper().strip()
                modify_book_status(borrow_book_id, "return")


            elif user_request == 5:
                print("Exiting application.")
                break

            else:
                print("Invalid Input.")

        except ValueError:
            print("Invalid Input.")

if __name__ == "__main__":
    main()


