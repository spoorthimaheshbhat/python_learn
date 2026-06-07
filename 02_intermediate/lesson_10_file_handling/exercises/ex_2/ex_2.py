def message():
    messages = input("Enter your message: ")
    return messages

def message_add(contents):
    with open("message.txt", "w") as file:
        file.write(contents)

content = message()
message_add(content)
