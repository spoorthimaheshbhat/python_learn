# Input: given "word"
# Count how many times:
# "s"
# appears.

word = "mississippi"
count = 0
for letter in word:
    if letter == "s":
        count += 1

print(count)