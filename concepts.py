import keyword

# input function

# name = input("Enter your name: ")
# print("Hello,", name, "! Welcome!")

# single variable
s= "bobby"
print(s)

# multiple variables


s= 'harsh'
age = 25
city ="Berlin"
print(s, age, city)

# string.split(separator, maxsplit)
#x, y = input('enter the two values').split()
# print(x)
# print(y)

text = 'hello world python'
result = text.split(' ', 2)
print(result)

# e=input('please enter the age')
# age = int(e)

if age <18:
    print('you are a minor person')
elif age >=18 and age < 65:
    print('you are Adult person')
else:
    print('you are a senior citizen')

# data type

a = "Hello World"
b = 10
c = 11.22
d = ("Geeks", "for", "Geeks")
e = ["Geeks", "for", "Geeks"]
f = {"Geeks": 1, "for":2, "Geeks":3}

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

# example of 2f: f refers to represents float and 2 for the two decimal places.
number = 3.14159
formatted = f"{number:.2f}"
print(formatted)

# in the print() function the seperator is new line, we could format as per requirements
# end Parameter with '@'
print("Python", end='@')
print("GeeksforGeeks")


# Seprating with Comma
print('G', 'F', 'G', sep='')

# for formatting a date
print('09', '12', '2016', sep='-')

# another example
print('pratik', 'geeksforgeeks', sep='@')

# formatted string literals(f or F): Inside the curly braces {}, you can include variables or expressions,
# and they will be evaluated and inserted into the string.

name = "Alice"
age = 30
greeting = f"Hello, my name is {name} and I am {age} years old."
print(greeting)

#  Using % Operator
#     %d –integer
#     %f – float
#     %s – string
#     %x –hexadecimal
#     %o – octal

num = int(input('Enter a value'))
add = num + 5
print('the sum is %d' %add)

# assign variables
a= b = c = 10
print(a, b, c)

x, y, z = 1, 2.5, "Python"
print(x, y, z)

# swapping two variables
a, b = 5, 10
a, b = b, a
print(a, b)

# Rules for Naming Variables
# To use variables effectively, we must follow Python’s naming rules:
#
#     Variable names can only contain letters, digits and underscores (_).
#     A variable name cannot start with a digit.
#     Variable names are case-sensitive (myVar and myvar are different).
#     Avoid using Python keywords (e.g., if, else, for) as variable names.

# Basic Casting Functions
#
#  int() – Converts compatible values to an integer.
#  float() – Transforms values into floating-point numbers.
#  str() – Converts any data type into a string

a = 10
print(a << 2)     # 40

a = 10
b = a
print(b)
b += a
print(b)
b -= a
print(b)
b *= a
print(b)
b <<= a
print(b)         # 102400

# Identity Operators
# is:     True if the operands are identical
# is not:  True if the operands are not identical

a = 10
b = 20
c = a

print(a is not b)
print(a is c)

# Membership Operators
# in True if value is found in the sequence
# not in True if value is not found in the sequence

x = 24
y = 20
list = [10, 20, 30, 40, 50]

if (x not in list):
    print("x is NOT present in given list")
else:
    print("x is present in given list")

if (y in list):
    print("y is present in given list")
else:
    print("y is NOT present in given list")

# Ternary Operators
a, b = 10, 20
min = a if a < b else b
print(min)


# Operator Precedence
expr = 10 + 20 * 30
print(expr)
name = "Alex"
age = 0

if name == "Alex" or name == "John" and age >= 2:
    print("Hello! Welcome.")
else:
    print("Good Bye!!")

# keywords
# print(keyword.kwlist)

# break and continue
# break: break out of the loop and passes the control to the statement following immediately after loop
# continue: skips the current iteration of the loop but does not end the loop.

# 'for' loop example
for num in range(3):
    if num == 2:
        continue  # Skip number 2
    print(num)
# Output: 0 1

# 'while' loop example
count = 0
while count < 4:
    count += 1
    if count == 3:
        break  # Exit the loop when count reaches 4
    print(count)
# Output: 1 2

