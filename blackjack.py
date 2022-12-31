import os
import random
import blackjack_art


def declare_winner(user, dealer):
    '''
    Compare the user's score to the 
    dealer's score to return a result 
    and declare a winner
    '''
    if user > 21:
        return 'You went over. You lose!'
    elif dealer > 21:
        return 'Opponent went over. You win!'
    elif dealer > user:
        return 'You lose!'
    elif user > dealer:
        return 'You win!'
    elif user == dealer:
        return 'It\'s a draw!'
    else:
        return 'This isn\n working /:'


# Create list of cards in deck.
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
continue_game = True

# Ask the user if they'd like to play a game of Blackjack.
play_a_game = input('\nDo you want to play a game of Blackjack? Type "y" or "n": ').lower()

if play_a_game == 'y':
    os.system('cls')
else:
    print('Goodbye!')
    continue_game = False

while continue_game:
    # Create empty list to represent the user's and dealer's cards in hand.
    user_cards = []
    dealer_cards = []

    print(blackjack_art.logo)

    # Generate 2 random cards to simulate the user's and dealer's first two cards.
    for i in range(0, 2):
        user_random_card = random.choice(cards)
        dealer_random_card = random.choice(cards)

        user_cards.append(user_random_card)
        dealer_cards.append(dealer_random_card)

    # Show the user which cards they have in their hand and their total.
    print(f'\tYour cards: {user_cards}, current score: {sum(user_cards)}')
    # Show the user the first card the dealer had drawn.
    print(f'\tComputer\'s first card: {dealer_cards[0]}')

    # The dealer is forced to take another random card until it's total is 17 or over.
    while sum(dealer_cards) < 17:
        dealer_next_card = random.choice(cards)
        dealer_cards.append(dealer_next_card)

    deal_more_cards = True

    # Ask the user if they want another card as many times they want until their total is over 21.
    while sum(user_cards) < 22 and deal_more_cards:
        deal_another_card = input('Type "y" to get another card, type "n" to pass: ').lower()
            
        if deal_another_card == 'y':
            user_next_card = random.choice(cards)
            user_cards.append(user_next_card)
            print(f'\tYour cards: {user_cards}, current score: {sum(user_cards)}')
            print(f'\tComputer\'s first card: {dealer_cards[0]}')
        else:
            deal_more_cards = False

    user_score = sum(user_cards)
    dealer_score = sum(dealer_cards)

    # Compare the user's and dealer's cards and totals.
    print(f'\tYour final hand: {user_cards}, final_score: {user_score}')
    print(f'\tComputer\'s final hand: {dealer_cards}, final_score: {dealer_score}')

    # Declare the winner.
    print(declare_winner(user=user_score, dealer=dealer_score))

    # Ask the user if they'd like to play another game of Blackjack.
    play_a_game = input('\nDo you want to play a game of Blackjack? Type "y" or "n": ').lower()
    
    if play_a_game == 'y':
        os.system('cls')
    else:
        print('Goodbye!')
        continue_game = False