import functions

play = True
while play:
  question = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
  if question != 'y':
    play = False
    exit()
  
  from functions import clear
  ### clear screen before the game starts
  clear()

  from logo import logo
  ### prints logo of the game
  print(logo)

  player = []
  dealer = []
  
  for round in range(3):
    card = functions.random_card()
    if round == 0 or round == 2:
        player.append(card)
    else:
        dealer.append(card)
  
  another_card = True
  while another_card:  
    player_score = functions.calculating_score(player)
    if player_score > 21:
      ace = 11
      if ace in player:
        index = player.index(ace)
        player[index] = 1
      player_score = functions.calculating_score(player)
    dealer_score = functions.calculating_score(dealer)

    print(f"   Your cards: {player}, current score: {player_score}")
    print(f"   Dealer's first card: {dealer_score}")

    if player_score > 21:
      another_card = False
    else:
      more_cards = input("Type 'y' to get another card, type any other key to pass: ")
    
    if more_cards != 'y':      
      another_card = False
    else:
      card = functions.random_card()
      player.append(card)
  
  while dealer_score <= 17:
    card = functions.random_card()
    dealer.append(card)
    dealer_score = functions.calculating_score(dealer)
    if dealer_score > 21:
      ace = 11
      if ace in dealer:
        index = dealer.index(ace)
        dealer[index] = 1
      dealer_score = functions.calculating_score(dealer)
  
  print(f"   Your cards: {player}, final score: {player_score}")
  print(f"   Dealer's cards: {dealer}, final score: {dealer_score}")

  if 10 in player and 11 in player:
    if 10 in dealer and 11 in dealer:
      print("It's a DRAW! You both have BLACKJACK!!!")
    else:
      print("You win! You have BLACKJACK")  
  elif player_score <= 21:
    if 10 in dealer and 11 in dealer:
      print("You lose. Dealer have BLACKJACK!!!")
    elif dealer_score > 21:
      print("Dealer went over. YOU WIN!!!!")
    elif player_score == dealer_score:
      print("It's a DRAW!!!")
    elif player_score < dealer_score:
      print("Dealer wins. YOU LOSE!!!")
    elif player_score > dealer_score:
      print("YOU WIN!!!")
  else:
    if 10 in dealer and 11 in dealer:
      print("You lose. Dealer have BLACKJACK!!!")
    if dealer_score > 21:
      print("You've both went over. It's a DRAW!!!")
    else:
      print("You went over. YOU LOSE!!!")

###End of code
