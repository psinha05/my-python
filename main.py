print(100)

print('hello')

num1 = 10
num2 = 20

print(num1 + num2)

# variables - not starts with no, no number and special characters
name = 'harsh'
print(name)

age = 22

# single line comment
print(f'user name is {name}')

"""
Here is multi line comments 
"""

price = 54.5
print(f'price is {price}')

mybol= True
print(f'check the condition {mybol}')

# check the type of data
print(type(age))
print(type(price))

print(f'sum of the two numbers are { 10 + 20}')

# how to use the power function in python (like 2^5,  use **)
print(2 ** 5)    #32
print(3 ** 3)    #27

# modules operator
print(10/3)

# in Modulus operator, print only the integer parts, avoid the decimal portions, use double (//)
print(12 //5)

# BODMAS operators , operator precedance
result =  2 * (3 + 4) ** 2 /5 - 6
print(result)

# String Operations: string are immutables
msg = 'Hello Python !'

# lower case
print(msg.lower())

# upper case
print(msg.upper())

# Title : This use as title Camel case
print(msg.title())

# split, this will split the sentences, based on the given conditions and stored in the list
print(msg.split())     # O/p:  ['Hello', 'Python', '!']

# based on condition
msg1 = 'World evolving !, data science is evolution'

print(msg1.split())  # ['World', 'evolving', '!,', 'data', 'science', 'is', 'evolution']
print(msg1.split('!'))    # ['World evolving ', ', data science is evolution '], based on (!)

# print the letter based on index positions
print(msg1[0])  # W

print(msg1[0:5])  # World

print(msg1[0:9])  # World evo

# reverse printing
print(msg1[::-1])   # reverse order of string (noitulove si ecneics atad ,! gnivlove dlroW)

print(msg1[4:1: -1])


msg2 = 'Hello Python'
substring = msg2[8:10]  # Start at index 8 and end at index 10 (exclusive, not included)
print(substring)    # th

# reverse string

substring = msg2[8:]  # Extract the word 'hon'
reversed_substring = substring[::-1]  # Reverse the substring
print(reversed_substring)

substring1 = msg2[::-1]
print(substring1)
