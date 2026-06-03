# Given: word = "Python"
# Output: nohtyP
# Constraint: Do NOT use: [::-1]

word = "Python"
i = -1
reverse_word = ""
while i != -(len(word)+1):
    reverse_word += word[i]
    i = i - 1

print(reverse_word)



