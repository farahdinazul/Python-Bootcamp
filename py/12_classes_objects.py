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