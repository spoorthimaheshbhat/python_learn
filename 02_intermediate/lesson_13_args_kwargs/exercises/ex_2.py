def find_largest(*args):
    if not args:
        return None
    return max(args)

numbers = [10, 5, 80, 20]
print(find_largest(*numbers))