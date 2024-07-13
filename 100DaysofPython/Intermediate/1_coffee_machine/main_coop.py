from menu import MENU, resources

profit = 0
is_on = True


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made,
    False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns total calculated from coins inserted"""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when paymen accepted, False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is {change}$ in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingrediets):
    """Deduct the required ingredients from the resources"""
    for item in order_ingrediets:
        resources[item] -= order_ingrediets[item]
    print(f"Here is your {drink_name} ☕")


while is_on:
    choise = input("What would you like? (espresso/latte/cappuccino): ")
    if choise == "off":
        is_on = False
    elif choise == "report":
        print(f"Water: {resources['water']}ml") 
        print(f"Milk:{resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}ml")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choise]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choise, drink["ingredients"])
