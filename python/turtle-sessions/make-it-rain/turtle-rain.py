import turtle
import random

screen = turtle.Screen()
screen.bgpic("lake-background.png")

turtle.tracer(0, 0) # yes this should be turtle, not t.
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

def draw_drop(x, y):
    t.shape('circle')
    t.color('blue')
    t.goto(x, y)
    t.stamp()
    t.pendown()
    #t.forward(50)
    t.penup()

drops = []
for n in range(100):
    drop = [random.randint(-400, 400), random.randint(-400, 400) ]
    drops.append( drop )

while True:
    t.clear()
    for drop in drops:
        drop[1] -= 3
        if drop[1] < -400:
            drop[1] = 400
        draw_drop(drop[0], drop[1])
    turtle.update()
