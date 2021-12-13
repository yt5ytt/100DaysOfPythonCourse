from data import MENU


def clear():
    """ Clears screen before the game starts"""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')\



def report(resources, money):
    print(f'''
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money}
''')


def check_resources(resources, choice):
    for key in resources:
        if key not in MENU[choice]["ingredients"]:
            continue
        elif resources[key] < MENU[choice]["ingredients"][key]:
            return key
        else:
            return "Available"


def sum_inserted(inserted):
    sum_of_money = sum(inserted)
    return sum_of_money


def spend_resources(resources, choice):
    for key in resources:
        if key not in MENU[choice]["ingredients"]:
            continue
        else:
            resources[key] = resources[key] - MENU[choice]["ingredients"][key]
    return resources
