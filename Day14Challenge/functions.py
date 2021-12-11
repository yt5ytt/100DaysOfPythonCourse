import random
from data import data

def clear():
    """ Clears screen before the game starts"""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def data_len():
    """Returns length of data list"""
    from data import data
    lenght = len(data)
    return lenght

def random_num():
    """Returns random number for the key of data list"""
    num = random.randint(0, data_len() - 1)
    return num

def followers(number):
    """Returns number of followers of the compare participant"""
    followers = data[number]["follower_count"]
    return followers

def compare_text(number):
    """Returns text of the compare participant"""
    name = data[number]["name"]
    description = data[number]["description"]
    country = data[number]["country"]
    message = f"{name}, {description}, from {country}."
    return message