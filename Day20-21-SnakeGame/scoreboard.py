from turtle import Turtle

WIDTH = 600
HEIGHT = 600


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.number = 0
        self.high_score = 0
        self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, WIDTH / 2 - 40)
        self.write_score()
        self.hideturtle()

    def update_score(self):
        self.number += 1
        self.write_score()

    def reset_score(self):
        if self.number > self.high_score:
            self.high_score = self.number
            self.save_high_score()
        self.number = 0
        self.write_score()

    def read_high_score(self):
        with open("high_score.txt") as file:
            score = int(file.read())
            self.high_score = score

    def save_high_score(self):
        with open("high_score.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.number} High Score: {self.high_score}", align="center",
                   font=("Arial", 20, "bold"))
        