#  Strings: A string is a sequence of characters. Python treats anything inside quotes as a string.
#  This includes letters, numbers, and symbols.

# a). creating a string (either single or double quotes)
s= 'Hello'
t = "python"

print(s + ' ' +t)


p='0711'
print(p)

b = 'True'
print(b)

# multiline string
s = """I am Learning
Python String on GeeksforGeeks"""
print(s)

s = '''I'm a 
Geek'''
print(s)

# b). Accessible elements in a python: using the index position of the elements.
# Accessing an index out of range will cause an IndexError,
#  -1 refers to the last character, -2 refers to the second last character,

print(t[0])

s = "GeeksforGeeks"

# Accesses 3rd character: 'k'
print(s[-10])

# Accesses 5th character from end: 'G'
print(s[-5])

# String Slicing: to extract a portion from start to end(excluded)

s = "GeeksforGeeks"

# Retrieves characters from index 1 to 3: 'eek'
print(s[1:4])

# Retrieves characters from beginning to index 2: 'Gee'
print(s[:3])

# Retrieves characters from index 3 to the end: 'ksforGeeks'
print(s[3:])

# Reverse a string: 'skeeGrofskeeG'
print(s[::-1])

# String Immutability: once string created, they can't be changed
x = 'test'
# x[3]= 'k'   # TypeError: 'str' object does not support item assignment
print(x)
x = "p" + x[1:4]
print(x)

# Delete a string : As string are immutable, so can't be delete an individual elements.
# for deleting an entire string using an 'del' keywords

q = 'DeleteThisMessage'
print(q)

del q
# print(q)   #  NameError: name 'q' is not defined

# To updating a string : we need to create a new string since strings are immutable.
s = "hello geeks"

# Updating by creating a new string
s1 = "H" + s[1:]

# replacnig "geeks" with "GeeksforGeeks"
s2 = s.replace("geeks", "GeeksforGeeks")
print(s1)     # Hello geeks
print(s2)     # hello GeeksforGeeks

# common string methods

# 1). len() : function returns the total number of characters in a string.
s = "GeeksforGeeks"
print(len(s))

# 2). upper() and lower() : to converts the string into lower and UPPER case
s = "Hello World"

print(s.upper())   # output: HELLO WORLD
print(s.lower())

# 3). strip() : removes leading and trailing whitespace from the string
# replace(old, new)   : replaces all occurrences of a specified substring with another.

s = "   Gfg   "

# Removes spaces from both ends
print(s.strip())

s = "Python is fun"

# Replaces 'fun' with 'awesome'
print(s.replace("fun", "awesome"))

# 4). concatenating and repeat strings : + operator for concatenation and
#     * operator for repeat a string

s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2
print(s3)

s = "PYTHON"
print(s * 3)

# format string : Python provides several ways to include variables inside strings
# f-strings
name = "Alice"
age = 22
print(f"Name: {name}, Age: {age}")

# using in
s = "GeeksforGeeks"
print("Geeks" in s)   # True
print("GfG" in s)     # False


# List in Python : Lists are used to store multiple items in a single variable.
#  Order sequence of data types, use the [] (square bracket) for storing the data. List are mutable
#  List items are ordered, changeable, and allow duplicate values.
#  the items have a defined order, and that order will not change.

# Note: the list will always retain the order of elements as you inserted them.

my_list = []
my_list.insert(0, 50)
my_list.insert(1, 35)
my_list.insert(2, 55)
my_list.insert(3, 20)
my_list.insert(4, 11)
my_list.insert(5, 25)
my_list.insert(6, 1)
my_list.insert(7, 75)
my_list.insert(8, 49)
my_list.insert(9, 15)
my_list.insert(10, 99)

print(my_list)

# Difference between insert() and append():
# append(): Add always at the end of list, no shifting of elements, just wants to add the elements(at the end)
# insert() : at any specified index position, elements are shifted to right, more controls where have to add the element

myList = ['Apple', 'Banana', 'Orange', 'Mango', 'guava']

print(myList)
print(myList[0])
print(myList[1])
print(myList[4])

print(myList[-1])   # in the reverse order

# Add new item to the list
myList.append('Papaya')     # this item will be add to the end of the list
myList.append('Litchi')
print(myList)

# delete a value form the list
myList.remove('Mango')
print(myList)

# to modify the values from the list
myList[3] = 'Lemon'

print(myList)

# adding an item to the given positions
myList.insert(1, 'Grapse')
print(myList)

# delete an item using an index positions
del myList[5]
print(myList)

# no. of items in the list
print(len(myList))

# sorting a list
myList.sort()
print(myList)

# reverse sort
myList.sort(reverse=True)
print(myList)

# reverse
myList.reverse()     # to reverse the list
print(myList)

# temporary sorting of a list


# popping the items in the list, this would be the last items to be removed
myList.pop()
print(myList)

# use pop using the index
myList.pop(1)
print(myList)

"""
Use pop() when you want to remove an item by index and you need the removed item.Returned remove item, raise IndexError
Use remove() when you want to remove the first occurrence of a specific value in the list.Not returned, ValueError(), if not found
Use del when you want to remove an item by index, delete a slice, or even delete an entire variable.Not return, raise IndexError

"""

# Key differences between remove(0 and del():
# remove(): delete by value, raise the error if value not in the list, returns nothing(none)
# del(): based on index(slice or entire variable), index out of the range(error raises), nothing returns
# pop(): remove and returns an element from list, remove last element or specify index.
# Raises error, if list is empty or index out of range

# Slicing of the list

print(myList[0:2])

print(myList[:2])    # default index(start index) will be 0 till 2

print(myList[-2: ])  # Grapse, Guava (-2 items till the end of the list)

# Numeric list
sell = [2, 9, 13, 28, 35, 4, 56]
print(max(sell))

print(min(sell))
print(sum(sell))

sell1 = [2, 9, 13, 28, 35.5, 4, 56, 3.2, 99]

print(max(sell1))

print(min(sell1))
print(sum(sell1))

# mix list
mix_list = ['harsh', 99, 22.5, True, 'hello']
print(mix_list)

print('************ Tuple **************************')

# TUPLES:
# Tuple items are ordered, unchangeable, and allow duplicate values. Tuples order will not change.
# Tuples are Immutable, cannot change, add or remove items after the tuple has been created.
# Tuples are written with round brackets ().

mytuple = ("apple", "banana", "cherry")

print(mytuple)
print(mytuple[0])

# try to modify the tuples, TypeError: tuple object does not support item assignment.
# mytuple[1]= 'Mango'   #TypeError: 'tuple' object does not support item assignment
# print(mytuple)

mytuple = ("apple", "banana", "cherry", "apple")
print(mytuple.count("apple"))    # to count the items in the tuple

print(mytuple.index('cherry'))   # to find the index of the given item

# although not changes in tuples, but assigned to new items
mytuple = (11, 22, 33, 44, 55)

print(mytuple[4])

tup1 = ('11', '22', '33')
print(tup1)

tup1 = ('Delhi', 'Berlin')
print(tup1)

print("######## DICTIONARY ############")

# DICTIONARY :
# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered, changeable and do not allow duplicates.
# Dictionaries are written with curly brackets {}, and have keys and values.
# Dictionaries cannot have two items with the same key.

car = {'brand': 'Audi', 'model': 'Q6'}
print("Brand of the car is: " + car['brand'])
print("Model of the car is: " + car['model'])

# to access the key and values of dictionary
print(car.get('brand'))

# get() : by using the get(), if key is not present it returns None rather then Error
print(car.get('year'))  # none, no Error

# add key and values to Dictionary
car['year'] = 2020
car['Country'] = 'Germany'

print(car)

car['year'] = 2020
car['Country'] = 'France'

print(car)

# delete a value from the dictionary : del dictionaryName['key']
del car['Country']

print(car)

# to get the length of key-values pairs
print(len(car))

# SETS
# A set is a collection which is unordered, unchangeable*, and unindexed. *unchangeable, but can remove and add new items
# Sets are written with curly brackets {}.
#  Sets are unordered, so you cannot be sure in which order the items will appear.
# Set do not allow duplicate values. Also  Sets appears different order every time you use them.

myset = {'Rose', 'Marigold', 'Jasmine', 'Sunflower', 'Lilly', 'Jasmine'}

print(myset)   # order does not maintained, everytime it changed. No duplicate allowed in Sets

# add new items in sets
myset.add('Blueberry')     # new flower has added in the sets
print(myset)

# Sets used for uniqueness, so convert the List into Sets as well.
myList1 = {'Rose', 'Marigold', 'Jasmine', 'Sunflower', 'Lilly', 'Jasmine', 'Rose', 'Blueberry'}

mySets1 = set(myList1)  # Repetition of 'Rose' and 'Jasmine' removed in newly created Sets.
print(mySets1)

# Sets methods:

# 1). add() : to add the new elements to the set
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# 2). clear() : Removes all elements from the set, making it an empty set
#      my_set.clear()

# 3). copy(): returns a shallow copy of the set
my_copy = my_set.copy()
print(my_copy)

# 4). discard() : Removes an element from the set if it exists if elements not exist, it does nothing (unlike remove, raise an keyerror)
my_set = {1, 2, 3}
my_set.discard(2)
print(my_set)  # Output: {1, 3}
my_set.discard(5)
print(my_set)

# 5) pop(): remove and returns an arbitrary elements from the sets.
my_set = {1, 2, 3, 4, 5}
pop_elements = my_set.pop()
print(pop_elements)  # 1 ( pop up an element randomly)


# if-elif-else condition(elif, if previous condition are not meet. Else, if all the conditions are not meet)

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# pass statement, use as a placeholder

a = 33
b = 200

if b > a:
  pass

# while loop: while loop can execute a set of statements as long as a condition is true.

i= 1
while i < 6:
    print(i)
    i += 1

print('\n')

print('***** break  Statement*****')
# break statement
i=1
while i < 6:
    print(i)
    if i==3:
        break
    i +=1

# Continue Statement
print('***** Continue Statement*****')
i=0
while i < 6:
    i +=1
    if i==3:
        continue
    print(i)


# for loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('***  use of for loop ***')

# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print('*************************')

# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


# range() function

for x in range(6):    # 0 to 5, but 6 not included
  print(x)

print('\n')

for x in range(2, 6):    # 2 to 6 ,  6 not included
    print(x)

print('****  with Increment in range function ******')

for x in range(2, 30, 3):
  print(x)

# Functions:
# Block of code which perform some task and run when it is called
# can be reuse many times in our program when requires, so line of code to reduced
# can pass arguments to the methods

# defining a function
def myfun():
    print('function is called..')

myfun()

print('*' * 20)


# defining a function
def userLogin(name, age=None):      # age is none, in case of *david, age is not available
    print(f'Name is {name}')
    print(f'Age is {age}')
    print('Thanks for signining...')
    print('*' * 20)

#calling afunction
userLogin('harsh', 28)
userLogin('riya', 30)
userLogin('david')

# Parameters variable names in function definition, acts as placeholders for the values that will be passed into the function
# Arguments: these are actual values pass to the function when you call it, fill the parameters with real data.

# Arbitrary arguments *args: If don't know the no. of arguments passed to functions,
# function will receive a tuple of arguments, and can access the items accordingly:

def greetings(user_name, *hobbies):      # dynamic arguments functions
    print(f'Name is {user_name}')
    print('Hobbies are:')
    for hobby in hobbies:
        print(f'- {hobby}')

greetings('harry', 'singing')
greetings('anu', 'dancing', 'painting', 'cooking')
print('*' * 20)


# Keyword arguments, **kwargs: if don't know the no. of arguments will be passed into your functions, add ** before parameters
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def empInfo(emp_name, **emp_info):
    print(f'Employee Name is {emp_name}')
    for key, value in emp_info.items():
        print(f'{key} is {value}')

empInfo('smith', age=22, city='berlin', email='smith123@gmail.com')
empInfo('keith', age=28, city='munich', email='keith@abc.com')
empInfo('sam')

# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Default parameters value: call the function without arguments, it uses the default values
def my_function(country = "Norway"):
    print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()       # no arguments provided in function calling
my_function("Brazil")

# Passing List as an arguments
# if you send a List as an argument, it will still be a List when it reaches the function:
def my_function(food):
    for x in food:
        print(x)

fruits = ['Apple', 'Banana', 'Mango', 'Cherry']

my_function(fruits)

# Return Values: to let the function return a values, use the return statement
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))

#  Recursive function: function  that calls itself

def factorial(x):

    """
    This is a recursive function
    to find the factorial of an integer
    """

    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))


num = 5
print("The factorial of", num, "is", factorial(num))

# main function:


#  lambda function / Anonymous Function :
# A lambda function is a small anonymous function.
# A lambda function can take any number of arguments, but can only have one expression.
#   lambda arguments : expression

# print(dir())

# List comprehension : to create lists using a concise syntax. It allows us to generate a new
# list by applying an expression to each item in an existing iterable (such as a list or range)

a = [2,3,4,5]
res = [val ** 2 for val in a]
print(res)

# apply filter on list
a = [1, 2, 3, 4, 5]
res = [val for val in a if val % 2 == 0]
print(res)