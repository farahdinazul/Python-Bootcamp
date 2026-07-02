age = int(input("Enter your age: "))

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

score = float(input("Enter your score: "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")

user_age = float(input("Enter your age: "))
has_license = True

if user_age >=18 and has_license:
    print("You are allowed to drive")
else:
    print ("You are not allowed to drive")

day = str(input("Enter day: "))
if day == "Saturday" or day == "Sunday":
    print("It is the weekend")
else:
    print("Its a weekday")