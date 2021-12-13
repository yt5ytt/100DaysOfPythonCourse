from logo import logo
from functions import clear, report, check_resources
from data import resources, menu_choice
money = 0
print(logo)
print("Welcome to 'COPACABANA' Coffee Machine!")

order_free = True
while order_free:
    # clear()
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "off":
        exit("GOODBYE!!!")
    elif choice == "report":
        report(resources, money)
    elif choice in menu_choice:
        is_available = check_resources(resources, choice)
    else:
        print("There is no such choice.")
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if is_available is not True:
        print(is_available)
    else:
        print("Just a moment please!")
