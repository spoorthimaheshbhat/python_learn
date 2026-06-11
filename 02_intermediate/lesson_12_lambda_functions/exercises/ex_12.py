# given
logins = [
    ("alice", 5),
    ("bob", 15),
    ("charlie", 2),
    ("admin", 25)
]

high_logins = list(filter(lambda user: user[1] > 10, logins))
print(high_logins)