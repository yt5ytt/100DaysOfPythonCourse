from turtle import Turtle

FONT = ("Courier", 8, "bold")
ALIGN = "center"

class WriteTurtle(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
    
    def writeState(self, coors, answer):
        self.goto(coors)
        self.write(f"{answer}", align=ALIGN, font=FONT)
        