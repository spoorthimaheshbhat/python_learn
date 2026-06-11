# given
names = [
    "alice",
    "bob",
    "charlie"
]

# list in reverse alphabetical order
upper_names = list(sorted(
        map(lambda name: name.upper(), names), reverse = True)
)
print(upper_names)

