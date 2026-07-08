#Basic class definition
class Person:
    #class attribute (shared by all instances)
    species = "Homo sapiens"

    #constructor method
    def __init__(self, name, age):
        #instance attributes
        self.name = name
        self.age = age

    #instance method
    def introduce(self):
        return f"Hi, I am {self.name} and I am {self.age} years old."
    
    #method with parameters
    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday! {self.name} is now {self.age}."
    
#Creatin objects (instances)
person1 = Person("Farah", 43)
person2 = Person("Yasmin", 31)

#Accessing attributes
print(person1.name)
print(person1.age)

#calling methods
print(person1.introduce())
print(person1.have_birthday())

#class attributes
print(Person.species)
print(person1.species)
print(person1.name)

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            return f"Deposited ${amount}. New balance: ${self.balance}."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew: ${amount}")
            return f"Withdrew ${amount}. New balance: ${self.balance}."
        else:
            return "Invalid withdrawal amount or insufficient funds."
        
    def get_balance(self):
        return f"Current balance: ${self.balance}."
    
    def get_transaction_history(self):
        return self.transaction_history

account1 = BankAccount("123456789", "Alice", 1000)
print(account1.deposit(500))
print(account1.withdraw(200))
print(account1.get_balance())
print(account1.get_transaction_history())