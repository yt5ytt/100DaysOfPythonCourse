run = True
while run:
  import functions
  functions.clear()
  from logo import logo
  print(logo)

  first_number = float(input("What's the first number?: "))

  for symbol in functions.operations:
    print(symbol)

  again = True
  while again:
    operand = input("Pick an operation: ")
    second_number = float(input("What's the second number?: "))

    result = functions.dynamic_operation(first_number, second_number, operand)

    print(f"{first_number} {operand} {second_number} = {result}")

    wrong = True
    while wrong:
      ask_again = input(f"Type 'y' if you want to calculating with {result}, 'n' to start a new calculation, or 'exit' to quit the program: ").lower()

      if ask_again == 'n':
        again = False
        wrong = False
      elif ask_again == 'y':
        first_number = result
        wrong = False
      elif ask_again == 'exit':
        wrong = False
        again = False
        run = False
        print("G O O D B Y E ! ! !")
      else:
        print("\nThat is wrong answer. Please try again!")

