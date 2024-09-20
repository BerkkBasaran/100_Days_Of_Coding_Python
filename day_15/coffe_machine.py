MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit = 0 
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
# TODO 4. Check resources sufficient?
def resource_check(icindekiler):
    for i in icindekiler:
        if icindekiler[i] > resources[i]:
            print(f"Sorry there is not enough {i}.")
            return False
    return True
# TODO 5. Process coins.
def coin_process():
    print("Please insert coins.")
    atilan_para = int(input("How many quarters?: ")) * 0.25
    atilan_para += int(input("How many dimes?: ")) * 0.10
    atilan_para += int(input("How many nickles?: ")) * 0.05
    atilan_para += int(input("How many pennies?: ")) * 0.01
    return atilan_para

# TODO 6. Check transaction successful?
def transaction_check(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



# TODO 7. Make Coffee.
def make_coffee(drink_name, order_ingredients):
    for i in order_ingredients:
        resources[i] -= order_ingredients[i]
    print(f"Here is your {drink_name} ☕. Enjoy!")


# TODO 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
devam = True
while devam:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()
# TODO 2. Turn off the Coffee Machine by entering “off” to the prompt.
    if order == "off":
        devam = False
# TODO 3. Print report.
    elif order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else: 
        drink = MENU[order]
        if resource_check(drink["ingredients"]):
            payment = coin_process()
            if transaction_check(payment, drink["cost"]):
                make_coffee(order, drink["ingredients"])

    



