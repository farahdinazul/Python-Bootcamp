# number = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{number} x {i} = {number * i}")


for number in range(2, 21):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(number)