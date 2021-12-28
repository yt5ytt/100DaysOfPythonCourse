from turtle import Turtle


class LittleTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.color("black")
        self.goto(0, -280)

    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)

    def reset_turtle(self):
        self.goto(0, -280)