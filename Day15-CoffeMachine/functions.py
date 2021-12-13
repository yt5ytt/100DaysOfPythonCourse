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
    from data import MENU
    available = True
    for key in resources:
        if key not in MENU[choice]["ingredients"]:
            continue
        elif resources[key] < MENU[choice]["ingredients"][key]:
            available = f"Sorry, there in not enough {key}"
    return available


