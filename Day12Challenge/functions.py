import random

def clear():
    """ Clears screen before the game starts"""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def level(difficulty):
    """Fetch difficulty argument and returns number of tries due the chosen difficulty level"""
    if difficulty == 'easy':
        tryes = 10
    elif difficulty == 'hard':
        tryes = 5
    else:
        tryes = 0
    
    return tryes

def ask_difficulty():
    """Asks difficulty level, calculate number of tries through level() function and then prints message. Returns number of tries"""
    difficulty = input("Izaberi tezinu. Ukucaj 'easy' ako hoces da imas 10 pokusaja ili da probas sa 'hard' ako mislis da mozes da pogodis u 5 pokusaja: ").lower()
    num_of_tryes = level(difficulty)
    if difficulty == 'easy':
        print("\nIzabrao si laksi nivo. Imas 10 pokusaja\n")
    elif difficulty == 'hard':
        print("\nIzabrao si tezi nivo. Imas samo 5 pokusaja\n")
    else:
        print("\nUkucao si nepostojecu opciju. Pokusaj ponovo\n")
        ask_difficulty()
    
    return num_of_tryes

def random_number():
    """Generate and returns random number from 1 - 100"""
    number = random.randint(1, 100)
    return number

def check(guess, random_number):
    """Compares relationship between guessed and random numbers"""
    if guess == random_number:
      print("BRAVO... POGODIO SI... POBEDA!!!\n")
    elif guess <= random_number:
      print("Malo je... Broj je veci!\nPogadjaj ponovo.\n")
    elif guess >= random_number:
      print("Mnogo je kume... Smanji malo!!!\nPogadjaj ponovo.\n")