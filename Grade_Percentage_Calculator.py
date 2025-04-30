"""
Author: Blessing Glory Tsikey

Purpose: Determine and display letter grades, including +/-.
"""
grade_percentage = int(input("Enter your grade percentage: "))

if grade_percentage >= 90:
    letter = "A"
elif grade_percentage >= 80:
    letter = "B"
elif grade_percentage >= 70:
    letter = "C"
elif grade_percentage >= 60:
    letter = "D"
else:
    letter = "F"

sign = ""
last_digit = int(grade_percentage) % 10
if letter != "F":
    if last_digit >= 7:
        sign = "+"
    elif last_digit < 3:
        sign = "-"

if letter == "A" and sign == "+":
    sign = ""


print(f"Your final grade is: {letter}{sign}")

if grade_percentage >= 70:
    print("Congratulations! You passed the class.")
else:
    print("Don't give up! Keep working hard, and you'll improve next time.")
