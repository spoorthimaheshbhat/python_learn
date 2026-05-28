# Create variables of all major data types:
# int, float, string, bool, list, tuple, dict, set
#
# Print their types using type().

greeting = "Hello, ChatGPT"
print(f"greeting: {type(greeting)}") #Because later debugging becomes MUCH easier in large systems.

exercise_no = 2
print(f"exercise number: {type(exercise_no)}")

difficulty_level = 1.5
print(f"difficulty level: {type(difficulty_level)}")

completed = True
print(f"Completed? {type(completed)}")

topics = ["variables", "datatypes"]
print(f"Topics covered: {type(topics)}")


exercises_count = (1, 2, 3, 4)
print(f"Exercise Count: {type(exercises_count)}")

exercises_done = {1:"yes", 2:"yes", 3:"no" , 4:"no"}
print(f"Exercised done: {type(exercises_done)}")

status = {"Completed", "two", "exercises"}
print(f"Completion: {type(status)}")
