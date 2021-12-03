ciklus = True
while ciklus:
  from clear import clear
  clear()

  from logo import logo
  print(logo)

  from alphabet import alphabet

  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

  import functions

  if direction == 'encode' or direction == 'decode':
    functions.ceasar(direction, text, shift)
  else:
    print('There is no such direction. Run program again')
  
  again = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
  if again == 'no':
    ciklus = False

print("Goodbye!!!")