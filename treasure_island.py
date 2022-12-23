print('Welcome to Treasure Island.\nYour mission is to find the treasure.')

choice_1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right".\n').lower()
if choice_1 == 'left':
    choice_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.\n').lower()
    if choice_2 == 'wait':
        choice_3 = input('You arrive to the island unharmed. There is a house with 3 doors. One red, one yellow, and one blue. Which color do you choose?\n').lower()
        if choice_3 == 'yellow':
            print('You found the treasure! You Win!')
        elif choice_3 == 'red':
            print('It\'s a room full of fire. Game Over.')
        elif choice_3 == 'blue':
            print('You enter a room of beasts. Game Over.')
    elif choice_2 == 'swim':
        print('You got attacked by an angry trout. Game Over.')
    else:
        print('That\'s not an option. Game Over.')
elif choice_1 == 'right':
    print('You fell into a hole. Game Over.')
else:
    print('That\'s not an option. Game Over.')