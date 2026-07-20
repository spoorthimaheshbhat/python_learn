class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print(f"Area of given rectangle is: {round((self.length * self.width), 2)}")

def main():

    rectangle1 = Rectangle(12,10)
    rectangle2 = Rectangle(123.99, 86.66)

    rectangle1.area()
    rectangle2.area()

if __name__ == "__main__":
    main()