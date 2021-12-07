import random

def clear():
    """ Clears screen before the game starts"""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

### These are the using cards
### Asume that there is a infinite deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def random_card():
    """Pick random card from deck"""
    card = random.choice(cards)
    return card

def dealing_cards(card, list):
    """Adding random card in player's and dealer's lists"""
