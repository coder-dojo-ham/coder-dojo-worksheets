---
title: Sheet name
---
<link rel="stylesheet" href="../common/sheet.css">

<table class="key_info">
<tr><td class="difficulty">Difficulty: <b>🌶🌶</b><i>🌶🌶🌶</i></td>
<td>Language: Python</td>
<td>Requires: Laptop with Python, coderdojo [games]</td></tr>
</table>

<img src="inspiration-screenshot.png" class="leader_picture"/>

Some inspiration text. A bit of background, and a link to the original project in github.
Focus on what is fun, what we will make and what we will learn.

This sheet recommends using Thonny in Python 3 mode.

## First part

Small text on what we'll start - like Lets start by setting up turtle to draw fast with `speed(0)`, hide the turtle with `hideturtle`, and pull up the pen with `penup`.

```python
import turtle

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
```

Save this in a file name like `rain.py` and run it.

To draw a simple drop we can use a blue circle. Add this:

<img src="raindrop-blue-circle.png" style="margin:0; padding: 0; float: right; margin-right: 5%; border: 0; box-shadow: none">

```python
t.shape("circle")
t.color("blue")

t.goto(0, 0)
t.stamp()
```

`t.shape` changes the turtles shape, `t.goto` jumps to a set of coordinates.
By using `t.stamp`, we can leave behind a stamp, an image of the turtles current shape on the canvas where it stands.


## Drawing multiple drops

We are going to want to stamp a blue circle many times - so let's move the drawing code into a function:

<pre><code>t.shape("circle")
t.color("blue")

<del>t.goto(0, 0)
t.stamp()
</del></code></pre>

```python
def draw_drop(x, y):
    t.goto(x, y)
    t.stamp()

draw_drop(0, 0)
draw_drop(30, -40)
draw_drop(50, 20)
```

`x` is how far across the screen from the left, `y` is how far up the screen from the bottom.
There is a negative number there. This is because `0, 0` is the middle of screen - so to go further down, or left, we need to subtract from `0` to get there. When you run this, it should draw 3 raindrops.

![Drawing 3 drops](drawing-3-drops.png)

## Checkpoint

Your code at this point should look like this:

```python
import turtle
import random

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()
t.shape("circle")
t.color("blue")

def draw_drop(x, y):
    t.goto(x, y)
    t.stamp()

drops = []
for n in range(100):
    drop = [random.randint(-400, 400), random.randint(-400, 400) ]
    drops.append(drop)

for drop in drops:
    draw_drop(drop[0], drop[1])
```

## Ideas to try

<!-- -- id="ideas" -->

### Try adding further parameters

You can try using a 3rd item in the lists - for speed, or raindrop size (t.shapesize). Let's try using it for speed.

When creating the drop, we can try a number between 2 and 4:

<pre><code>for n in range(100):
    drop = [random.randint(-400, 400), random.randint(-400, 400)<b>, random.randint(2,4)</b>]
    drops.append(drop)
</code></pre>

You can then use this 3rd parameter for speed instead of -3:

<pre><code>     for drop in drops:<del>
         drop[1] -= 3</del><b>
         drop[1] -= drop[2]</b>
         if drop[1] < -400:
             drop[1] = 400
</code></pre>

This now moves different drops at different speeds, giving a feeling of depth.

### Try changing the rain drops

Rain drops can be snow flakes too. Try changing the shape to a triangle, or a square using turtle commands. You can change the colour, size, put the pen down and do standard turtle drawing commands, or even use GIF or PNG images.

<pre><code>t.penup()
<del>t.shape("circle")
t.color("blue")</del>
<b>screen = turtle.Screen()
image = "myimage.gif"
screen.addshape(image)
t.shape(image)</b>

def draw_drop(x, y):
</code></pre>

Now when you stamp - it will be your image instead of the circles. Happy faces? Footballs? Spaceships? Stars?

## Turtle Colours

<!-- -- id="colours" -->

This is a limited list. Look up "TK colours" for more names. You can also use three numbers for red, green and blue to mix your
own colours: `t.color((172, 38, 53))` <span style="background: rgb(172, 38, 53)">Sample</span>.

<table>
<thead><tr><th>Colour Name</th><th>Sample</th></tr></thead>
<tbody>
    <tr><td>red</td><td style="background: red">&nbsp;</td></tr>
    <tr><td>blue</td><td style="background: blue">&nbsp;</td></tr>
    <tr><td>green</td><td style="background: green">&nbsp;</td></tr>
    <tr><td>yellow</td><td style="background: yellow">&nbsp;</td></tr>
    <tr><td>salmon</td><td style="background: salmon">&nbsp;</td></tr>
    <tr><td>orange</td><td style="background: orange">&nbsp;</td></tr>
    <tr><td>black</td><td style="background: black">&nbsp;</td></tr>
    <tr><td>white</td><td style="background: white">&nbsp;</td></tr>
</tbody>
</table>

It's worth trying other colour names and seeing what works.

## Turtle reference

Command                   | Effect
------------------------- | ----------------------------------------------
`t = turtle.Turtle()`     | Make a turtle called t
`turtle.tracer(0,0)`      | Turn off tracer animation - makes it very fast
`turtle.update()`         | Make a screen update - handy when fast
`turtle.done()`           | Program finished, wait for window to close
`t.clear()`               | Clear everything drawn by this turtle
`t.speed(0)`              | Make this turtle fast
`t.penup()`               | Pull the pen up - don't draw lines
`t.pendown()`             | Put the pen down - draw a line
`t.hideturtle()`          | Hide the turtle - don't draw it
`t.goto(x, y)`            | Jump to position x, y. 0, 0 is the middle
`t.stamp()`               | Stamp the current turtle shape
`t.shape("shape")`        | Change shape. Try "turtle", "circle", "square"
`t.shapesize(0.1)`        | Change the size of the shape
`t.color("color")`        | Change color. Try "red", "green", "blue"
`t.forward(100)`          | go forward 100 pixels
`t.left(90)`              | turn left 90 degrees
`t.right(45)`             | turn right 45 degrees
`turtle.bgcolor("black")` | Set the screen background to "black"
`turtle.window_height()`  | Get the height of the window
`turtle.window_width()`   | Get the width of the window