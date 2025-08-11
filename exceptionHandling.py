# Exception Handling Keywords:
# try : in “try” block is checked, if there is any type of error, except block is executed.
#     except : this works with “try” to catch exceptions.
#     finally : No matter what is result of the “try” block, “finally” is always executed.
#     raise: We can raise an exception explicitly with the raise keyword
#     assert: to check the correctness of code. If a statement is evaluated to be true, nothing happens
#     but when it is false, ” AssertionError ” is raised. One can also print a message with the error, separated by a comma


# Case 1 : once divide by 0


print(10 + 2)

print(10 * 2)

try:
    print(10 / 0)
except ZeroDivisionError:
    print('division by 0 is not allowed')

print(10 - 2)


# Case 2: file not found

try:
    with open('user-info.txt', 'r') as file:     # no such file or directory
        info = file.readlines()   # for reading the contents line by line
except FileNotFoundError:
    print("No such file or directory found")
else:
    print(info)  # this info stored in List
finally:
    print('This block must be executed..')

# for handle the generic exception:
try:
    with open('hola.txt') as f:
        context = f.read()
except Exception as e:
    print(e, type(e))

#  multiple exception

a = ["10", "twenty", 30]  # Mixed list of integers and strings
try:
    total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int

except (ValueError, TypeError) as e:
    print("Error", e)

except IndexError:
    print("Index out of range.")

