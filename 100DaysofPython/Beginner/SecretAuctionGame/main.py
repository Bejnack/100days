import os
import art

def clear():
    os.system('cls')


print(art.logo)

other_user = True
revenue = {}

while other_user == True:
    name = input("What is your name?")
    bid_price = input("What is your bid price? $")
    revenue[name] = bid_price
    highest_bid= float()
    other_user_loop = input("Is there another bidder?\n")
    if other_user_loop == "no" or other_user_loop == "No" or other_user_loop == "NO":
        other_user = False
    for key in revenue:
        if float(revenue[key]) > highest_bid:
           highest_bid = float(revenue[key])
    else:
        clear()
        print(f"Highest bidder is {key} with {revenue[key]}$!")

        
