age = int(input("Enter your age: "))
has_ticket = input("Do you have the ticket? y/n: ").lower()

if has_ticket not in ["y", "n"]:
    print("Invalid Input")

elif has_ticket == "y" and age >= 18:
    print("You are eligible to enter the theater")

else:
    print("You are not eligible to enter the theater")