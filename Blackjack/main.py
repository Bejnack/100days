############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_game = True

if input("Do you want to play a game of Blackjack? Type 'y' or 'n' ") == "y":
    play_game = True
else:
    play_game = False

def random_cards():
    random_card = []
    for x in range(2):
        # print(x)
        a = random.randrange(0, 12)
        #print(a)
        random_card.append(cards[a])
   #print(random_card)
    return random_card

while play_game == True:
    #random_cards()
    print(f"Your cards: {random_cards()} ")
    pass