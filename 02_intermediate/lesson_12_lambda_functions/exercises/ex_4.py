get_string = input("Enter any note: ")

l = lambda x: len(x.strip().replace(" ", ""))
print(l(get_string))

print(f"Number of characters in your note is: {l(get_string)}")
