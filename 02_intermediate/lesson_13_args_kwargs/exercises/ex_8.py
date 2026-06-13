def multiply_all(*args):
    result = 1
    for a in args:
        result = result * a

    return result

numbers = [2, 3, 4]
print(multiply_all(*numbers))