#module is a collection of functions
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def factorial(n):
    if n <=1:
        return 1
    else:
        return n * factorial(n - 1)

PI = 3.14159

class Calculator:
    def __init__(self):
        self.history = []

    def calculator(self, operation,a, b):
        if operation == "add":
            result = add(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        else:
            result = None

        self.history.append(f"{operation}({a}, {b}) = {result}")
        return result