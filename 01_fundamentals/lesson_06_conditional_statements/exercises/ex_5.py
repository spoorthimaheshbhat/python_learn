# Create:

correct_username = "admin"
correct_password = "python123"

# Ask user for both.
# Cases:
# Username wrong: Invalid username
# Username correct but password wrong: Invalid password
# Both correct: Login successful

username = input("Enter your username: ")
password = input("Enter your password: ")

if username != correct_username and password != correct_password:
    print("login failed: Invalid username and password")
elif username == correct_username and password != correct_password:
    print("login failed: Invalid password")
elif username != correct_username and password == correct_password:
    print("login failed: Invalid username")
else:
    print("login successful")