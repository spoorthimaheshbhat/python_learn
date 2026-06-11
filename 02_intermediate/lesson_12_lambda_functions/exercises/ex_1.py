numbers = [1,2,3,4,5,6, 45, 33, 56, 82, 90, 77, 75, 21] # given list

squares = list(
    # map each list element to x - return it's square
    map(lambda x: x**2, numbers)
)
print(squares)