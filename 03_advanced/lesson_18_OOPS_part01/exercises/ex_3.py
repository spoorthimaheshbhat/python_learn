class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def release_announcement(self):
        print(f"\nNew Book Release Notification!\n"
              f"Check Out! -\n"
              f"{self.title} by {self.author}\n")


def main():
    while True:
        request = input("Do you want to make a release announcement? (y/n): ").lower()

        if request == "y":

            book_title = input("Enter book title: ").title()
            book_author = input("Enter the author's name: ").title()

            book_banner = Book(book_title, book_author)

            book_banner.release_announcement()

        elif request == "n":
            print("\nHave a good day! Bye")
            break

        else:
            print("\nInvalid Input. Try Again.\n")


if __name__ == "__main__":
    main()