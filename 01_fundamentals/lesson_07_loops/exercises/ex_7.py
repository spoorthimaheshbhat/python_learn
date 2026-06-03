# Correct password: python123
#
# Allow the user only 3 attempts.
#
# If correct: Access Granted
#
# Otherwise: Account Locked (after 3 failed attempts).

attempt = 0
correct_password = "python123"

while attempt < 3:
    password = input("Enter a password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Wrong password: Try again")
        attempt += 1

if attempt == 3:
    print("Access denied. Account Locked")
