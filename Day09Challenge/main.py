from functions import clear
clear()
from logo import logo
print(logo)

all_bidders = {}

again = True
while again:
    name = input("what is your name?:\n")
    bid = int(input("What's your bid?\n$"))

    all_bidders[name] = bid

    type_error = True
    while type_error:
      more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

      if more_bidders == 'no':
        again = False
        type_error = False
      elif more_bidders == 'yes':
        type_error = False
        clear()
      else:
        print("\nWrong input. Please try again.")

from functions import find_highest_bidder
find_highest_bidder(all_bidders)