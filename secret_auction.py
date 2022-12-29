import os
import secret_auction_art


def add_bidder(name, bid):
    bid_info = {}
    bid_info[name] = bid
    bidders.append(bid_info)


print(secret_auction_art.logo)
print('Welcome to the secret auction program.')

more_bidders = True
bidders = []
winner = ''
max_bid = 0

while more_bidders:
    bidder_name = input('What\'s your name?: ')
    bid_amount = int(input('What\'s your bid?: $'))
    other_bidders = input('Are there any other bidders? Type "yes" or "no".\n').lower()

    add_bidder(name=bidder_name, bid=bid_amount)

    if other_bidders == 'no':
        more_bidders = False

    # Clear the screen on Windows
    os.system('cls')
    # Clear the screen on Linux / OS X
    # os.system('clear')

for bidder_info in bidders:
    for bidder_name in bidder_info:
        if bidder_info[bidder_name] > max_bid:
            winner = bidder_name
            max_bid = bidder_info[bidder_name]

print(f'The winner is {winner} with a bid of ${max_bid}.')