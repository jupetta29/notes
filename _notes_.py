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
# This is the lower method.
name = "DYLAN"
lowercase_name = name.lower()
print(lowercase_name)

print('\nNotes 40\n-------------------------')
# This is the count method.
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
# import module

print('\nNotes 46\n-------------------------')
# How to call from module.
# print(module.pi)

print('\nNotes 47\n-------------------------')
# How to import and call from module.
# from module import pi
# print(pi)

print('\nNotes 48\n-------------------------')
# How to make a random floating point number with the random module.
random_float = random.random()
print(random_float)

print('\nNotes 49\n-------------------------')
# How to make a list.
states_of_america = ['Delaware', 'Pennsylvania']
print(states_of_america)

print('\nNotes 50\n-------------------------')
# Subscript operator on list.
print(states_of_america[-1])

print('\nNotes 51\n-------------------------')
# Edit items in list.
states_of_america[-1] = 'Pencilvania'
print(states_of_america)

print('\nNotes 52\n-------------------------')
# Append item to end of list with the append method.
states_of_america.append('New Jersey')
print(states_of_america)

print('\nNotes 53\n-------------------------')
# Add multiple items to end of list with the extend method.
states_of_america.extend(['Georgia', 'Connecticut'])
print(states_of_america)

print('\nNotes 54\n-------------------------')
# Split string into list with the split method.
names = "Jordan, Courtney, Dylan, Licha, Carmen, Aracel"
names_split = names.split(', ')
print(names_split)

print('\nNotes 55\n-------------------------')
# Generate random item from list with the choice function from the random module.
names = ['Jordan', 'Courtney', 'Dylan', 'Licha', 'Carmen', 'Aracel']
random_name = random.choice(names)
print(random_name)

print('\nNotes 56\n-------------------------')
# Use a for loop to itterrate.
fruits = ['Apple', 'Peach', 'Pear']
for fruit in fruits:
    print(f'{fruit} Pie')

print('\nNotes 57\n-------------------------')
# This is the sum function.
points = [0, 1, 2, 3, 4, 5]
total_points = sum(points)
print(total_points)

print('\nNotes 58\n-------------------------')
# This is the max function.
points = [0, 1, 2, 3, 4, 5]
max_points = max(points)
print(max_points)

print('\nNotes 59\n-------------------------')
# This is the min function.
points = [0, 1, 2, 3, 4, 5]
min_points = min(points)
print(min_points)

print('\nNotes 60\n-------------------------')
# This is the range function.
for number in range(0, 101, 10):
    print(number)

print('\nNotes 61\n-------------------------')
# This is a custom function.
def print_hello():
    print('Hello!')
print_hello()

print('\nNotes 62\n-------------------------')
# This is a while loop.
x = 1
while x < 6:
    print(f'Hello #{x}!')
    x += 1

print('\nNotes 63\n-------------------------')
# This is a custom function with positional arguments.
def print_hello(name, location):
    print(f'Hello, {name}! What\'s it like in {location}?')
print_hello('Dylan', 'Azle')

print('\nNotes 64\n-------------------------')
# This is a custom function with keyword arguments.
def print_hello(name, location):
    print(f'Hello, {name}! What\'s it like in {location}?')
print_hello(location='Azle', name='Dylan')

print('\nNotes 65\n-------------------------')
# How to import the math module.
import math

print('\nNotes 66\n-------------------------')
# How to round up to nearest integer with the ceil function with the math module.
people = 6.1
print(math.ceil(people))

print('\nNotes 67\n-------------------------')
# Find the index of an item in a list with the index method.
names = ['Jordan', 'Courtney', 'Dylan', 'Licha', 'Carmen', 'Aracel']
print(names.index('Dylan'))

print('\nNotes 68\n-------------------------')
# How to make a dictionary.
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.'
}
print(programming_dictionary)

print('\nNotes 69\n-------------------------')
# How to index a dictionary.
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.'
}
print(programming_dictionary['Bug'])

print('\nNotes 70\n-------------------------')
# How to add new items to dictionary.
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.'
}
programming_dictionary['Loop'] = 'The action of doing something over and over again.'
print(programming_dictionary)

print('\nNotes 71\n-------------------------')
# How to edit an item in a dictionary.
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.'
}
programming_dictionary['Bug'] = 'A moth in your computer.'
print(programming_dictionary)

print('\nNotes 72\n-------------------------')
# How to loop through a dictionary.
programming_dictionary = {
    'Bug': 'An error in a program that prevents the program from running as expected.',
    'Function': 'A piece of code that you can easily call over and over again.'
}
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

print('\nNotes 73\n-------------------------')
# How to nest a list in a dictionary.
travel_log = {
    'France': ['Paris', 'Lille', 'Dijon'],
    'Germany': ['Berlin', 'Hamburg', 'Stuttgart']
}
print(travel_log)

print('\nNotes 74\n-------------------------')
# How to nest a dictionary in a dictionary.
travel_log = {
    'France': {'cities_visited': ['Paris', 'Lille', 'Dijon'], 'total_visits': 12},
    'Germany': {'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'], 'total_visits': 5}
}
print(travel_log)

print('\nNotes 75\n-------------------------')
# How to nest a dictionary in a list.
travel_log = [
    {
        'country': 'France',
        'cities_visited': ['Paris', 'Lille', 'Dijon'],
        'total_visits': 12
    },
    {
        'country': 'Germany',
        'cities_visited': ['Berlin', 'Hamburg', 'Stuttgart'],
        'total_visits': 5
    }
]
print(travel_log)

print('\nNotes 76\n-------------------------')
# How to import the os module.
import os

print('\nNotes 77\n-------------------------')
# How to clear the screen on Windows with the os module.
# os.system('cls')

print('\nNotes 78\n-------------------------')
# How to clear the screen on Linux/OS X with the os module.
# os.system('clear')

print('\nNotes 79\n-------------------------')
# This is a function with an output.
def multiply_numbers(first_number, second_number):
    result = first_number + second_number
    return result
multiplied_numbers_minus_one = multiply_numbers(2, 3) - 1
print(multiplied_numbers_minus_one)

print('\nNotes 80\n-------------------------')
# This is the title method.
formatted_name = 'dylan'.title()
print(formatted_name)

print('\nNotes 81\n-------------------------')
# This is a docstring.
def multiply_numbers(first_number, second_number):
    '''Multiply two numbers together'''
    result = first_number + second_number
    return result

print('\nNotes 82\n-------------------------')
# Store and call function name from dictionary.
def add(n1, n2):
    '''Add'''
    return n1 + n2
def subtract(n1, n2):
    '''Subtract'''
    return n1 - n2
operations = {
    '+': add,
    '-': subtract
}
num1 = 99
num2 = 98
for symbol in operations:
    print(symbol)
# operation_symbol = input('Pick an operation: ')
operation_symbol = '-'
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
result = f'{num1} {operation_symbol} {num2} = {answer}'
print(result)

print('\nNotes 83\n-------------------------')
# This is a tab escape.
print('\tHello, World!')

print('\nNotes 84\n-------------------------')
# This is global vs local scope.
enemies = 1
def increase_enemies():
    enemies = 2
    print(f'Enemies inside function: {enemies}')
increase_enemies()
print(f'Enemies outside function: {enemies}')

print('\nNotes 85\n-------------------------')
# How to modify variable in global scope (NOT SUGGESTED).
enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f'Enemies inside function: {enemies}')
increase_enemies()
print(f'Enemies outside function: {enemies}')

print('\nNotes 86\n-------------------------')
# How to modify variable in global scope (SUGGESTED).
enemies = 1
def increase_enemies():
    return enemies + 1
enemies = increase_enemies()
print(f'Enemies outside function: {enemies}')

print('\nNotes 87\n-------------------------')
# How to make global constants.
PI = 3.14159
URL = 'https://www.google.com'
TWITTER_HANDLE = '@jupetta29'

print('\nNotes 88\n-------------------------')
# How to import the turtle module.
import turtle

print('\nNotes 89\n-------------------------')
# How to make a Turtle object with the Turtle class from the turtle module.
# Class = Blueprint to Create an Object
# Turtle Object = Turtle Module.Turtle Class
# timmy = turtle.Turtle()
# print(timmy)

print('\nNotes 90\n-------------------------')
# How to make a Screen object with the Screen class from the turtle module.
# Screen Object = Turtle Module.Screen Class
# my_screen = turtle.Screen()
# print(my_screen)

print('\nNotes 91\n-------------------------')
# How to access the Canvas Height attribute of a Screen object from the turtle module.
# Object Attribute = Data for an Object
# my_screen = turtle.Screen()
# print(my_screen)
# print(my_screen.canvheight)

print('\nNotes 92\n-------------------------')
# How to use the Exit on Click method of a Screen object from the turtle module.
# Will only close screen when a click is made.
# Object Method = Function for an Object
# my_screen = turtle.Screen()
# print(my_screen)
# my_screen.exitonclick()

print('\nNotes 93\n-------------------------')
# How to use the Shape method of a Turtle object from the turtle module.
# Will change the shape of the Turtle object.
# Object Method = Function for an Object
# timmy = turtle.Turtle()
# print(timmy)
# timmy.shape('turtle')

# my_screen = turtle.Screen()
# print(my_screen)

# my_screen.exitonclick()

print('\nNotes 94\n-------------------------')
# How to use the Color method of a Turtle object from the turtle module.
# Will change the color of the Turtle object.
# Object Method = Function for an Object
# timmy = turtle.Turtle()

# timmy.shape('turtle')
# timmy.color('coral')

# my_screen = turtle.Screen()

# my_screen.exitonclick()

print('\nNotes 95\n-------------------------')
# How to use the Forward method of a Turtle object from the turtle module.
# Will move the Turtle object forward.
# Object Method = Function for an Object
# timmy = turtle.Turtle()

# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)

# my_screen = turtle.Screen()

# my_screen.exitonclick()

print('\nNotes 96\n-------------------------')
# How to import the PrettyTable package.
# Install 'prettytable' in virtual environment.
# cmd: pip install prettytable
import prettytable

print('\nNotes 97\n-------------------------')
# How to make a Table object with the PrettyTable class from the prettytable package.
# Class = Blueprint to Create an Object
# Table Object = prettytable Module.PrettyTable Class
table = prettytable.PrettyTable()

print(table)

print('\nNotes 98\n-------------------------')
# How to use the Field Names method of a PrettyTable object from the prettytable package.
# The Field Names method adds a table header with a list of items.
# Object Method = Function for an Object
table = prettytable.PrettyTable()

table.field_names = ['Pokémon Name', 'Type']
print(table)

print('\nNotes 99\n-------------------------')
# How to use the Add Row method of a PrettyTable object from the prettytable package.
# The Add Row method adds a new row with a list of items.
# Object Method = Function for an Object
table = prettytable.PrettyTable()

table.field_names = ['Pokémon Name', 'Type']
table.add_row(['Bulbasaur', 'Grass, Poison'])
table.add_row(['Charmander', 'Fire'])
table.add_row(['Squirtle', 'Water'])
table.add_row(['Pikachu', 'Electric'])

print(table)

print('\nNotes 100\n------------------------')
# How to use the Add Column method of a PrettyTable object from the prettytable package.
# The Add Column method adds a new table header for the column with a list of items in the column.
# Object Method = Function for an Object
table = prettytable.PrettyTable()

table.add_column('Pokémon Name', ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu'])
table.add_column('Type', ['Grass, Poison', 'Fire', 'Water', 'Electric'])

print(table)

print('\nNotes 101\n------------------------')
# How to access and edit the Canvas Height attributes of a Screen object from the turtle module.
# Object Attribute = Data for an Object
table = prettytable.PrettyTable()

table.add_column('Pokémon Name', ['Bulbasaur', 'Charmander', 'Squirtle', 'Pikachu'])
table.add_column('Type', ['Grass, Poison', 'Fire', 'Water', 'Electric'])
table.align = 'l'

print(table)
print(table.align)

print('\nNotes 102\n------------------------')
# How to make an empty function.
def function():
    pass


function()

print('\nNotes 103\n------------------------')
# How to create a class.
class User:
    pass


user_1 = User()

print('\nNotes 104\n-------------------------')
# How to create an attribute to a class.
class User:
    pass


user_1 = User()

user_1.id = '001'
user_1.username = 'Dylan'

print(f'User ID: {user_1.id}, Username: {user_1.username}')

print('\nNotes 105\n------------------------')
# How to create a default constructor to a class.
class User:
    
    def __init__(self):
        print('new user being created...')


user_1 = User()

user_1.id = '001'
user_1.username = 'Dylan'

print(f'User ID: {user_1.id}, Username: {user_1.username}')

user_2 = User()

user_2.id = '002'
user_2.username = 'Elena'

print(f'User ID: {user_2.id}, Username: {user_2.username}')

print('\nNotes 106\n------------------------')
# How to create a parameterized constructor to a class.
class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0


user_1 = User('001', 'Dylan')

print(f'User ID: {user_1.id}, Username: {user_1.username}, Followers: {user_1.followers}')

user_2 = User('002', 'Elena')

print(f'User ID: {user_2.id}, Username: {user_2.username}, Followers: {user_2.followers}')

print('\nNotes 107\n------------------------')
# How to create a method to a class.
class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.following = 0
        self.followers = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1
        print(f'{self.username} just followed {user.username}!')


user_1 = User('001', 'Dylan')

print(f'User ID: {user_1.id}, Username: {user_1.username}, Following: {user_1.following}, Followers: {user_1.followers}')

user_2 = User('002', 'Elena')

print(f'User ID: {user_2.id}, Username: {user_2.username}, Following: {user_2.following}, Followers: {user_2.followers}')

user_1.follow(user_2)

print(f'User ID: {user_1.id}, Username: {user_1.username}, Following: {user_1.following}, Followers: {user_1.followers}')
print(f'User ID: {user_2.id}, Username: {user_2.username}, Following: {user_2.following}, Followers: {user_2.followers}')

print('\nNotes 108\n------------------------')
# How to use the Right method of a Turtle object from the turtle module.
# Will turn the Turtle object right by a certain amount of degrees.
# Object Method = Function for an Object
# timmy = turtle.Turtle()

# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
# timmy.right(90)

# my_screen = turtle.Screen()

# my_screen.exitonclick()

print('\nNotes 109\n------------------------')
# How to use the Left method of a Turtle object from the turtle module.
# Will turn the Turtle object right by a certain amount of degrees.
# Object Method = Function for an Object
# tim = turtle.Turtle()

# tim.shape('turtle')
# tim.color('coral')
# tim.forward(100)
# tim.left(90)

# my_screen = turtle.Screen()

# my_screen.exitonclick()

print('\nNotes 110\n------------------------')
# How to import everything from a module.
# tim = turtle.Turtle()

# tim.shape('turtle')
# tim.color('coral')
# tim.forward(100)
# tim.left(90)

# my_screen = turtle.Screen()

# my_screen.exitonclick()

print('\nNotes 111\n------------------------')
# How to import everything from module.
# from module import *
# print(pi)

print('\nNotes 112\n------------------------')
# How to import a module with an alias.
# import module as m
# print(m.pi)

print('\nNotes 113\n------------------------')
# How to import the Heroes package.
# Install 'heroes' in virtual environment.
# cmd: pip install heroes
import heroes

print('\nNotes 114\n------------------------')
# How to use the Gen function from the Heroes package.
# The Gen function generates a random hero name.
hero_name = heroes.gen()

print(hero_name)

print('\nNotes 115\n------------------------')
# How to use the Pen Up method of a Turtle object from the turtle module.
# Will lift up the pen on the Turtle object.
# Object Method = Function for an Object
# tim = turtle.Turtle()

# tim.forward(10)
# tim.penup()
# tim.forward(10)

# screen = turtle.Screen()

# screen.exitonclick()

print('\nNotes 116\n------------------------')
# How to use the Pen Down method of a Turtle object from the turtle module.
# Will put down the pen on the Turtle object.
# Object Method = Function for an Object
# tim = turtle.Turtle()

# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# screen = turtle.Screen()

# screen.exitonclick()

print('\nNotes 117\n------------------------')
# How to use the Set Heading method of a Turtle object from the turtle module.
# Will set the orientation of the Turtle object.
# Object Method = Function for an Object
# tim = turtle.Turtle()

# tim.setheading(90)

# screen = turtle.Screen()

# screen.exitonclick()

print('\nNotes 118\n------------------------')
# How to use the Pen Size method of a Turtle object from the turtle module.
# Will set the pen size of the Turtle object.
# Object Method = Function for an Object
# tim = turtle.Turtle()

# tim.pensize(10)
# tim.forward(100)

# screen = turtle.Screen()

# screen.exitonclick()

print('\nNotes 119\n------------------------')
# How to use the Speed method of a Turtle object from the turtle module.
# Will set the speed of the Turtle object.
# Object Method = Function for an Object
# tim = turtle.Turtle()

# tim.speed('fastest')

# for i in range(10):
#     tim.right(90)
#     tim.forward(25)

# screen = turtle.Screen()

# screen.exitonclick()

print('\nNotes 120\n------------------------')
# This is a tuple.
# Tuples are immutable.
my_tuple = (1, 3, 8)

print('\nNotes 121\n------------------------')
# This is how to index a tuple.
# Tuples are immutable.
my_tuple = (1, 3, 8)
print(my_tuple[0])

print('\nNotes 122\n------------------------')
# This is set the Color Mode of the turtle module.
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color


# turtle.colormode(255)

# tim = turtle.Turtle()
# tim.pensize(10)
# tim.speed(0)
# tim.color(random_color())

# screen = turtle.Screen()
# screen.exitonclick()

print('\nNotes 123\n------------------------')
# How to use the Circle method of a Turtle object from the turtle module.
# Will have the Turtle object draw a circle.
# Object Method = Function for an Object
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# turtle.colormode(255)
# tim = turtle.Turtle()
# tim.speed(0)

# for i in range(0, 36):
#     tim.color(random_color())
#     tim.setheading(i * 10)
#     tim.circle(100)

# screen = turtle.Screen()
# screen.exitonclick()

print('\nNotes 124\n------------------------')
# How to use the Heading method of a Turtle object from the turtle module.
# Will retrieve the heading position of the Turtle object.
# Object Method = Function for an Object
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color


# turtle.colormode(255)
# tim = turtle.Turtle()
# tim.speed(0)

# heading = tim.heading()
# print(heading)

# for i in range(0, 36):
#     tim.color(random_color())
#     tim.setheading(i * 10)
#     tim.circle(100)

# heading = tim.heading()
# print(heading)

# screen = turtle.Screen()
# screen.exitonclick()

print('\nNotes 124\n------------------------')
# How to import the Colorgram package.
# Install 'colorgram.py' in virtual environment.
# cmd: pip install colorgram.py
import colorgram

print('\nNotes 125\n------------------------')
# How to use the Extract function from the Colorgram package.
# Use the Extract function to extract the most used colors from an image source into a list of Color objects.
# colors = colorgram.extract('notes/kirby.png', 6)
# print(colors)

print('\nNotes 126\n------------------------')
# How to use the RGB method from the Colorgram package.
# Use the RGB method to extract the RGB from the Color object.
# colors = colorgram.extract('notes/kirby.png', 6)

# color1 = colors[0]
# color1_rgb = color1.rgb
# print(color1_rgb)

print('\nNotes 127\n------------------------')
# How to use the RGB method from the Colorgram package.
# Use the RGB method to extract the RGB from the Color object.
# colors = colorgram.extract('notes/kirby.png', 6)

# color1 = colors[0]
# color1_hsl = color1.hsl
# print(color1_hsl)

print('\nNotes 128\n------------------------')
# How to use the Proportion method from the Colorgram package.
# Use the Proportion method on the Color object to extract what proportion was that color.
# colors = colorgram.extract('notes/kirby.png', 6)

# color1 = colors[0]
# color1_proportion = color1.proportion
# print(color1_proportion)

print('\nNotes 129\n------------------------')
# How to use the R method from the Colorgram package.
# Use the R method to extract the RGB Red value from the Color object.
# colors = colorgram.extract('notes/kirby.png', 6)

# color1_red = colors[0].rgb.r
# print(color1_red)

print('\nNotes 130\n------------------------')
# How to use the G method from the Colorgram package.
# Use the G method to extract the RGB Green value from the Color object.
# colors = colorgram.extract('notes/kirby.png', 6)

# color1_red = colors[0].rgb.r
# color1_green = colors[0].rgb.g
# print(color1_green)

print('\nNotes 131\n------------------------')
# How to use the B method from the Colorgram package.
# Use the B method to extract the RGB Blue value from the Color object.
# colors = colorgram.extract('notes/kirby.png', 6)

# color1_red = colors[0].rgb.r
# color1_green = colors[0].rgb.g
# color1_blue = colors[0].rgb.b
# print(color1_blue)

# color1_rgb = (color1_red, color1_green, color1_blue)
# print(color1_rgb)

print('\nNotes 132\n------------------------')
# How to use the Dot method of a Turtle object from the turtle module.
# Will have the Turtle object make a dot.
# Object Method = Function for an Object
# screen = turtle.Screen()

# tim = turtle.Turtle()
# tim.penup()

# for i in range(5):
#     tim.dot(20, 'Blue')
#     tim.forward(50)

# screen.exitonclick()

print('\nNotes 133\n------------------------')
# How to use the Hide Turtle method of a Turtle object from the turtle module.
# Will hide the Turtle object from being displayed.
# Object Method = Function for an Object
# screen = turtle.Screen()

# tim = turtle.Turtle()
# tim.hideturtle()
# tim.penup()

# for i in range(5):
#     tim.dot(20, 'Blue')
#     tim.forward(50)

# screen.exitonclick()

print('\nNotes 134\n------------------------')
# How to use the Listen method of a Screen object from the turtle module.
# Will set focus on the Screen object to start listening for events.
# Object Method = Function for an Object
# screen = turtle.Screen()
# tim = turtle.Turtle()

# screen.listen()
# screen.exitonclick()

print('\nNotes 135\n------------------------')
# How to use the On Key method of a Screen object from the turtle module.
# Will start listening for on key events with the 'key' parameter.
# Will respond with a function when the key event is triggered.
# Object Method = Function for an Object
# screen = turtle.Screen()
# tim = turtle.Turtle()

# def move_forwards():
#     tim.forward(10)

# screen.listen()
# screen.onkey(key='space', fun=move_forwards)
# screen.exitonclick()

print('\nNotes 136\n------------------------')
# How to use the On Key Press method of a Screen object from the turtle module.
# Will start listening for on key press events with the 'key' parameter.
# Will respond with a function when the key event is triggered.
# Object Method = Function for an Object
# def move_forwards():
#     tim.forward(10)


# tim = turtle.Turtle()
# screen = turtle.Screen()

# screen.listen()
# screen.onkeypress(key='w', fun=move_forwards)
# screen.exitonclick()

print('\nNotes 137\n------------------------')
# How to use the Backward method of a Screen object from the turtle module.
# Will move the Turtle object backward.
# Object Method = Function for an Object
# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# tim = turtle.Turtle()
# screen = turtle.Screen()

# screen.listen()
# screen.onkeypress(key='w', fun=move_forwards)
# screen.onkeypress(key='s', fun=move_backwards)
# screen.exitonclick()

print('\nNotes 138\n------------------------')
# How to use the Right method of a Screen object from the turtle module.
# Will move the Turtle object right.
# Object Method = Function for an Object
# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# def move_clockwise():
#     tim.right(10)


# tim = turtle.Turtle()
# screen = turtle.Screen()

# screen.listen()
# screen.onkeypress(key='w', fun=move_forwards)
# screen.onkeypress(key='s', fun=move_backwards)
# screen.onkeypress(key='d', fun=move_clockwise)
# screen.exitonclick()

print('\nNotes 139\n------------------------')
# How to use the Left method of a Screen object from the turtle module.
# Will move the Turtle object left.
# Object Method = Function for an Object
# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# def move_clockwise():
#     tim.right(10)


# def move_counter_clockwise():
#     tim.left(10)


# tim = turtle.Turtle()
# screen = turtle.Screen()

# screen.listen()
# screen.onkeypress(key='w', fun=move_forwards)
# screen.onkeypress(key='s', fun=move_backwards)
# screen.onkeypress(key='d', fun=move_clockwise)
# screen.onkeypress(key='a', fun=move_counter_clockwise)
# screen.exitonclick()

print('\nNotes 140\n------------------------')
# How to use the Clear method of a Turtle object from the turtle module.
# Will clear the drawing from the Turtle object.
# Object Method = Function for an Object
# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# def move_clockwise():
#     tim.right(10)


# def move_counter_clockwise():
#     tim.left(10)

# def clear():
#     tim.clear()


# tim = turtle.Turtle()
# screen = turtle.Screen()

# screen.listen()
# screen.onkeypress(key='w', fun=move_forwards)
# screen.onkeypress(key='s', fun=move_backwards)
# screen.onkeypress(key='d', fun=move_clockwise)
# screen.onkeypress(key='a', fun=move_counter_clockwise)
# screen.onkeypress(key='c', fun=clear)
# screen.exitonclick()

print('\nNotes 141\n------------------------')
# How to use the Home method of a Turtle object from the turtle module.
# Will move the Turtle object to the center of the Screen object.
# Object Method = Function for an Object
# def move_forwards():
#     tim.forward(10)


# def move_backwards():
#     tim.backward(10)


# def move_clockwise():
#     tim.right(10)


# def move_counter_clockwise():
#     tim.left(10)

# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()


# tim = turtle.Turtle()
# screen = turtle.Screen()

# screen.listen()
# screen.onkeypress(key='w', fun=move_forwards)
# screen.onkeypress(key='s', fun=move_backwards)
# screen.onkeypress(key='d', fun=move_clockwise)
# screen.onkeypress(key='a', fun=move_counter_clockwise)
# screen.onkeypress(key='c', fun=clear)
# screen.exitonclick()

print('\nNotes 142\n------------------------')
# How to use the Setup method of a Screen object from the turtle module.
# Will set up the width and height respectively of the Screen object.
# Object Method = Function for an Object
# tim = turtle.Turtle()

# screen = turtle.Screen()
# screen.setup(width=500, height=400)
# screen.exitonclick()

print('\nNotes 143\n------------------------')
# How to use the Text Input method of a Screen object from the turtle module.
# Will pop up a Text Input on the Screen object.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(500, 400)
# user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

# tim = turtle.Turtle()

# screen.exitonclick()

print('\nNotes 144\n------------------------')
# How to use the Go To method of a Turtle object from the turtle module.
# Will have the Turtle object go to specific x and y coordinates.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(500, 400)
# user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

# tim = turtle.Turtle()
# tim.goto(x=-230, y=-100)

# screen.exitonclick()

print('\nNotes 145\n------------------------')
# How to use the X Coordinate method of a Turtle object from the turtle module.
# Will extract the x coordinate of the Turtle object.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(500, 400)
# user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

# tim = turtle.Turtle()
# tim.goto(x=-230, y=-100)
# x_cor = tim.xcor()
# print(x_cor)

# screen.exitonclick()

print('\nNotes 146\n------------------------')
# How to use the Pen Color method of a Turtle object from the turtle module.
# Will set or extract the Pen Color of the Turtle object.
# Object Method = Function for an Object
# is_race_on = False
# screen = turtle.Screen()
# screen.setup(500, 400)
# user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')
# colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# y_positions = [-70, -40, -10, 20, 50, 80]
# all_turtles = []

# for turtle_index in range(0, 6):
#     new_turtle = turtle.Turtle(shape='turtle')
#     new_turtle.color(colors[turtle_index])
#     new_turtle.penup()
#     new_turtle.goto(x=-230, y=y_positions[turtle_index])
#     all_turtles.append(new_turtle)

# if user_bet:
#     is_race_on = True

# while is_race_on:
#     for turtle in all_turtles:
#         if turtle.xcor() > 230:
#             is_race_on = False
#             winning_color = turtle.pencolor()
#             if winning_color == user_bet:
#                 print(f'You\'ve won! The {winning_color} turtle is the winner!')
#             else:
#                 print(f'You\'ve lost! The {winning_color} turtle is the winner!')
#         random_distance = random.randint(0, 10)
#         turtle.forward(random_distance)


# screen.exitonclick()

print('\nNotes 147\n------------------------')
# How to use the Background Color method of a Screen object from the turtle module.
# Will set the background color of the Screen object.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.exitonclick()

print('\nNotes 148\n------------------------')
# How to use the Title method of a Screen object from the turtle module.
# Will set the title of the Screen object.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.exitonclick()

print('\nNotes 149\n------------------------')
# How to use the Tracer method of a Screen object from the turtle module.
# Will turn animation on or off and set delay for update drawings.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for position in starting_positions:
#     new_segment = turtle.Turtle('square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

# game_is_on = True

# while game_is_on:
#     for seg in segments:
#         seg.forward(20)
#     game_is_on = False

# screen.exitonclick()

print('\nNotes 150\n------------------------')
# How to use the Update method of a Screen object from the turtle module.
# Will update the animation for drawings.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for position in starting_positions:
#     new_segment = turtle.Turtle('square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

# screen.update()

# game_is_on = True

# while game_is_on:
#     for seg in segments:
#         seg.forward(20)
#     game_is_on = False

# screen.exitonclick()

print('\nNotes 151\n------------------------')
# How to import the time module.
import time

print('\nNotes 152\n------------------------')
# How to use the sleep function from the time module.
# Will have the program sleep for a certain amount of seconds.
# screen = turtle.Screen()
# screen.setup(width=600, height=600)
# screen.bgcolor('black')
# screen.title('Snake Game')
# screen.tracer(0)

# starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# segments = []

# for position in starting_positions:
#     new_segment = turtle.Turtle('square')
#     new_segment.color('white')
#     new_segment.penup()
#     new_segment.goto(position)
#     segments.append(new_segment)

# screen.update()

# game_is_on = True

# while game_is_on:
#     for seg in segments:
#         seg.forward(20)
#         screen.update()
#         time.sleep(1)
#     game_is_on = False

# screen.exitonclick()

print('\nNotes 153\n------------------------')
# How to use the Y Coordinate method of a Turtle object from the turtle module.
# Will extract the y coordinate of the Turtle object.
# Object Method = Function for an Object
# screen = turtle.Screen()
# screen.setup(500, 400)
# user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

# tim = turtle.Turtle()
# tim.goto(x=-230, y=-100)
# y_cor = tim.ycor()
# print(y_cor)

# screen.exitonclick()

print('\nNotes 154\n------------------------')
# How to use class inheritance.
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breath(self):
#         print('Inhale, exhale')

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()

#     def swim(self):
#         print('moving in water.')
    
# nemo = Fish()
# nemo.swim()
# nemo.breath()
# print(nemo.num_eyes)

print('\nNotes 155\n------------------------')
# How to modify class inheritance.
# class Animal:
#     def __init__(self):
#         self.num_eyes = 2

#     def breath(self):
#         print('Inhale, exhale')

# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
    
#     def breath(self):
#         super().breath()
#         print('doing this underwater.')

#     def swim(self):
#         print('moving in water.')
    
# nemo = Fish()
# nemo.swim()
# nemo.breath()
# print(nemo.num_eyes)

print('\nNotes 156\n------------------------')
# How to use the Shape Size method of a Turtle object from the turtle module.
# Will reshape the length and width of a Turtle object.
# Object Method = Function for an Object
# screen = turtle.Screen()

# tim = turtle.Turtle()
# tim.shapesize(stretch_len=5, stretch_wid=5)

# screen.exitonclick()

print('\nNotes 157\n------------------------')
# How to use the Distance method of a Turtle object from the turtle module.
# Will return a Turtle object's distance from another Turtle object.
# Object Method = Function for an Object
# screen = turtle.Screen()

# tim = turtle.Turtle()
# tim.goto(0, 0)
# tom = turtle.Turtle()
# tom.goto(10, 10)

# distance_from_each = tim.distance(tom)
# print(distance_from_each)

# screen.exitonclick()

print('\nNotes 158\n------------------------')
# How to use the Write method of a Turtle object from the turtle module.
# Will write text at the position of a Turtle object.
# Object Method = Function for an Object
# screen = turtle.Screen()

# tim = turtle.Turtle()
# tim.write('HELLO!', align='center', font=('Arial', 24, 'normal'))
# tim.hideturtle()

# screen.exitonclick()

print('\nNotes 159\n------------------------')
# How to use the Clear method of a Turtle object from the turtle module.
# Will clear the Turtle object's drawings from the screen.
# Object Method = Function for an Object
# screen = turtle.Screen()

# tim = turtle.Turtle()
# tim.hideturtle()
# tim.penup()
# tim.write('HELLO #1!', align='center', font=('Arial', 24, 'normal'))
# tim.clear()
# tim.setheading(270)
# tim.forward(100)
# tim.write('HELLO! #2', align='center', font=('Arial', 24, 'normal'))

# screen.exitonclick()

print('\nNotes 160\n------------------------')
# How to slice.
piano_keys = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])
print(piano_keys[2:5:2])
print(piano_keys[::2])
print(piano_keys[::-1])

piano_tuple = ('do', 're', 'mi', 'fa', 'so', 'la', 'ti', 'do')
print(piano_tuple[2:5])

piano_string = 'abcdefg'
print(piano_string[2:5])

print('\nNotes 161\n------------------------')
# How to use the open function to open a file.
# file = open('file.txt')

print('\nNotes 162\n------------------------')
# How to use the read method to read a file.
# The default mode for the open function is 'read'.
# file = open('file.txt')
# contents = file.read()
# print(contents)

print('\nNotes 163\n------------------------')
# How to use the close function to close a file.
# file = open('file.txt')
# contents = file.read()
# print(contents)
# file.close()

print('\nNotes 164\n------------------------')
# How to use the with open function to open and close a file.
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

print('\nNotes 165\n------------------------')
# How to use the write method to write to a file.
# If a file isn't existent during 'w' mode, the 'w' mode will create the file.
# with open('my_file.txt', mode='w') as file:
#     file.write('New text.')

print('\nNotes 166\n------------------------')
# How to use the append mode on the open function to add text to a file.
# with open('my_file.txt', mode='a') as file:
#     file.write('\nNew text.')

print('\nNotes 166\n------------------------')
# How to make a raw string to ignore 'escape' characters.
# with open(r"C:\Users\jupet\Desktop\data.txt", mode='w') as file:
#     file.write('\nNew text.')

print('\nNotes 167\n------------------------')
# How to use a filepath that will work on Windows and Mac.
# The '/' will represent the root directory.
# with open("/Users/jupet/Desktop/data.txt", mode='w') as file:
#     file.write('New text.\nNext line of text.')

print('\nNotes 168\n------------------------')
# How to move up two directories with '../'.
# with open("../../data.txt", mode='r') as file:
#     content = file.read()
#     print(content)

print('\nNotes 169\n------------------------')
# How to use the read lines method on a file.
# Returns a list contaiing each line in the file as a list item.
# with open("/Users/jupet/Desktop/data.txt", mode='r') as file:
#     content = file.readlines()
#     print(content)

print('\nNotes 170\n------------------------')
# How to use the strip method.
# Strips a specified phrase from a string.
# message = 'Hello, [name]!\nHope you\'re doing well!\nHave a good day,\nDylan'

# with open("/Users/jupet/Desktop/data.txt", mode='r') as file:
#     names = file.readlines()
# for name in names:
#     new_name = name.strip('\n')
#     print(new_name)

print('\nNotes 171\n------------------------')
# How to use the replace method.
# Replaces a specified phrase with another specified phrase.
# message = 'Hello, [name]\n\nHope you\'re doing well!\n\nHave a good day,\nDylan'

# with open("/Users/jupet/Desktop/data.txt", mode='r') as file:
#     names = file.readlines()
# for name in names:
#     name = name.strip('\n')
#     new_message = message.replace('[name]', name)
#     filename = f'letter_for_{name}.txt'
#     with open(f'/Users/jupet/Desktop/{filename}', 'w') as file:
#         file.write(new_message)

print('\nNotes 172\n------------------------')
# How to import the csv module.
import csv

print('\nNotes 173\n------------------------')
# How to use the reader method from the csv module.
# with open('weather_data.csv') as file:
#     data = csv.reader(file)
#     for row in data:
#         print(row)

print('\nNotes 174\n------------------------')
# How to import the pandas module.
# 'pip install pandas' in Terminal.
import pandas

print('\nNotes 175\n------------------------')
# How to use the read_csv method to make a data frame in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# print(data)

print('\nNotes 176\n------------------------')
# How to index a column series in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# print(data['temp'])

print('\nNotes 177\n------------------------')
# How to convert a data frame into a dictionary in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# data_dict = data.to_dict()
# print(data_dict)

print('\nNotes 178\n------------------------')
# How to convert a series to a list in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# temp_list = data['temp'].to_list()
# print(temp_list)

print('\nNotes 179\n------------------------')
# How to use the mean method to find the mean of a series in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# temp_mean = data['temp'].mean()
# print(temp_mean)

print('\nNotes 180\n------------------------')
# How to use the max method to find the mean of a series in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# temp_max = data['temp'].max()
# print(temp_max)

print('\nNotes 181\n------------------------')
# How to use the column or series name to select a column in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# print(data.day)
# print(data.temp)
# print(data.condition)

print('\nNotes 182\n------------------------')
# How to get data from a row in the pandas module.
# data = pandas.read_csv('weather_data.csv')
# monday_row = data[data.day == 'Monday']
# print(monday_row)

print('\nNotes 183\n------------------------')
# How to create a Data Frame from scratch in the pandas module.
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'], 
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

print('\nNotes 184\n------------------------')
# How to convert a Data Frame to a csv file in the pandas module.
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'], 
#     'scores': [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv('new_data.csv')

print('\nNotes 185\n------------------------')
# How to use the item method in the pandas module to grab the first item.
# data = pandas.read_csv('weather_data.csv')
# print(data.day)
# print(data.temp)
# print(data.condition)
# print(data.day.item())

print('\nNotes 186\n------------------------')
# How to use list comprehension on a list to create a list.
# List comprehensions work with sequences like: list, range, string, tuple
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

print('\nNotes 187\n------------------------')
# How to use list comprehension on a string to create a list.
name = 'Dylan'
letters_list = [letter for letter in name]
print(letters_list)

print('\nNotes 188\n------------------------')
# How to use list comprehension on a range to create a list.
range_list = [n * 2 for n in range(1, 5)]
print(range_list)

print('\nNotes 189\n------------------------')
# How to use conditional list comprehension.
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# short_names = [name for name in names if len(name) <= 4]
# print(short_names)
# upper_long_names = [name.upper() for name in names if len(name) >= 5]
# print(upper_long_names)
# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# squared_numbers = [n ** 2 for n in numbers]
# print(squared_numbers)
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

print('\nNotes 190\n------------------------')
# How to use dictionary comprehension with a list to create a dictionary.
# Dicitionary comprehensions work with sequences like: list, range, string, tuple
import random
# names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
# students_scores = {student:random.randint(1, 100) for student in names}
# print(students_scores)

print('\nNotes 191\n------------------------')
# How to use the items method on a dictionary to retrieve items.
# Dicitionary comprehensions work with sequences like: list, range, string, tuple
names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

print('\nNotes 192\n------------------------')
# How to use the split method to convert a string into a list.
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)

print('\nNotes 193\n------------------------')
# How to iterate over a row from pandas DataFrame.
# student_dict = {
#     'student': ['Dylan', 'Chris', 'Caelan'], 
#     'score': [56, 76, 98]
# }
# # Original way of looping through dictionaries.
# # for (key, value) in student_dict.items():
# #     print(value)

import pandas

# student_data_frame = pandas.DataFrame(student_dict)
# # print(student_data_frame)

# # Loop through rows of a DataFrame to create a Series.
# for (index, row) in student_data_frame.iterrows():
#     print(row)

print('\nNotes 194\n------------------------')
# How to iterate over a row from pandas DataFrame.
# student_dict = {
#     'student': ['Dylan', 'Chris', 'Caelan'], 
#     'score': [56, 76, 98]
# }

# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

# # Loop through rows and specific column of a DataFrame to create a Series.
# for (index, row) in student_data_frame.iterrows():
#     print(row.student)
#     print(row.score)

print('\nNotes 195\n------------------------')
# How to import tkinter.
import tkinter

print('\nNotes 196\n------------------------')
# How to create a window with the TK class in the tkinter module.
# window = tkinter.Tk()

print('\nNotes 197\n------------------------')
# How to use the mainloop method to keep the gui running in the tkinter module.
# window = tkinter.Tk()
# window.mainloop()

print('\nNotes 198\n------------------------')
# How to use the title method to give a title to the gui in the tkinter module.
# window = tkinter.Tk()
# window.title('My First GUI Program')
# window.mainloop()

print('\nNotes 199\n------------------------')
# How to use the minsize method to give the minimum size to the gui in the tkinter module.
# window = tkinter.Tk()
# window.title('My First GUI Program')
# window.minsize(width=500, height=300)

# window.mainloop()

print('\nNotes 200\n------------------------')
# How to use the Label class to create a label in the tkinter module.
# window = tkinter.Tk()
# window.title('My First GUI Program')
# window.minsize(width=500, height=300)

# my_label = tkinter.Label(text='I am a Label', font=('Arial', 24, 'bold'))

# window.mainloop()

print('\nNotes 201\n------------------------')
# How to use the pack method to place a label on the gui in the tkinter module.
# window = tkinter.Tk()
# window.title('My First GUI Program')
# window.minsize(width=500, height=300)

# my_label = tkinter.Label(text='I am a Label', font=('Arial', 24, 'bold'))
# my_label.pack(side='left')

# window.mainloop()

print('\nNotes 202\n------------------------')
# How to define a function with unlimited positional arguments.
# Unlimited args data type is a tuple.
def add(*args):
    # print(args[0])
    numbers = sum([n for n in args])
    return numbers
print(add(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
