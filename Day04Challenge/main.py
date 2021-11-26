rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

lista = [rock, paper, scissors]

myHand = int(input('What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n'))

print(lista[myHand])

computer = random.randint(0,2)

print('\nComputer choose:\n')

print(lista[computer])

if myHand == computer:
    print('It\'s a draw!')
elif (myHand == 0 and computer == 1) or (myHand == 1 and computer == 2) or (myHand == 2 and computer == 0):
    print('You\'ve lost!')
else:
    print('You\'ve win!')