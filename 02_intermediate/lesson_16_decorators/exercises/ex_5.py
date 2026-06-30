# def decorator(func):
#
#     def inner():
#         print("A")   # the text that wraps the function from above. appears before the function is executed
#         func()        # Function runs and returns the output
#         print("B")    # the text that wraps the function from below. appears after the function is executed
#
#     return inner
#
# @decorator
# def test():
#     print("C")
#
# test()

# o/p:
# A  # the top wrapper text
# C  # the output of function test
# B  # the bottom wrapper text