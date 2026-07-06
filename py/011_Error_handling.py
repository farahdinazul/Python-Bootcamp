# try:
#     number = int(input("Enter a number: "))
#     result = 10 / number
#     print(f"Result : {result}")
# except ValueError:
#     print("Invalid input! Enter a number")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")

# try:
#     file = open("data.txt", "r")
# except FileNotFoundError:
#     print("File not found")
# else:
#     # Executes if no exception occured
#     content = file.read()
#     print("File read successfully")
# finally:
#     if 'file' in locals() and not file.closed:
#         file.close()
# print("Cleanup completed")

def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 100:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(129)
except ValueError as e:
    print(f"Validation error: {e}")