import turtle

myshape = ["green", "blue", "orange", "red", "forest green", "black",
           "brown", "magenta", "purple", "indigo", "lime", "gray", "cyan"] * 2

for colour in myshape:
    turtle.pencolor(colour)
    turtle.forward(100)
    turtle.left(100)
