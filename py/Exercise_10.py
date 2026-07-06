def primechecker(number):
    if number <2:
        return False
    for x in range(2, number):
        if number % x == 0:
            return False
        return True
    
print(primechecker(7))
print(primechecker(10))
print(primechecker(5))
print(primechecker(1))