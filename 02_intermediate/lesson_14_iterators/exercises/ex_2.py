# given:

word = "Python"

for letter in word:
    print(letter)

print("\n")

# what for loops do internally -
iterator = iter(word)
while True:
    try:
        letter = next(iterator)
        print(letter)

    except StopIteration:
        break
