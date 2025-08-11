#  Class: A class is considered a blueprint of objects. The variables inside the class are called attributes.
#  Object: An object is an instance of the class

class Bike:
    gear = 0
    tyre = 0
    engine = 0
    name = ""


# create an object of the class
bike1 = Bike()

bike1.engine = 180
bike1.name= 'Yamaha'
bike1.tyre = 2
bike1.gear = 5

print(f"Name: {bike1.name}, Gears: {bike1.gear} ")



# Define a class

class Employee:
    # define a property
    employee_id = 0


# create two objects of the Employee class
employee1 = Employee()
employee2 = Employee()

# access property using employee1
employee1.employeeID = 1001
print(f"Employee ID: {employee1.employeeID}")

# access properties using employee2
employee2.employeeID = 1002
print(f"Employee ID: {employee2.employeeID}")



# Python Methods
class Room:
    breadth = 45
    length = 60

    def calculate_area(self):
        print(f'Calculate the room area = ', self.length * self.breadth)

# to create an class objet
study_room = Room()

#study_room.length = 45
#study_room.breadth = 60

study_room.calculate_area()


# Python constructors

class Bike:

    # constructor function
    def __init__(self, name = "", type = "", year = ""):
        self.name = name
        self.type = type
        self.year = year


bike2 = Bike()
bike2.name = 'Hero'
bike2.type = 'Racing'
bike2.year = 2022

print(f'My bike is: {bike2.name}, {bike2.type}, {bike2.year}')

# __init__() is the constructor function that is called whenever a new object of that class is instantiated.

# Python Inheritance: Python supports class inheritance. It allows us to create a new class from an existing one.
# The newly created class is known as the subclass (child or derived class).
#  The existing class from which the child class inherits is known as the superclass (parent or base class).

# example of inheritance

class Animal:
    name = ''

    def eat(self):
        print('I can eat')

# inherit from Animal
class Dog(Animal):

    # introduced new methods in sub class dog
    def display(self):
        print('my name is ', self.name)

# create an object of a class
labrador = Dog()

labrador.name = 'Jimmy'
labrador.eat()    # object of the sub class can access the methods of super class.

# to access the subclass methods
labrador.display()

# Methods Overridding: same methods present in both the subclass and super class.

print('************* Inhertiance *****************')
class Animal:
    def eat(self):
        print('eat methods in the parent class')


class Creature(Animal):
    def eat(self):
        print('eat methods in the child class')


lab = Animal()
lab.eat()    # here eat called to the parent class eat() methods


lab1 = Creature()
lab1.eat()     # here eat calling the child class eat() methods

print('#######  super() in the inheritance ###########')

# super() function in Inheritance: to access the methods of the super class function

class Animal:
    name = ''

    def eat(self):
        print('In the SuperClass eat methods..')

# inherit from Animal
class Dog(Animal):

    # override the superclass eat() methods

    def eat(self):
        super().eat()
        print('my name is ', self.name)
        print('In the subclass eat() methods')

# create an object of a class
labrador = Dog()

labrador.name = 'Tanny'
labrador.eat()    # object of the sub class can access the methods of super class.

print('********** MULTIPLE INHERITANCE ************')

# Python Multiple Inheritance

class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()


print('********** MULTILEVEL INHERITANCE ************')

# Python Multilevel Inheritance : can also derive a class from the derived class.

class SuperClass:

    def super_method(self):
        print("Super Class method called")

# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")

# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()  # Output: "Derived class 2 method called"


# Polymorphism in Python
#  It refers to the use of a single type entity (method, operator or object) to
#  represent different types in different scenarios.

# example of len function
print(len("Programiz"))      # for string(length of string), list(no. of items), Dictionary(no. of keys)
print(len(["Python", "Java", "C"]))
print(len({"Name": "John", "Address": "Mumbai"}))

print('$$$$$$$$ Class Polymorphism $$$$$$')

# Class Polymorphism
# while creating class methods as Python allows different classes to have methods with the same name.

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()


# Note: Method Overloading, a way to create multiple methods with the same name but different arguments,
# is not possible in Python.

# some special functions in python
"""
__init__() initializes the attributes when the object is created.
__str__() provides a string representation for the object (for print statements).
__len__() allows you to use len() on an object.
__add__() allows you to use the + operator between objects.
__call__() allows an object to be called as a function.

"""

# __init__(): Initialize the attributes of the object
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Create an object
p = Person('Harsh', 30)
print(p.name)  # Output: Harsh
print(p.age)   # Output: 30

# __str__ : Returns a string representation of the object

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, Age: {self.age}"

p = Person("Alice", 30)
print(p)  # Output: Person: Alice, Age: 30

#  __len__() - Returns the length of the object

class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

# Create an object
obj = MyList([1, 2, 3, 4])
print(len(obj))  # Output: 4


#  __add__() - Adds two objects

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3)  # Output: Point(6, 8)


# __call__() - Call objects of the class like a normal function

class Adder:
    def __init__(self, value):
        self.value = value

    def __call__(self, number):
        return self.value + number

# Create an object
adder = Adder(10)
print(adder(5))  # Output: 15 (as the object is called like a function)
