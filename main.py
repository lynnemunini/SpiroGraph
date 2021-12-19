from turtle import Turtle, Screen
import random
tim = Turtle()
screen = Screen()
screen.colormode(255)
screen.bgcolor("seashell")
tim.shape("circle")
tim.shapesize(0.1, 0.1)
tim.speed("fastest")

def circle():
    radius = 100
    tim.circle(radius)


for _ in range(80):
    circle()
    x = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.pencolor(x)
    tim.color(x)
    tim.left(5)


screen.exitonclick()
