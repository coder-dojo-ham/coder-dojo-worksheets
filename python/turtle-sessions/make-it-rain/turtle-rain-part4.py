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

draw_drop(0,0)
##
##drops=[]
##for n in range(100):
##    drop = [random.randint(-400, 400), random.randint(-400, 400) ]
##    drops.append( drop )
##
##while(True):
##    t.clear()
##    for drop in drops:
##        # Move it down!
##        drop[1] = drop[1] - 3
##        # Start it up  at the top
##        if drop[1] < -400:
##            drop[1] = 400
##        draw_drop(drop[0], drop[1])
##    turtle.update()

turtle.done()
