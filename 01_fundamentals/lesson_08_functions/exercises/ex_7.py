def count_vowels(word):
    count = 0
    for letter in word.lower():
        if letter in 'aeiou':
            count += 1
    return count

input_word = input("Enter a word: ")
vowels = count_vowels(input_word)
print(f"Number of vowels in {input_word}: {vowels}")