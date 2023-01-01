import random
import number_guessing_game_art

# Generate the random number for the user to guess.
random_number = random.randint(1, 100)

# Introduce the user to the game.
print(number_guessing_game_art.logo)
print('Welcome to the Number Guessing Game!')
print('I\'m thinking of a number between 1 and 100.')

# Ask the user to select the game difficulty.
difficulty = input('Choose a difficulty. Type "easy" or "hard": ').lower()

# Adjust the user's amount of guesses according to the difficulty selected.
if difficulty == 'easy':
    number_of_guesses = 10
elif difficulty == 'hard':
    number_of_guesses = 5
else:
    print('Hard it is!')
    number_of_guesses = 5

# Create a variable to toggle to 'True' if the user guesses the correct number.
player_wins = False

# Remove one guess when the user uses a guess wrong.
# Keep the user guessing until they run out of guesses.
while number_of_guesses > 0 and player_wins == False:
    print(f'You have {number_of_guesses} attempts remaining to guess the number.')

    guess = int(input('Make a guess: '))

    if guess == random_number:
        player_wins = True
    elif guess > random_number:
        print('Too high.')
        number_of_guesses -= 1
    elif guess < random_number:
        print('Too low.')
        number_of_guesses -= 1

# Determine if the user won or lost the game.
if number_of_guesses > 0:
    print(f'You got it! The answer was {random_number}.')
else:
    print('You\'ve run out of guesses, you lose!')