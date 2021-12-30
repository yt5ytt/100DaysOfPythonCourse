with open("./Input/Names/invited_names.txt") as f:
    list_of_names = f.readlines()

with open("./Input/Letters/starting_letter.txt") as file:
    letter = file.read()

for name in list_of_names:
    name = name.strip()
    new_letter = letter.replace("[name]", name)
    new_file = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")
    new_file.write(new_letter)
