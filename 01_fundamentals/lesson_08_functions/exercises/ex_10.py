def calculate(a, b):
    return a + b, a - b, a * b

x,y = int(input("Enter a number: ")), int(input("Enter another number: "))
sum_calc, difference_calc, multiply_calc = calculate(x, y)

print(f"Sum is: {sum_calc}, "
      f"Difference is: {difference_calc}, "
      f"Product is: {multiply_calc}")