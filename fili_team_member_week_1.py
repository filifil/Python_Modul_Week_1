w = float(input("Weight (kg): "))
h = float(input("Height (m): "))
bmi = w / (h ** 2)
#bmi is 'body mass index' formula
print(f"BMI: {bmi:.2f}")

if bmi < 25:
    print("belowweight")
elif bmi < 30:
    print("Normal")
elif bmi <= 40:
    print("Overweight")
else:
    print("Severely overweight")
