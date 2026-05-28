#Swap two variables without using a third variable.

x = 13675
y = 12883
print("Before swap:")
print("x=",x)
print("y=",y)

# x = x+y
# y = x-y
# x = x-y

x, y = y, x  #Pythonic swapping
print("After swap:")
print("x=",x)
print("y=",y)

