def get_transaction(given_file):
    try:
        # Open the file manually so it stays open while values are streamed
        current_file = open(given_file.lower(), "r")

        # Loop directly over the file object to read line-by-line automatically
        for line in current_file:
            try:
                # Clean up hidden spaces or newline breaks
                cleaned_line = line.strip()

                # Skip completely blank lines safely
                if not cleaned_line:
                    continue

                transaction = float(cleaned_line)

                if transaction >= 0:
                    yield f"Processed Transaction: {transaction:.2f}"
                else:
                    yield f"Failed Transaction: {transaction * -1:.2f}"

            except ValueError:
                # Handles case where the transaction value isn't a number
                yield f"Invalid Transaction Encountered: '{line.strip()}'"

        # Cleanly close the file when the loop finishes streaming all data
        current_file.close()

    except FileNotFoundError:
        print("Given User Does Not Exist.")
        return None




# Safely consume the generator values individual by individual
def main():
    # Initialize the generator stream
    file_name = input("Enter the user's name whose transactions you want to access: ").lower()
    transactions = get_transaction("transactions_" + file_name + ".txt")

    try:
        while True:
            try:
                request = input("Display transactions? (y/n): ").lower()
                if request == "y":

                    request_number = int(input("Number of transactions you wish to see?: "))

                    if request_number < 0:
                        print("Invalid Number! Try again.")
                        continue

                    while request_number >= 1:
                        print(next(transactions))
                        request_number -= 1

                elif request == "n":
                    print("Thank you! See you next time.")
                    break

                else:
                    print("Invalid Input! Try again.")

            except ValueError:
                print("Invalid Number! Try again.")


    except StopIteration:
        print("End of Transaction Records! Thank you.")


if __name__ == "__main__":
    main()