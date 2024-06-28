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

def deal_card():
    random_card_pick = random.randrange(0, 12)
    random_card = cards[random_card_pick]
    return random_card

def calculate_score(hand):
    sum_hand = sum(hand)
    if len(hand) == 2 and hand[0] + hand[1] == 21:
        return 0 #Blackjack
    elif sum_hand > 21 and 11 in hand:
        hand.remove(11)
        hand.append(1)
        sum_hand = sum(hand)
    return sum_hand

def compare(score_u, score_c):
    if score_u == score_c:
        print("Draw")
        return False
    elif score_u == 21:
        print("Blackjack, you win")
    elif score_u > 21:
        print(f"Your score {score_u} is bigger than 21, you lost!")
        return False
    elif score_c == 21:
        print("Blackjack, computer wins")
        return False
    elif score_c > 21:
        print(f"Computer score {score_c} is bigger than 21, you win")
        return False
    elif score_c < 21 and score_u < 21:
        if score_c < score_u:
            print(f"You win {score_u} > {score_c} ")
            return False
        else:
            print(f"Computer wins {score_c} > {score_u}")
            return False

def blackjack():
    print("")
    should_continue = True
    user_card = []
    computer_card = []

    for x in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
    #user_card = [11, 10]
    user_score = calculate_score(user_card)
    computer_score = calculate_score(computer_card)

    print(f"""Player cards {user_card}, sum of player {calculate_score(user_card)} \nComputer cards {computer_card}, computer sum {calculate_score(computer_card)}""")

    if user_score == 0:
        print("Blackjack, you win")
        should_continue = False
    # elif user_score > 21:
    #     should_continue = False
    elif computer_score == 0:
        print("Blackjack, computer wins")
        should_continue = False

    while should_continue == True:
        while input("Do you want another card? 'y' or 'n'? ") == "y" and user_score < 21:
            user_card.append(deal_card())
            print(user_card)
            user_score = calculate_score(user_card)
            print(f"User score: {user_score}")
            if user_score > 21:
                should_continue = compare(user_score,computer_score)
                if input("Do you want another game? 'y' or 'n' ") == "y":
                    blackjack()
                else:
                    break

        while computer_score < 17:
            computer_card.append(deal_card())
            computer_score = calculate_score(computer_card)
        
        should_continue = compare(user_score,computer_score)
        should_continue
        if should_continue == False:
            if input("Do you want another game? 'y' or 'n' ") == "y":
                blackjack()
            else:
                break

blackjack()
