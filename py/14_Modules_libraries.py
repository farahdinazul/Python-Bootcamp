# from maths_util import add, multiply, factorial, PI, Calculator

# result = add(5, 3)
# print(f"Addition Result: {result}")

# result = multiply(10, 5)
# print(f"Multiplication Result: {result}")

import os
import sys
import datetime
import random

#only use line15 when we want to access API key or module created outside of py module or different directory
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

now = datetime.datetime.now()
today = datetime.date.today()
formatted_date = now.strftime("%d-%m-%y %H:%M:%S")
print(f"Now date: {now.strftime('%d-%m-%y %H:%M:%S')}")
print(f"Current Date: {today.strftime('%d-%m-%y')}")
print(f"Current Date and Time: {formatted_date}")

random_number = random.randint(1, 100)
random_choice = random.choice(['apple', 'banana', 'orange'])
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)

print(f"Random Number: {random_number}")
print(f"Random Choice: {random_choice}")
print(f"Shuffled List: {numbers}")
