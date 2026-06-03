# Given: numbers
# Search for:
# 30
# Use: break
# Print:Found or Not Found


numbers = [10, 20, 30, 40, 50, 60, 70, 80]

found = False
for num in numbers:
    if num == 30:
        found = True
        break

if found:
    print("Found")
else:
    print("Not Found")