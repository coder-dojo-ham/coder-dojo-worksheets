import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
turtle.tracer(0, 0)
GRID_CELL_SIZE = 100
TOP_LEFT = (-(GRID_CELL_SIZE * 1.5), (GRID_CELL_SIZE * 1.5))
# horizontal
pen.goto(TOP_LEFT[0], GRID_CELL_SIZE/2)
pen.pendown()
pen.forward(GRID_CELL_SIZE * 3)
pen.penup()
pen.goto(TOP_LEFT[0],-GRID_CELL_SIZE/2)
pen.pendown()
pen.forward(GRID_CELL_SIZE * 3)
pen.penup()
# Vertical lines
pen.goto(-GRID_CELL_SIZE/2, TOP_LEFT[1])
pen.right(90)
pen.pendown()
pen.forward(GRID_CELL_SIZE * 3)
pen.penup()
pen.goto( GRID_CELL_SIZE/2, TOP_LEFT[1])
pen.pendown()
pen.forward(GRID_CELL_SIZE * 3)

turtle.update()
turtle.done()
