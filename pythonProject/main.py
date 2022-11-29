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


def print_report(menu):
    for i in MENU[menu]:
        print(f"{i} : {MENU[menu][i]}")

def insert_coin():
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    return 0.25*quarters + 0.1*dimes + 0.05*nickles + 0.01*pennies


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money: {profit}")


def check_resources(choose):
    for i in MENU[choose]['ingredients']:
        if resources[i]< MENU[choose]['ingredients'][i]:
            print(f"Sorry there is not enough {i}")
            return False
    return True
    #
    # if resources['water'] < MENU[choose]['ingredients']['water']:
    #     print("Sorry there is not enough water.")
    #     return False
    # if resources['milk'] < MENU[choose]['ingredients']['milk']:
    #     print("Sorry there is not enough milk.")
    #     return False
    # if resources['coffee'] < MENU[choose]['ingredients']['coffee']:
    #     print("Sorry there is not enough coffee.")
    #     return False
    # return True

def make_coffee(choose):
    global profit
    for i in MENU[choose]['ingredients']:
        resources[i] -= int(MENU[choose]['ingredients'][i])

    #
    # resources['water']-=int(MENU[choose]['ingredients']['water'])
    # resources['milk'] -= int(MENU[choose]['ingredients']['milk'])
    # resources['coffee'] -= int(MENU[choose]['ingredients']['coffee'])
    profit+=MENU[choose]['cost']

def print_resources():
    for i in resources:
        print(resources[i])

choose = input("What would you like? (espresso/latte/cappuccino): ")
while choose!='off':
    if choose == 'off':
        exit()
    elif choose == "report":
        report()
    else:
        cost = float(MENU[choose]["cost"])
        #print(money)
        #print_resources()
        if check_resources(choose):
            money = insert_coin()
            if money <= cost:
                print("Sorry that's not enough money. Money refunded.")
            profit += cost
            print(f"Here is ${money-cost} dollars in change.")
            make_coffee(choose)
            print(f"Here is your {choose} ☕. Enjoy!")
    choose = input("What would you like? (espresso/latte/cappuccino): ")