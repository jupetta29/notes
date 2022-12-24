import random

names_string = input('Give me everybody\'s names, separated by a comma. ')

names = names_string.split(', ')
number_of_names = len(names)
random_number = random.randint(0, number_of_names - 1)
loser = names[random_number].capitalize()
message = f'{loser} is going to buy the meal today!'

print(message)