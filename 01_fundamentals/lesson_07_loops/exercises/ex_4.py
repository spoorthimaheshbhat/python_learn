# Take a number from the user.
# Output:
#
# 5 x 1 = 5
# 5 x 2 = 10
# ...
# 5 x 10 = 50

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number*i}")