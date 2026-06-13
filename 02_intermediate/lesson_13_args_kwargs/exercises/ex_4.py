def create_profile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    return None

create_profile(
    name="Alice",
    age=20,
    city="London"
)