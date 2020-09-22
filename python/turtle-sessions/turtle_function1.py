import turtle


def square():
    turtle.begin_fill()
    for n in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()

def hexagon():
        for n in range(6):
            turtle.forward(100)
            turtle.left(60)

colours = ["red", "blue", "green"] * 2
for colour in colours:
    turtle.pencolor(colour)
    turtle.fillcolor(colour)
    square()
    turtle.forward(100)
    turtle.right(60)
