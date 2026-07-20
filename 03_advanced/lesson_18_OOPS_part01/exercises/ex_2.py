class Car:

    def __init__(self, car):

        self.car = car

    def complete(self):
        print(f"{self.car} -> Car Created")


def main():
    cars = []
    while True:
        try:
            print("Request List:"
                  "\n1. Create Car"
                  "\n2. Exit")
            request = int(input("Enter request number (1 or 2): "))

            if request == 1:
                car_name = input("Enter the name of the car you want to create: ").title()
                cars.append(car_name)

            elif request == 2:
                print("Thank you for using Create Car. Bye!")
                break

            else:
                print("Invalid Input. Try again.")

        except ValueError:
            print("Invalid Input. Try again.")

    for each in cars:
        create_car = Car(each)
        create_car.complete()


if __name__ == "__main__":
    main()