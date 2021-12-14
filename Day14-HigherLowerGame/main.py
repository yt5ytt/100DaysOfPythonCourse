from data import data
import functions
import logo
score = 0
random_a = functions.random_num()
message = ""

play = True
guess = True
while play:
  functions.clear()
  print(logo.logo)

  print(message)
  if not guess:
    break

  followers_a = functions.followers(random_a)

  print(f"Compare A: {functions.compare_text(random_a)}.")

  print(logo.vs)

  random_b = functions.random_num()
  while random_a == random_b:
    random_b = functions.random_num()

  followers_b = functions.followers(random_b)

  print(f"Compare B: {functions.compare_text(random_b)}.")

  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  if (answer == 'a' and followers_a > followers_b) or (answer == 'b' and followers_a < followers_b):
    score += 1
    random_a = random_b
    message = f"You're right! Current score: {score}"
  else:
    message = f"Sorry, that's wrong. Final score: {score}"
    guess = False
