def search(given_list):
    try:
        list_index = int(input("Please enter an index value: "))
        return given_list[list_index]

    except IndexError:
        print("Index does not exist.")

    except ValueError:
        print("Invalid Index.")

numbers = [10, 20, 30, 40, 50]
search_result = search(numbers)
if search_result is not None:
    print(f"Search result is: {search_result}")
