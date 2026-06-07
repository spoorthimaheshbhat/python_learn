def count_words():
    try:
        with open("passage.txt", "r") as given_file:
            word_count = given_file.read().split()
            #print(word_count)
            return len(word_count)

    except FileNotFoundError:
        print("The file was not found!")

    return None

words = count_words()
print(f"Total number of words: {words}")
