# Take three numbers.
#
# Print the largest.
#
# Constraint
#
# Do NOT use: max()

number = []
i = 0
while i < 3:
    number.append(int(input(f"Enter number {i+1}: ")))
    i = i + 1

# number.sort()
# print(f"Largest of given 3 numbers is: {number[-1]}")


# with conditional statement:

if number[0] >= number[1] and number[0] >= number[2]:
    largest = number[0]
elif number[1] >= number[0] and number[1] >= number[2]:
    largest = number[1]
else:
    largest = number[2]

print(f"Largest of given 3 numbers is: {largest}")


