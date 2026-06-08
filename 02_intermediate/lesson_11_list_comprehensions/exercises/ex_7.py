# given list:

words = [
    "cat",
    "elephant",
    "dog",
    "giraffe",
    "bird",
    "buffalo",
    "monkey",
    "rat",
    "mink",
    "cow",
    "deer",
    "donkey",
    "whale"
]

def return_long_words(given_list):
     long_words = [word for word in given_list if len(word) > 4]
     return long_words

print(return_long_words(words))
