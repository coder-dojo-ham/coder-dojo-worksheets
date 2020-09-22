import turtle 

def square():
    for n in range(4):
        turtle.forward(100)
        turtle.left(90)

for n in range(6):
    square()
    turtle.forward(100)
    turtle.right(60)

