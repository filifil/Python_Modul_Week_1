# Lesson 1: Get Midterm Grade
midterm = float(input("Enter Midterm Grade: "))

# Lesson 2: Get Final Grade
final = float(input("Enter Final Grade: "))

# Lesson 3: Calculate Year-End Average
average = (0.40 * midterm) + (0.60 * final)

# Lesson 4: Result
if average < 50:
  print("failed")
else:
  print("successful")