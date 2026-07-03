#Create a grocery list and perform various operations

groceries = ["Milk", "Eggs", "Bread", "Chocolates"]
groceries.append("Maggi")
groceries.insert(1, "Chillies")
groceries.remove("Milk")
popped = groceries.pop()
groceries.sort()
groceries.reverse()
groceries + ["Fruits"]
print(len(groceries))
print(groceries)
print(popped)


#Write a program to find largest and smallest number in a list
def find_min_max(numbers):
    if not numbers:
        raise ValueError("List cannot be empty")

    smallest = largest = numbers[0]
    for n in numbers[1:]:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n

    return smallest, largest


if __name__ == "__main__":
    numbers = [12, 4, 56, 7, 23, 89, 1, 45]
    smallest, largest = find_min_max(numbers)
    print(f"List: {numbers}")
    print(f"Smallest: {smallest}")
    print(f"Largest: {largest}")
