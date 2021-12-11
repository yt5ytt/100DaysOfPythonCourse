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

  name_a = functions.name(random_a)
  followers_a = functions.followers(random_a)
  description_a = functions.description(random_a)
  country_a = functions.country(random_a)

  print(f"Compare A: {name_a}, {description_a}, from {country_a}.")

  print(logo.vs)

  random_b = functions.random_num()
  while random_a == random_b:
    random_b = functions.random_num()

  name_b = functions.name(random_b)
  followers_b = functions.followers(random_b)
  description_b = functions.description(random_b)
  country_b = functions.country(random_b)

  print(f"Compare B: {name_b}, {description_b}, from {country_b}.")

  answer = input("Who has more followers? Type 'A' or 'B': ").lower()

  if (answer == 'a' and followers_a > followers_b) or (answer == 'b' and followers_a < followers_b):
    score += 1
    random_a = random_b
    message = f"You're right! Current score: {score}"
  else:
    message = f"Sorry, that's wrong. Final score: {score}"
    guess = False
