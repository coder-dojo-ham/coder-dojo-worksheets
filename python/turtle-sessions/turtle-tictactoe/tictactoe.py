import turtle

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.penup()
turtle.tracer(0, 0)
GRID_CELL_SIZE = 100
TOP_LEFT = (-(GRID_CELL_SIZE * 1.5), (GRID_CELL_SIZE * 1.5))

def draw_centred_x(x, y):
  pen.goto(x, y)
  pen.pendown()
  pen.setheading(45)
  pen.forward(GRID_CELL_SIZE/2)
  pen.backward(GRID_CELL_SIZE)
  pen.forward(GRID_CELL_SIZE/2)
  pen.setheading(135)
  pen.forward(GRID_CELL_SIZE/2)
  pen.backward(GRID_CELL_SIZE)
  pen.forward(GRID_CELL_SIZE/2)
  pen.penup()

def draw_centered_circle(x, y):
  pen.goto(x, y - GRID_CELL_SIZE * 0.45)
  pen.pendown()
  pen.setheading(0)
  pen.circle(GRID_CELL_SIZE * 0.45)
  pen.penup()

def draw_move(row_number, col_number, move):
  cell_top_left = (
      TOP_LEFT[0] + GRID_CELL_SIZE/2 + (col_number * GRID_CELL_SIZE), 
      TOP_LEFT[1] - GRID_CELL_SIZE/2 - (row_number * GRID_CELL_SIZE)
    )
  if move == "x":
    draw_centred_x(cell_top_left[0], cell_top_left[1])
  else:
    draw_centered_circle(cell_top_left[0], cell_top_left[1])

def draw_board(board):
  pen.clear()
  # ensure pen is facing right
  pen.setheading(0)
  # Horizontal lines
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
  pen.penup()
  # draw board positions
  for row_number, row in enumerate(board.board_position):
    for col_number, move in enumerate(row):
      if move:
        draw_move(row_number, col_number, move)
  
  # draw a Current player box
  # with "Current player:" text next to it
  # and a circle/x in the box
  pen.goto(TOP_LEFT[0] + GRID_CELL_SIZE, TOP_LEFT[1] + GRID_CELL_SIZE * 1.5)
  pen.pendown()
  pen.setheading(0)
  for n in range(4):
    pen.forward(GRID_CELL_SIZE)
    pen.right(90)
  pen.setheading(0)
  pen.penup()
  pen.goto(TOP_LEFT[0], TOP_LEFT[1] + GRID_CELL_SIZE)
  pen.pendown()
  pen.write("Current player:", align="center", font=("Arial", 20, "normal"))
  pen.penup()
  if board.current_player == "x":
    draw_centred_x(TOP_LEFT[0] + GRID_CELL_SIZE * 1.5, TOP_LEFT[1] + GRID_CELL_SIZE * 1)
  else:
    draw_centered_circle(TOP_LEFT[0] + GRID_CELL_SIZE * 1.5, TOP_LEFT[1] + GRID_CELL_SIZE * 1)
  turtle.update()


class GameBoard:
  def __init__(self):
    self.board_position = [
      ['', '', ''],
      ['', '', ''],
      ['', '', '']
    ]

    self.current_player = "o"

  def can_move(self, row_number, col_number):
    return self.board_position[row_number][col_number] == ''
  
  def make_move(self, row_number, col_number):
    self.board_position[row_number][col_number] = self.current_player

  def next_turn(self):
    self.current_player = "o" if self.current_player == "x" else "x"
 
  def has_a_winner(self):
    # check rows
    for row in self.board_position:
      if row[0] == row[1] == row[2] and row[0] != '':
        return True
    # check columns
    for col_number in range(3):
      if self.board_position[0][col_number] == self.board_position[1][col_number] == self.board_position[2][col_number] and \
          self.board_position[0][col_number] != '':
        return True
    # check diagonals
    if self.board_position[0][0] == self.board_position[1][1] == self.board_position[2][2] and \
        self.board_position[0][0] != '':
      return True
    if self.board_position[0][2] == self.board_position[1][1] == self.board_position[2][0] and \
        self.board_position[0][2] != '':
      return True
    return False


def on_click(x, y):
  print("Clicked at", x, y)
  row_number = int((TOP_LEFT[1]-y) / GRID_CELL_SIZE)
  col_number = int((x - TOP_LEFT[0]) / GRID_CELL_SIZE)
  print("Clicked at row", row_number, "col", col_number)
  if row_number < 0 or row_number > 2 or col_number < 0 or col_number > 2:
    return
  if board.can_move(row_number, col_number):
    turtle.bgcolor("white")
    board.make_move(row_number, col_number)
  else:
    turtle.bgcolor("red")
    draw_board(board)
    return
  
  draw_board(board)
  if board.has_a_winner():
    pen.goto(0, -15)    
    pen.write("Winner!", align="center", font=("Arial", 50, "normal"))
    turtle.bgcolor("blue")
    turtle.update()
    turtle.exitonclick()
  else:
    board.next_turn()
    draw_board(board)

board = GameBoard()
turtle.onscreenclick(on_click)

draw_board(board)

turtle.done()
