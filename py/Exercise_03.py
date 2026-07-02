welcome = "Hello, Welcome to Simple Addition Calculator"
number_1 = float(input("Enter first number: "))
number_2 = float(input("Enter next number: "))
operation = str(input("Choose + - * /: "))

if operation == "+":
    answer = number_1 + number_2
    print(f"Answer is {answer}.")

elif operation == "-":
    answer = number_1 -number_2
    print(f"Answer is {answer}.")

elif operation == "*":
    answer = number_1 * number_2
    print(f"Answer is {answer}.")

elif operation == "/":
    if number_2 == 0:
        print("Cannot divide by zero!")
    else:
        answer = number_1 / number_2
    print(f"Answer is {answer}")

else:
    print("Invalid Operation")

