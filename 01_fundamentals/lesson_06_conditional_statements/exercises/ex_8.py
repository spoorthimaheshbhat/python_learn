# Input: Three sides.
#
# Check if a triangle can exist.
#
# Rule:
#
# a + b > c
# a + c > b
# b + c > a
#
# If valid: Valid Triangle
# Else: Invalid Triangle

triangle = []
i = 0

while i < 3:
    triangle.append(int(input(f"Enter side length {i+1}: ")))
    i += 1

a,b,c = triangle

if a<=0 or b<=0 or c<=0:
    print("Invalid input")
elif a + b > c and a + c > b and b + c > a:
    print("Valid Triangle")
else:
    print("Invalid Triangle")
