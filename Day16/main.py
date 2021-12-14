from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee = CoffeeMaker()
menu = Menu()
money = MoneyMachine()

is_on = True
while is_on:
    
    choice = input("What would you like? (espresso/latte/cappuccino/): ").lower()

    if choice == 'off':
        exit("COFFEE MACHINE IS GOING DOWN!")
    elif choice == 'report':
        coffee.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffee.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffee.make_coffee(drink)