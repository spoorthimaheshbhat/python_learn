# Take a number from the user.
#
# Print: Positive or Negative or Zero

number = int(input("Enter a number: "))

if number == 0:
    print("Number is zero")
elif number < 0:
    print("Number is negative")
else:
    print("Number is positive")
