# Input:
# word = "programming"
# Count how many vowels exist.

word = input("Enter a word: ")
count = 0

for char in word:
    if char.lower() in "aeiou":
        count += 1

print(f"Number of vowels in given word is: {count}")