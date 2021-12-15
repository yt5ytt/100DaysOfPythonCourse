from random import random
import functions

play = True
while play:
  functions.clear()
  from logo import logo
  print(logo)
  print("Dobro dosli u igru 'Pogodi broj'")
  print("Zamislicu broj izmedju 1 i 100.")
  
  num_of_tryes = functions.ask_difficulty()

  random_number = functions.random_number()

  for atempt in range(num_of_tryes):
    guess = int(input(f"Pokusaj broj {atempt + 1}: "))
    functions.check(guess, random_number)    
    
    if guess == random_number:
      break
    
  if guess != random_number:
    print("Nemas vise pravo da pogadjas. IZGUBIO SI!!!\n")  

  play_again = input("Da li zelis ponovo da igras igru. Ukucaj 'y' ako zelis ili 'n' ako ne zelis: ").lower()
  if play_again == 'n':
    play = False

###End of code