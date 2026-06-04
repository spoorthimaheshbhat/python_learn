def largest(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None

result = largest(-20, 20)

if result is not None:
    print(result)
else:
    print("Numbers are equal")