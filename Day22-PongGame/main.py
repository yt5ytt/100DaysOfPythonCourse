from turtle import Screen
from paddle import Paddle
from scoreboard import Score
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    # Detect if ball hits wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect if ball hits paddle
    if ball.xcor() > 320 and ball.distance(r_paddle) < 50 or ball.xcor() < - 320 and ball.distance(l_paddle) < 50:
        ball.bounce_x()
        ball.ball_speed()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

    screen.update()

screen.exitonclick()
