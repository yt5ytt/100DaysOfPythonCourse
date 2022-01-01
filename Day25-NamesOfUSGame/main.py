import turtle
import pandas
from writeTurtle import WriteTurtle

IMAGE = "./blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

t = WriteTurtle()

data = pandas.read_csv("50_states.csv")
states_list = data["state"]
states = states_list.to_list()

correct_answers = []

while len(correct_answers) < 50:
    if len(correct_answers) > 0:
        popup_title = f"{len(correct_answers)}/50 States Correct"
    else:
        popup_title = "Guess the State"
    answer = screen.textinput(title=f"{popup_title}", prompt="What is the valid state name?").title()

    if answer == "Exit":
        states_to_learn = [state for state in states if state not in correct_answers]

        final_dict = {
            "States to learn": states_to_learn,
        }
        
        file_for_csv = pandas.DataFrame(final_dict)
        file_for_csv.to_csv("states_to_learn.csv")

        break

    if (answer in states) and (answer not in correct_answers):
        drzava = data[data["state"] == answer]
        x_coor = int(drzava.x)
        y_coor = int(drzava.y)
        coors = (x_coor, y_coor)
        t.writeState(coors, answer)
        correct_answers.append(answer)
