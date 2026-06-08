words = ["python", "java", "go", "javascript", "TypeScript", "C++", ""]  #given list
null_list = []

def word_length(word_list):
    word_len_list = [len(each_word) for each_word in word_list]
    return word_len_list

print(word_length(words))
print(word_length(null_list))