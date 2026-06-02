# Input marks obtained b/w 1-100
# Assign:
#
# Marks     |	Grade
# 90+	    |   A
# 80-89	    |   B
# 70-79     |	C
# 60-69     |	D
# Below 60	|   F
#
# Also handle invalid marks.

marks = int(input("Enter marks obtained: "))

if marks > 100 or marks < 0:
    print("Invalid Marks")
elif marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
elif marks >= 60:
    print("Grade: D")
else:
    print("Grade: F")


