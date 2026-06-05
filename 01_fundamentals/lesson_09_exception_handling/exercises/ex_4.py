def key_search(dictionary):
    try:
        input_key = input("Please enter key value: ")
        return dictionary[input_key.lower()]

    except KeyError:
        print("Key does not exist.")


student = {
    "name": "Alice",
    "age": 20,
    "course": "Python"
}

search_result = key_search(student)
if search_result is not None:
    print(f"Search result is: {search_result}")
