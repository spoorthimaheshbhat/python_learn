def calculate_grade(marks):
    if marks < 0 or marks > 100:
        return None
    elif marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"

score = int(input("Enter marks: "))
result = calculate_grade(score)

if result is not None:
    print(f"Grade is: {result}")
else:
    print("Invalid marks")