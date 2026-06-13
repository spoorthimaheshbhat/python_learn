def register_user(username, **details):
    print(f"Username: {username}")
    for detail, content in details.items():
        print(f"{detail.title()} : {content}")

register_user(
    "spoorthi",
    email="spoorthi@gmail.com",
    city="Bangalore",
    profession="QA"
)
