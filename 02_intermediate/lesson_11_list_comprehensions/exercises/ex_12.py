# given list:

passwords = [
    "abc",
    "python123",
    "admin",
    "securePass2025",
    "123"
]

def list_strong_password(pass_list):
    return [pwd for pwd in pass_list if len(pwd) >= 8]

strong_passwords = list_strong_password(passwords)
if strong_passwords:
    print(f"list of strong passwords: {strong_passwords}")

else:
    print(f"list has no strong passwords.")