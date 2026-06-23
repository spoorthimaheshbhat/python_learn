# Given: List comprehension

squares1 = [x*x for x in range(5)]

# Given: Generator expression

squares2 = (x*x for x in range(5))

print(type(squares1))
print(type(squares2))

# returns a list of squares
print(squares1)

# returns generator object pointer
print(squares2)

for sq in squares2:
    print(sq)