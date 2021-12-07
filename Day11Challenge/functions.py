import random

def clear():
    """ Clears screen before the game starts"""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

### These are the using cards
### Asume that there is a infinite deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

### Declare empty lists of participans
player = []
dealer = []

def random_card():
    """Pick random card from deck"""
    card = random.choice(cards)
    return card

def append_card():
    for round in range(3):
        card = random_card()
        if round == 0 or round == 2:
            player.append(card)
        else:
            dealer.append(card)

def another_card():
    card = random_card()
    player.append(card)

def calculating_score(list):
    score = 0
    for card in list:
        score += card
    return score