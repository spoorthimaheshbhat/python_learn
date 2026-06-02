# Input:
# age
#
# Rules:
# Age	Price
# < 5	Free
# 5-17	₹100
# 18-59	₹200
# 60+	₹150
#
# Print ticket price.
# Handle negative ages.

age = int(input("Enter your age: "))

if age > 110 or age <= 0:
    print("Invalid age")
elif age < 5:
    print("Ticket Price: Free")
elif 5 <= age <= 17:
    print("Ticket Price: Rs. 100")
elif 17 < age <= 59:
    print("Ticket Price: Rs. 200")
else:
    print("Ticket Price: Rs. 150")