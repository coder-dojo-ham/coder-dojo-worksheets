# make it rain
import turtle
import random

t = turtle.Turtle()
t.speed(0)
turtle.tracer(0, 0)
t.hideturtle()
t.penup()


def draw_drop(x, y):
    t.shape('circle')
    t.color('blue')
    t.goto(x, y)
    t.stamp()

drops=[]
for n in range(100):
    drop = random.randint(-400, 400), random.randint(-400, 400) 
    drops.append( drop )

while(True):
    t.clear()
    for drop in drops:
        draw_drop(drop[0], drop[1])
    turtle.update()

turtle.done()
