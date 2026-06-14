word = "The Devil Wears Prada"

def print_all_letters(given_word):

    iterator = iter(given_word)
    try:
        while True:
            each_letter = next(iterator)
            print(each_letter)

    except StopIteration:
        return None


print_all_letters(word)

print(iter("abc")) # o/p: <str_ascii_iterator object at 0x000001C7DEBB2E30> - location of iterator




