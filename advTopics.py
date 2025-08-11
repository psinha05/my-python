# a) List Comprehension
# List comprehension allows you to: Condense loops into a single line of code.
# Optionally include conditions to filter items. Create lists efficiently.

# 1). Basic List Comprehension

square = [x**2 for x in range(1, 6)]
print(square)

# 2). List Comprehension with condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)

# 3). List Comprehension with conditional expression
result = [x if x % 2==0 else 'odd' for x in range(1, 11)]
print(result)

# Python Lambda/Anonymous Function: a small, anonymous function that is defined using the lambda keyword
# Key Characteristics of Lambda Functions:
# Anonymous: They don't have a name unless explicitly assigned to a variable.
# Single Line: They are written in a single line, which makes them concise.
# No return keyword: The result is automatically returned from a lambda function, so you don't need to use the return keyword.
# lambda arguments: expression

# a). Basic Lambda Function
add = lambda x, y: x + y
result = add(3, 5)
print(result)

# b). Lambda Function with map(): function used with map(), filter() and reduce() for concise code
numbers = [1, 2, 3, 4, 5]
squ = list(map(lambda x:x**2, numbers))
print(squ)

# c). lambda function with filter
numbs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
myfilter = list(filter (lambda x: x% 2== 0, numbs))
print(myfilter)

# d). Lambda function with sorted
#  use the lambda to sort the tuples by the second elements, lambda pair: pair[1] and sorted()
pairs = [(1, 'apple'), (3, 'banana'), (2, 'cherry')]
pairs_sorted = sorted(pairs, key=lambda pair: pair[1])
print(pairs_sorted)

#e). Lambda function as argument
def apply_function(func, value):
    return func(value)

result = apply_function(lambda x: x**3, 4)
print(result)

print('*'* 30)

# Iterator: an iterator is an object that allows you to traverse through a sequence of elements (like a list, tuple, or string) one at a time
# __iter__(): This method returns the iterator object itself. It is required to make an object iterable.
# __next__(): This method returns the next item in the sequence. When there are no more items to return, it raises a StopIteration exception to signal the end of iteration.
# Iterable: An object that can return an iterator, e.g., a list, tuple, string, or any object that implements the __iter__() method.
#  Iterator: An object that represents a stream of data. It implements the __next__() method to fetch the next item and __iter__()
#  to return the iterator object itself.

# A simple iterable object
numbers = [1, 2, 3, 4, 5]

# Creating an iterator
numbers_iter = iter(numbers)

# Using the iterator to get values
print(next(numbers_iter))  # 1
print(next(numbers_iter))  # 2
print(next(numbers_iter))  # 3
print(next(numbers_iter))  # 4
print(next(numbers_iter))  # 5

# If we call next() again, it will raise StopIteration
# print(next(numbers_iter))  # Uncommenting this will raise StopIteration

print('*'* 30)

# Custom Iterator
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self  # The iterator object is the object itself

    def __next__(self):
        if self.current > self.high:
            raise StopIteration  # When the range is exhausted
        else:
            self.current += 1
            return self.current - 1


# Using the custom iterator
counter = Counter(1, 3)

for num in counter:
    print(num)


# Generators:
# Generators are a type of iterable that allow you to iterate over a sequence of values without creating and storing the entire sequence in memory.
# Generators are implemented using special functions that use the yield keyword to return values one at a time.
# Generators produce values on the fly (one at a time) and do not store the entire sequence in memory.
# Yield, pauses the function’s execution and retains its state. The function can continue from where it left off when called again
# When the generator function is called again, it picks up where it left off, with all its local variables intact.

def my_generator():
    yield 1
    yield 2
    yield 3

# Using the generator
gen = my_generator()

# Retrieving values one at a time using next()
print(next(gen))  # Output: 1
print(next(gen))  # Output: 2
print(next(gen))  # Output: 3

# If we try to call next() again, it will raise StopIteration
# print(next(gen))  # Uncommenting this will raise StopIteration

def my_generator():
    yield 10
    yield 20
    yield 30

# Using a for loop
for value in my_generator():
    print(value)


# Python Decorators: a decorator is a design pattern that allows you to modify the functionality of a function by wrapping it in another function.
# The outer function is called the decorator, which takes the original function as an argument and returns a modified version of it.

def my_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()  # Call the original function
        print("After calling the function.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

# Calling the decorated function
say_hello()
