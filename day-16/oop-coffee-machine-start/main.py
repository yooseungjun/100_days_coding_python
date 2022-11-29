from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()

choose = input(f"What would you like? {menu.get_items()}:")

while True :
    if choose == 'off':
        break
    elif choose =='report':
        coffeemaker.report()
        moneymachine.report()
    else:
        drink = menu.find_drink(choose)
        if drink is not None and coffeemaker.is_resource_sufficient(drink) and moneymachine.make_payment(drink.cost):
            coffeemaker.make_coffee(drink)

    choose = input(f"What would you like? {menu.get_items()}:")