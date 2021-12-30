from turtle import Turtle
import random

WIDTH = 600
HEIGHT = 600


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.width(10)
        self.penup()
        self.refresh()

    def refresh(self):
        random_x = random.randint(int(WIDTH/2 - 20) * (-1), int(WIDTH/2) - 20)
        random_y = random.randint(int(HEIGHT/2 - 20) * (-1), int(HEIGHT/2) - 20)
        self.goto(random_x, random_y)
