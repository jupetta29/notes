import os
import random
import higher_lower_game_art as art
import higher_lower_game_data as data


def generate_account():
    '''
    Return and remove a random account from the list of Instagram accounts. 
    '''
    random_position = random.randint(0, len(data.instagram_accounts) - 1)
    account = data.instagram_accounts.pop(random_position)
    return account


def account_details(account, a_or_b):
    '''
    Pull and display the Instagram account details. 
    '''
    name = account['name']
    description = account['description']
    country = account['country']
    print(f'Compare {a_or_b}: {name}, a {description}, from {country}.')


def amount_of_followers(account):
    '''
    Return the Instagram account's amount of followers.
    '''
    followers = account['follower_count']
    return followers


def most_followers(account_a, account_b):
    '''
    Return if 'A' or 'B' has more followers
    '''
    if account_a > account_b:
        return 'a'
    else:
        return 'b'


def new_screen(message):
    '''
    Clear the screen and display the logo with an updated message.
    '''
    os.system('cls')
    print(art.logo)
    print(message)


# Start the game with a clear screen.
os.system('cls')

# Create a variable to toggle if the game ends.
game_active = True
# Create a variable for a scoreboard when the user chooses correctly.
score = 0
# Create a variable with an empty string to later know if they chose correctly or not.
message = ''
# Setup Account A.
account_a = generate_account()

while game_active and len(data.instagram_accounts) > 0:
    new_screen(message)

    # Display 'Compare A'.
    account_details(account_a, 'A')

    # Display 'vs" art.
    print(art.vs)

    # Generate 'Compare B':
    account_b = generate_account()

    # Display 'Compare B'.
    account_details(account_b, 'B')

    # Create variables to compare amount of followers.
    account_a_followers = amount_of_followers(account_a)
    account_b_followers = amount_of_followers(account_b)

    # Ask the user to guess who has more followers.
    user_guess = input('Who has more followers? Type "A" or "B": ').lower()

    if user_guess == most_followers(account_a_followers, account_b_followers):
        # Set the correct answer to be the new 'A'.
        if user_guess == 'b':
            account_a = account_b

        # Increase the score since the user chose correctly.
        score += 1
        # Create a winning message.
        message = f'You\'re right! Current score: {score}'
    else:
        # Create a losing message.
        message = f'Sorry, that\'s wrong. Final score: {score}'

        new_screen(message)
        
        # Toggle the game off.
        game_active = False

# Let the user know they beat the game if there are no more accounts left in the Instagram account list.
if len(data.instagram_accounts) == 0:
    message = f'You beat the game! Score: {score}'
    new_screen(message)