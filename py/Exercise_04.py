weight = float(input("Enter your weight: "))
height = float(input("Enter your height: "))
bmi = weight / (height ** 2)

print("Your bmi is:", round(bmi,2))

if bmi < 18.5:
    print("You are underweight")
elif bmi  < 24.9:
    print("You are at a normal weight")
elif bmi  < 29.9:
    print("You are overweight")
else:
    print("You are obese")