# Predict output BEFORE running:
#
# a = [1, 2, 3]
# b = a
#
# b.append(4)
#
# print(a)
# print(b)
#
# o/p:
#[1,2,3,4]
#[1,2,3,4]
#
# Explain WHY output occurs. - Here, a and b both refer to the same list which implies:
# When b is manipulated, a gets manipulated too.
#
# Then create a proper independent copy.

a = [1, 2, 3]
b = a.copy()

# b = a[:]

b.append(4)

print(a)
print(b)

