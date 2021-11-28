#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

easyPass = ""
for number in range(1, nr_letters + 1):
    easyPass += random.choice(letters)
    
for number in range(1, nr_numbers + 1):
    easyPass += random.choice(numbers)

for number in range(1, nr_symbols + 1):
    easyPass += random.choice(symbols)

print(f"This is result of the Easy Level of password generator: {easyPass}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#this is my solution of Hard Level password generator

hardPass = "".join(random.sample(easyPass,len(easyPass)))
print(f"This is result of the Hard Level of password generator: {hardPass}")

#this is Angela's solution of Hard Level password generator

password_list = []

for char in range(1, nr_letters + 1):
  password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
  password_list += random.choice(symbols)

for char in range(1, nr_numbers + 1):
  password_list += random.choice(numbers)

# print(password_list)
random.shuffle(password_list)
# print(password_list)

password = ""
for char in password_list:
  password += char

print(f"Your password is: {password}")