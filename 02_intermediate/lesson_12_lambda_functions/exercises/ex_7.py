numbers = [5,10,15,20,25,30] # given

large_numbers = list(filter(lambda x: x > 15, numbers))
# filter() only filters elements based on a True or False condition

print(large_numbers)

negative_numbers = [-8, -4, -9, -10, -23, -45, -100, -2323, -30]
# return a positive numbers list with same values

positive_numbers = list(map(lambda x: x * -1, negative_numbers))
# map() applies this transformation to every item in the list.

#positive_numbers = list(map(abs, negative_numbers))
print(positive_numbers)