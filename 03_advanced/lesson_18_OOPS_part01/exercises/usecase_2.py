class TestCase:

    def __init__(self, test_id, test_feature,test_priority, test_status):
        self.test_id = test_id
        self.test_feature = test_feature
        self.test_priority = test_priority
        self.test_status = test_status

    def display_record(self):
        print(f"\nTest ID: {self.test_id}\n"
              f"Feature: {self.test_feature}\n"
              f"Priority: {self.test_priority}\n"
              f"Status: {self.test_status}\n")


    def mark_pass(self):
        self.test_status = "PASS"

    def mark_fail(self):

        self.test_status = "FAIL"

def get_test_data():
    test_id_input = input("Enter the Test ID: ").upper()
    feature = input("Enter the feature under test: ").title()
    priority = input("Enter priority (High -> P1 - P4 -> Low): ").upper()
    status = input("Enter status (Pass/Fail): ").upper()

    return test_id_input, feature, priority, status


def main():
    test_data = TestCase(*get_test_data())
    print("New test data added.\n\n")
    while True:
        try:
            print(f"Request List:"
                  f"\n1. View test record."
                  f"\n2. Mark test status as PASS."
                  f"\n3. Mark test status as FAIL."
                  f"\n4. Exit application.")

            request = int(input("Enter the request number (1-4): "))

            if request == 1:
                test_data.display_record()

            elif request == 2:
                test_data.mark_pass()
                test_data.display_record()

            elif request == 3:
                test_data.mark_fail()
                test_data.display_record()

            elif request == 4:
                print("Exiting application")
                break

            else:
                print("Invalid Input.")

        except ValueError:
            print("Invalid Input.")

if __name__ == "__main__":
    main()