import random
import hangman_art
import hangman_words
from clear import clear

clear()

chosen_word = random.choice(hangman_words.word_list)
lives = 6

print(hangman_art.logo)

display = []
for letter in chosen_word:
  display += "_"

finish = False
guessedLetters = []
while not finish:
  guessLetter = input('Pogadjaj slovo: ').lower()

  clear()

  if guessLetter in guessedLetters:
    print(f'You\'ve already choose letter {guessLetter}. Try other one.')
  elif guessLetter not in chosen_word:
    print(f'Letter {guessLetter} is not in the chosen word. You\'ve losted one life')
    lives -= 1
    guessedLetters.append(guessLetter)
  else:    
    guessedLetters.append(guessLetter)

  listIndex = 0
  for letter in chosen_word:
    if guessLetter == letter:
      display[listIndex] = guessLetter

    listIndex += 1
  
  if lives == 0:
    finish = True
    memo = 'You\'ve lost!!!'
  elif "_" not in display:
    finish = True
    memo = 'You\'ve won!!!'

  #Join all the elements in the list and turn it into a String.
  print(f"{' '.join(display)}")

  print(hangman_art.stages[lives])

print(memo)



