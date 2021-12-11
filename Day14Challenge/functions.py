import random
from data import data

def clear():
    """ Clears screen before the game starts"""
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')

def data_len():
    from data import data
    lenght = len(data)
    return lenght

def random_num():
    num = random.randint(0, data_len() - 1)
    return num

def name(number):
    name = data[number]["name"]
    return name

def followers(number):
    followers = data[number]["follower_count"]
    return followers

def description(number):
    description = data[number]["description"]
    return description

def country(number):
    country = data[number]["country"]
    return country


