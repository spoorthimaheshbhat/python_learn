def validate_login(username, password):
    if username == "admin" and password == "python123":
        return True
    else:
        return False

user_name = input("Enter your username: ")
pass_word = input("Enter your password: ")

if validate_login(user_name, pass_word):
    print("Login Successful")
else:
    print("Login Failed")