from turtle import Turtle

WIDTH = 600
HEIGHT = 600


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.number = 0
        self.color("white")
        self.penup()
        self.goto(0, WIDTH / 2 - 40)
        self.write(f"Score: {self.number}", move=False, align="center", font=("Arial", 20, "bold"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.number += 1
        self.write(f"Score: {self.number}", move=False, align="center", font=("Arial", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align="center", font=("Arial", 20, "bold"))
        