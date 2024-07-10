"""Coffee machine"""
import sys
from menu import MENU, resources

coins = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01,
}

while  True:
    choise = input("What would you like? (espresso/latte/cappucino): ").lower()

    if choise == "report":
        for resource, amount in resources.items():
            print(f"{resource}: {amount}")
        continue
    if choise in {"espresso", "latte", "cappuccino"}:
        for ingredient_type in MENU[choise]["ingredients"]:
            if ingredient_type in resources:
                if MENU[choise]["ingredients"][ingredient_type] < resources[ingredient_type]:
                    print(f"Sorry there is not enough {ingredient_type}.")
                    sys.exit()
    elif choise == "off":
        sys.exit()
    else:
        print("Input not recognised")

    print(f"Price of the selection is: {MENU[choise]["cost"]}$.")
    inserted_coins = 0.0
    for coin, value in coins.items():
        amount_of_coin = int(input(f"How many {coin}s?: "))
        sum_of_coins = amount_of_coin * value
        inserted_coins += sum_of_coins
    print(f"inserted coin = {"%.2f" % inserted_coins}")

    value_of_selection = MENU[choise]["cost"]

    if value_of_selection <= inserted_coins:
        if value_of_selection < inserted_coins:
            rest = inserted_coins - value_of_selection 
            print(f"Here is ${"%.2f" % rest} in change.")
        print(f"Here is your {choise} ☕.Enjoy")
        if "money" in resources:
            resources["money"] += value_of_selection
        else:
            resources["money"] = value_of_selection
        for ingredient_type in MENU[choise]["ingredients"]:
            resources[ingredient_type] -= MENU[choise]["ingredients"][ingredient_type]
    else:
        print("Sorry that's not enough money. Money refunded")
