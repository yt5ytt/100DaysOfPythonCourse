from data import MENU


def clear():
    """ Clears screen before the game starts"""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')\



def report(resources, money):
    """ Prints formated string with report """
    print(f'''
Water: {resources["water"]}ml
Milk: {resources["milk"]}ml
Coffee: {resources["coffee"]}g
Money: ${money}
''')


def check_resources(resources, choice):
    """ Check if is there enough resources or not"""
    for key in resources:
        if key not in MENU[choice]["ingredients"]:
            continue
        elif resources[key] < MENU[choice]["ingredients"][key]:
            return key
        else:
            return "Available"


def sum_inserted(inserted):
    """ Calculates SUM of entered money """
    sum_of_money = sum(inserted)
    return sum_of_money


def spend_resources(resources, choice):
    """ Returns list with new amount of resources after spent ingredients """
    for key in resources:
        if key not in MENU[choice]["ingredients"]:
            continue
        else:
            resources[key] = resources[key] - MENU[choice]["ingredients"][key]
    return resources
