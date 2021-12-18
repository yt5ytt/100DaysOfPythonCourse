import turtle as t
from random import choice

list_of_tuples = [(202, 12, 30), (35, 91, 186), (232, 149, 48), (197, 68, 22), (212, 13, 9), (35, 31, 152),
                  (49, 220, 60), (241, 46, 151), (20, 22, 53), (14, 208, 224), (75, 9, 53),
                  (17, 154, 18), (55, 26, 13), (80, 193, 223), (219, 23, 116), (232, 159, 8), (241, 64, 24),
                  (221, 138, 191), (96, 75, 10), (247, 11, 9), (83, 238, 162), (11, 96, 63), (5, 35, 33),
                  (89, 208, 147)]


tim = t.Turtle()
tim.speed(0)
t.colormode(255)
tim.penup()
tim.hideturtle()
y = -250


def one_row():
    for _ in range(10):
        tims_color = choice(list_of_tuples)
        tim.dot(20, tims_color)
        tim.forward(50)


for i in range(10):
    tim.goto(-250, y)
    one_row()
    y += 50

screen = t.Screen()
screen.exitonclick()
