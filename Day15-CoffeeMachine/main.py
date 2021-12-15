from logo import logo
from functions import clear, report, check_resources, sum_inserted, spend_resources
from data import resources, menu_choice, MENU
money = 0
clear()
print(logo)
print("Welcome to 'COPACABANA' Coffee Machine!")

# Begins while loop with whole app
order_free = True
while order_free:

    # Start parameters
    is_available = False
    choice = ""
    checked_choice = ""

    # If choice is wrong in input parameter, while loop to return to begin of app
    wrong_choice = True
    while wrong_choice:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "off":
            exit("GOODBYE!!!")
        elif choice == "report":
            report(resources, money)
        elif choice in menu_choice:
            checked_choice = check_resources(resources, choice)
            if checked_choice == "Available":
                is_available = True
            wrong_choice = False
        else:
            print("There is no such choice.")

    # Checking if there is enough ingredients or not and begin calculation and coffee prepare.
    if not is_available:
        print(f"Sorry, there's not enough {checked_choice}")
    else:
        print("Please insert coins.")
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))
        inserted = [quarters * 0.25, dimes * 0.10, nickles * 0.05, pennies * 0.01]
        sum_money = sum_inserted(inserted)

        # Checks if is enough money for order or not
        if sum_money < MENU[choice]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            spend_resources(resources, choice)
            change = sum_money - MENU[choice]["cost"]
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice}. Enjoy!")
            money += MENU[choice]["cost"]
