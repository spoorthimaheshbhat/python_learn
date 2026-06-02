# Take a year from the user.
#
# Rules:
#
# A leap year is:
#
# divisible by 400, OR
# divisible by 4 but not by 100

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("It's a leap year")
else:
    print("It's not a leap year")