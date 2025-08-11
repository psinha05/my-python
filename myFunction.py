# function in pyhon
# syntax: def function_name(parameters):
import string
import logging

def add(a, b):
    c = a + b
    return c

result = add(5, 10)
print(result)


#
def subNumber(x, y):
     return (x - y)


a = 90
b = 40

res = subNumber(a, b)
print(res)

print('*' * 20)


# for 10 prime numbers
def fun(n):
    x = 2
    count =0
    while count < n :
        for d in range(2, int(x ** 0.5) + 1 ):
           if x % d == 0:
             break
        else:
             print(x)
             count += 1
        x +=1
n = 10
fun(10)

print('passing function as argument below')

# passing function as argument
# A function that takes another function as an argument
def fun(func, arg):
    return func(arg)


def square(x):
    return x ** 2


# Calling fun and passing square function as an argument
res = fun(square, 5)
print(res)


# *args : to pass a variable number of arguments to a function
def arguments(*args):
    for arg in args:
        print(arg)

arguments(1, 2, 3)

# *kwargs:

def fun(**kwargs):
    for keys, val in kwargs.items():
        print(f" {keys}: {val}")

fun(name= "harsh", profession= "marketing", city = "berlin")

# use of def in Python Class
class Person:
    # Constructor method should be __init__
    def __init__(self, name, age, profession='Unknown', city='Unknown', salary=0, language='None'):  # Corrected __init__ method
        self.name = name
        self.age = age
        self.profession = profession
        self.city = city
        self.salary = salary
        self.language = language if language is not None else []

    # Include 'self' parameter in instance methods to access instance variables
    def info(self):  # Corrected by adding 'self'
        print(f"Name: {self.name}, Age: {self.age}, Profession: {self.profession}, City: {self.city}")

    def professional(self):
        print(f"Name: {self.name}, Age: {self.age}, Profession: {self.profession}, salary: {self.salary}, language:{self.language}")

# Create an instance of Person with the required arguments
# p1 = Person('harsh', 'developer', 'paris')
p1 = Person('Harsh', 25, 'Data Analyst', 'Delhi')
p2 = Person(name='Sinha', age =28, profession='AI Engineer', city='Berlin', salary='1.5M', language=['English', 'German', 'Spanish'])
# Call the info method
p1.info()
p2.professional()


def fun():
    name = "Alice"
    age = 30
    return name, age

name, age = fun()
print(name)
print(age)   # Output: 30


# Local Variables
def f1():
    s = ' I love python !'
    print('Inside function:', s)

f1()
#print(s)

# Lambda function (Syntax: lambda arguments : expression)
# lambda: define function, arguments: list of input parameters,
# expression: a single expression that is evaluated and returned.
s1 = 'ilovepython'
s2 = lambda func: func.upper()
print(s2(s1))

n = lambda x: "positive" if x > 0 else "negative" if x < 0 else "zero"

print(n(3))    # positive
print(n(-5))   # negative
print(n(-212)) # negative
print(n(00000))

# lambda and other function
sq = lambda x: x**2
print(sq(3))      # 9

def sqt(x):
    return x**2
print(sqt(3))   # 9

# lambda with list comprehension
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

calc = lambda x, y: (x+y,  x*y)
res = calc(3, 5)
print(res)


# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)    # filter takes 2 arguments, 1st is the lambda function and number itself
print(list(even))

# lambda with map()

# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))


#  map() function: an in-built function that allows to apply a given function to every items of an iterable(list, tuple etc)
#  and return a new iterable (map or list).
# map(function, iterable): function, to apply to each elements, iterable: whose elements wants to modify or transform

number = [1, 2, 3, 4, 5, 6]
result = map(lambda x: x * 2, number)
print(list(result))

# convert string to integers
s = ['1', '2', '3', '4', '5']
res = map(int, s)
print(list(res))

# map to convert list of strings to upper case
s = ['apple', 'orange', 'mango', 'grape', 'litchi']
res = map(str.upper, s)
print(list(res))

# sorted the above string
s = ['guava', 'orange', 'mango', 'grape', 'litchi', 'apple', 'cherry']
res1 = sorted(s)
print(list(res1))


# filter function
x = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
print(list(b))       # [2, 4]

# use filter with map()
x = [1, 2, 3, 4, 5, 6]
b = filter(lambda x: x % 2 == 0, a)
c = map(lambda x: x *2, b)      # [4, 8]
print(list(c))


# Inner function

def outer():
    s= "in the outer space"

    def inner():
        print(s)

    inner()

outer()

logging.basicConfig(level=logging.INFO)  # configure logging
def logger(func):
    # logs function execution details

    def wrapper(*args, **kwargs):
        logging.info(f"Executing {func.__name__} with {args}, {kwargs}")  # log function call
        return func(*args, **kwargs)  # call original function

    return wrapper
@logger
def add(a, b):
    return a + b  # return sum

print(add(3, 4))


# Decorators are a powerful and flexible way to modify or extend the behavior of functions or methods,
# without changing their actual code. a function that takes another function as an argument and returns
# a new function with enhanced functionality(used for logging, authentication and memorization).

def decorator(func):

    def wrapper():
        print('Before calling the function')
        func()
        print('After calling the function')
    return wrapper

@decorator
def greet():
    print("Hello Decorator !")

greet()


