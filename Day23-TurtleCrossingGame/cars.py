from turtle import Turtle
import random

COLORS = ["orange", "green", "red", "blue", "brown", "black", "purple"]


class Cars(Turtle):

    def __init__(self, random_y):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.goto(300, random_y)
        self.shapesize(1, 2)

    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
