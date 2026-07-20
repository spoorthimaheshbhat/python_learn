class Circle:

    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.14

    def circumference(self):
        return round(2*self.pi*self.radius, 2)

def main():
    circle_1 = Circle(12)
    circle_2 = Circle(18.56)

    print(circle_1.circumference())
    print(circle_2.circumference())

if __name__ == "__main__":
    main()