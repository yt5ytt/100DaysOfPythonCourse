import turtle as t
import random

is_race_on = False
screen = t.Screen()

start_width = random.randint(300, 1800)
start_height = random.randint(200, 800)
screen.setup(width=start_width, height=start_height)
colors = ["red", "orange", "black", "green", "blue"]
turtle_list = []
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ").lower()
num_turtles = len(colors)


def start_x(width):
    x = 20 - int(width/2)
    return x


def start_y(number):
    y = 0 - 30 * round(number/2)
    return y


start_x = start_x(start_width)
start_y = start_y(num_turtles)


for i in range(len(colors)):
    new_turtle = t.Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(start_x, start_y)
    start_y += 30
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtle_list:

        if turtle.xcor() > start_width / 2 - 20:
            is_race_on = False
            winning_color = turtle.pencolor().lower()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle has won!")
            else:
                print(f"You've lost! The {winning_color} turtle has won!")

        random_distance = random.randint(1, 6)
        turtle.forward(random_distance)

screen.exitonclick()
