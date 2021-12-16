import turtle as t
import random

tim = t.Turtle()
# tim.shape("turtle")
tim.color("red")
tim.speed(1)
t.colormode(255)

# step = 5
# i = round(360/step)
# heading = 0



# heading = [0, 90, 180, 270]
# elements = "0123456789ABCDEF"
#
#
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return (r, g, b)


tim.penup()

tim.goto(-200, -200)
tim.dot(20, random_color())

tim.goto(-150, -200)
tim.dot(20, random_color())

tim.goto(-100, -200)
tim.dot(20, random_color())


# for _ in range(i):
#     tim.circle(100)
#     tim.setheading(heading)
#     tim.color(random_color())
#     heading += step
#
#
# for _ in range(1000):
#     tim.pencolor(random_color())
#     tim.forward(30)
#     angle = random.choice(heading)
#     tim.setheading(angle)

screen = t.Screen()
screen.exitonclick()
