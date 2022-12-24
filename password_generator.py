import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')

number_of_letters = int(input('How many letters would you like in your password?\n'))
number_of_numbers = int(input('How many numbers would you like?\n'))
number_of_symbols = int(input('How many symbols would you like?\n'))

password_characters = []

for letter in range(0, number_of_letters):
    random_letter = random.choice(letters)
    password_characters.append(random_letter)

for number in range(0, number_of_numbers):
    random_number = random.choice(numbers)
    password_characters.append(random_number)

for symbol in range(0, number_of_symbols):
    random_symbol = random.choice(symbols)
    password_characters.append(random_symbol)

shuffled_password_list = random.shuffle(password_characters)
password = ''

for character in password_characters:
    password += character

print(password)