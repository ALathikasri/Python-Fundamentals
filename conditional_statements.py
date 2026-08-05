print("=== Student Performance Analyzer ===")

name = input("Enter student name: ")
marks = float(input("Enter marks (0-100): "))


if marks >= 90 :
    result = "Outstanding"
elif marks >= 75 :
    result = "Excellent"
elif marks >= 60 :
    result = "Good"
elif marks >= 40:
    result = "Pass"
else:
    result = "Fail"

print("\nStudent Report")
print("Name:", name)
print("Marks:", marks)

print("Performance:", result)
