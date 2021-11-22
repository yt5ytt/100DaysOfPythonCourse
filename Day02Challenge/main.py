#Greetings message
print("Welcome to the tip calculator")

#Input total bill
bill = input("What was the total bill? $")

#Input percentage tip
tipPercentage = input("What percentage tip would you like to give? 10, 12 or 15? ")

#Input number of people
numberPeople = input("How many people to split the bill? ")

#Let's calculate
bill = float(bill)
tipPercentage = 1 + round(int(tipPercentage)/100, 2)
numberPeople = int(numberPeople)

result = bill * tipPercentage / numberPeople
result = "{:.2f}".format(result)

print(f"Each person should pay: ${result}")