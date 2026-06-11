numbers = [1,2,3,4,5,6,7,8,9,10] # given

even_list = list(filter(lambda x: x % 2 == 0, numbers))

action = input("Choose even or odd:").strip().lower() # clean string
if action == "even":
    print(even_list)

else:
    print([number for number in numbers if number not in even_list])