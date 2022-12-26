print('\nNotes 1\n-------------------------')
# This is a print function.
print()

print('\nNotes 2\n-------------------------')
# These are strings.
print("Hello, World!")
print('Hello, World!')

print('\nNotes 3\n-------------------------')
# This is a new line escape.
print('Hello, World!\nHello, World!')

print('\nNotes 4\n-------------------------')
# This is string concatenation.
print('Hello,' + ' ' + 'World!')

print('\nNotes 5\n-------------------------')
# This is an input function.
# input("What is your name? ")

print('\nNotes 6\n-------------------------')
# This is a length function.
print(len("Hello, World"))

print('\nNotes 7\n-------------------------')
# This is a variable.
name = 'Dylan'
print(name)
name = 'Lily'
print(name)

print('\nNotes 8\n-------------------------')
# Subscript operator on string.
print('Hello, World!'[0])

print('\nNotes 9\n-------------------------')
# This is an integer.
print(123)

print('\nNotes 10\n-------------------------')
# This is an addition operator.
print(123 + 456)

print('\nNotes 11\n-------------------------')
# This is a large integer with underscores for readability.
print(123_456_789)

print('\nNotes 12\n-------------------------')
# This is a float.
print(3.14159)

print('\nNotes 13\n-------------------------')
# These are booleans.
print(True)
print(False)

print('\nNotes 14\n-------------------------')
# This is a type function.
print(type('Hello, World!'))
print(type(123))
print(type(3.14159))
print(type(True))

print('\nNotes 15\n-------------------------')
# This is string conversion.
print(str(123))
print(str(3.14159))
print(str(True))

print('\nNotes 16\n-------------------------')
# This is float conversion.
print(float('123'))
print(float(123))

print('\nNotes 17\n-------------------------')
# This is integer conversion.
print(int('123'))
print(int(3.14159))

print('\nNotes 18\n-------------------------')
# This is subtraction operator.
print(7 - 4)

print('\nNotes 19\n-------------------------')
# This is multiplication operator.
print(3 * 2)

print('\nNotes 20\n-------------------------')
# This is division operator.
print(6 / 3)

print('\nNotes 21\n-------------------------')
# This is exponent operator.
print(2 ** 3)

print('\nNotes 22\n-------------------------')
# This is the round function.
print(round(3.14159))

print('\nNotes 23\n-------------------------')
# This is rounding to a number of spaces.
print(round(3.14159, 3))

print('\nNotes 24\n-------------------------')
# This is floor division operator.
print(8 // 3)

print('\nNotes 25\n-------------------------')
# These are shorthand operators.
score = 3
print(score)
score += 3
print(score)
score -= 3
print(score)
score *= 3
print(score)
score /= 3
print(score)
score **= 4
print(score)
score //= 4
print(score)

print('\nNotes 26\n-------------------------')
# This is an f-string.
score = 0
height = 1.8
is_winning = True
print(f'Your score is {score}, your height is {height} meters, and you are winning is {is_winning}.')

print('\nNotes 27\n-------------------------')
# This is how to force round to a number of decimals places.
print('{:.2f}'.format(12.3456789))

print('\nNotes 28\n-------------------------')
# This is a greater than comparison operator.
print(1 > 0)

print('\nNotes 29\n-------------------------')
# This is an if statement.
x = 0
if 1 > x:
    print('Number 1 is greater than variable x.')
if x > 1:
    print('Variable x is greater than number 1.')

print('\nNotes 30\n-------------------------')
# This is an else statement.
x = 2
if 1 > x:
    print('Number 1 is greater than variable x.')
else:
    print('Variable x is greater than or equal to number 1.')

print('\nNotes 31\n-------------------------')
# This is a greater than or equal to comparison operator.
print(1 >= 1)

print('\nNotes 32\n-------------------------')
# This is a less than comparison operator.
print(1 < 2)

print('\nNotes 33\n-------------------------')
# This is a less than or equal to comparison operator.
print(1 <= 1)

print('\nNotes 34\n-------------------------')
# This is an equal to comparison operator.
print(1 == 1)

print('\nNotes 34\n-------------------------')
# This is a not equal to comparison operator.
print(1 != 2)

print('\nNotes 34\n-------------------------')
# This is a modulo operator.
print(7 % 3)

print('\nNotes 35\n-------------------------')
# This is an elif statement.
x = 5
if x >= 10:
    print('Variable x is greater than or equal to number 10.')
elif x >= 5:
    print('Variable x is greater than or equal to number 5.')
elif x == 5:
    print('Variable x is number 5.')
else:
    print('Variable x is less than number 0.')

print('\nNotes 36\n-------------------------')
# This is an and logical operator.
x = 5
if x > 0 and x < 10:
    print("Variable x is greater than 0 and less than 10.")

print('\nNotes 37\n-------------------------')
# This is an or logical operator.
x = 5
if x == 0 or x == 5:
    print("Variable x is equal to 0 or 5.")

print('\nNotes 38\n-------------------------')
# This is a not logical operator.
x = 5
if not x > 10:
    print("Variable x is not greater than 10.")

print('\nNotes 39\n-------------------------')
# This is the lower function.
name = "DYLAN"
lowercase_name = name.lower()
print(lowercase_name)

print('\nNotes 40\n-------------------------')
# This is the count function.
name = "Dylan Villanueva"
number_of_letter_l = name.count("l")
print(number_of_letter_l)

print('\nNotes 41\n-------------------------')
# This is a multiple line string.
message = """
H
e
l
l
o
"""
print(message)

print('\nNotes 42\n-------------------------')
# These are quotation escapes.
print("You\'re awesome!")
print("He said, \"You're awesome!\"")

print('\nNotes 43\n-------------------------')
# How to import the random module.
import random

print('\nNotes 44\n-------------------------')
# How to make a random integer number with the random module.
random_integer = random.randint(1, 10)
print(random_integer)

print('\nNotes 45\n-------------------------')
# How to import a module.
import module

print('\nNotes 46\n-------------------------')
# How to call from module.
print(module.pi)

print('\nNotes 47\n-------------------------')
# How to make a random floating point number with the random module.
random_float = random.random()
print(random_float)

print('\nNotes 48\n-------------------------')
# How to make a list.
states_of_america = ['Delaware', 'Pennsylvania']
print(states_of_america)

print('\nNotes 49\n-------------------------')
# Subscript operator on list.
print(states_of_america[-1])

print('\nNotes 50\n-------------------------')
# Edit items in list.
states_of_america[-1] = 'Pencilvania'
print(states_of_america)

print('\nNotes 51\n-------------------------')
# Append item to end of list with the append function.
states_of_america.append('New Jersey')
print(states_of_america)

print('\nNotes 52\n-------------------------')
# Add multiple items to end of list with the extend function.
states_of_america.extend(['Georgia', 'Connecticut'])
print(states_of_america)

print('\nNotes 53\n-------------------------')
# Split string into list with the split function.
names = "Jordan, Courtney, Dylan, Licha, Carmen, Aracel"
names_split = names.split(', ')
print(names_split)

print('\nNotes 54\n-------------------------')
# Generate random item from list with the choice function from the random module.
names = ['Jordan', 'Courtney', 'Dylan', 'Licha', 'Carmen', 'Aracel']
random_name = random.choice(names)
print(random_name)

print('\nNotes 55\n-------------------------')
# Use a for loop to itterrate.
fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(f'{fruit} Pie')

print('\nNotes 56\n-------------------------')
# This is the sum function.
points = [0, 1, 2, 3, 4, 5]
total_points = sum(points)
print(total_points)

print('\nNotes 57\n-------------------------')
# This is the max function.
points = [0, 1, 2, 3, 4, 5]
max_points = max(points)
print(max_points)

print('\nNotes 58\n-------------------------')
# This is the min function.
points = [0, 1, 2, 3, 4, 5]
min_points = min(points)
print(min_points)

print('\nNotes 59\n-------------------------')
# This is the range function.
for number in range(0, 101, 10):
    print(number)

print('\nNotes 60\n-------------------------')
# This is the range function.
def print_hello():
    print('Hello!')
print_hello()

print('\nNotes 61\n-------------------------')
# This is a while loop.
x = 1
while x < 6:
    print(f'Hello #{x}!')
    x += 1