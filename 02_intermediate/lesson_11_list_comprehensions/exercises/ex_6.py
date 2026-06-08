names = ["alice", "bob", "charlie"]  #given list
null_names = []

def upper_case_list(given_list):
    return [word.upper() for word in given_list]

upper_case_names = upper_case_list(null_names)
if upper_case_names:
    print(upper_case_names)
else:
    print("No names provided")