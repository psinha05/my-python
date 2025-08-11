import random
from datetime import datetime


def sum(num1, num2):
    return num1 + num2

def sub(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2

def even_or_odd(num):
    if num % 2 ==0:
        print('number is even')
    else:
        print('number is odd')


def main():
    print("This is the main function.")


#  for the __name__ in the python file

if __name__ == "__main__":
    main()



# random number generators

# to generate a random number between 0-1, each time generated the different number 0-1.
print(random.random())

# generate the integer numbers using randomint() function (1-10)
print(random.randint(1, 10))


# to generate a random choice from the list
options = ['apple', 'banana', 'cherry', 'orange', 'date']
print(random.choice(options))

# range of float value b/w the ranges
print(random.uniform(3.5, 6.5))

# shuffle
print(options)
random.shuffle(options)
print(options)


random.randint(1, 6)

while True:
    print(f'random Number generates is', {random.randint(1, 6)})
    user_inputs = input('Do you want to continue Y/N ')
    if user_inputs == 'n':
        break


# use of datetime
curr_date_time = datetime.now()
print(curr_date_time)




# print('*' * 20)

