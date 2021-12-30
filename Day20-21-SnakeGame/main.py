from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

WIDTH = 600
HEIGHT = 600


screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update_score()
    
    # detect if snake hits wall
    if snake.head.xcor() > WIDTH/2 - 20 or snake.head.xcor() < -(WIDTH/2 - 20) or snake.head.ycor() < -(HEIGHT/2 - 20) \
            or snake.head.ycor() > HEIGHT/2 - 20:
        score.reset_score()
        snake.reset_snake()
        # game_is_on = False
        # score.game_over()
    
    # detect if snake hits its tale
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
            # game_is_on = False
            # score.game_over()
        

screen.exitonclick()
