import functions

play = True
while play:
  question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if question == 'n':
    play = False
    exit()
  elif question != 'y':
    exit()
  
  from functions import clear
  ### clear screen before the game starts
  clear()

  from logo import logo
  ### prints logo of the game
  print(logo)

  functions.player = []
  functions.dealer = []
  
  functions.append_card()
  
  another_card = True
  while another_card:  
    player_score = functions.calculating_score(functions.player)
    dealer_score = functions.calculating_score(functions.dealer)

    print(f"   Your cards: {functions.player}, current score: {player_score}")
    print(f"   Dealer's first card: {dealer_score}")
    more_cards = input("Type 'y' to get another card, type any other key to pass: ")
    
    if more_cards != 'y':
      another_card = False
    else:
      functions.another_card()