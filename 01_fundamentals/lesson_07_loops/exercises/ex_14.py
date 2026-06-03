# Given: numbers = [4, 7, 2, 7, 9, 7, 1]
# Without using: count()
# Find: how many times 7 occurs
# Expected: 3

numbers = [4, '7', 2, 7, '7', 7, 1]
count = 0
for num in numbers:
    if int(num) == 7:
        count += 1

print(count)
