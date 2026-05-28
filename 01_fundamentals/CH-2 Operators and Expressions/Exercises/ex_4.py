# Exercise 4 — Logical Operators
# Create:
# age
# has_ticket
#
# Check:
# if a person can enter a movie theater
# condition:
# age >= 18
# AND has ticket

age = int(input("Enter your age: "))
has_ticket = input("Do you have the ticket? y/n: ")

if has_ticket == "y" and age >= 18:
    print("You are eligible to enter the theater")
elif has_ticket == "n":
    print("You are not eligible to enter the theater")
elif has_ticket == "y" and age < 18:
    print("You are not eligible to enter the theater")
else:
    print("Invalid Input")