import functions

play = True
while play:
  question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if question == 'n':
    play = False
    exit()
  
  from functions import clear
  ### clear screen before the game starts
  clear()

  from logo import logo
  ### prints logo of the game
  print(logo)

  card = functions.random_card()

  

