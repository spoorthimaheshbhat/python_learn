# Create variables for:
#
# your name
# age
# height
# whether you are learning Python
#
# Print all variables.

name = "Spoorthi"
age = 27
height = 160
learning_python = True #Since this represents a true/false state, a boolean is more appropriate

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Are you learning Python?", learning_python)

#extra learning:

message = "It's raining"
#fact = 'It's raining' #wrong usage
fact = 'It\'s raining'

print("Python strings inside '' : ", fact)
print("Python strings inside \"\" : ", message) #The \ is called an escape character.

paragraph = """This is
a multi-line
string."""

print(paragraph)