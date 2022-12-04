---
title: Python Turtle Raindrops
---
<link rel="stylesheet" href="../css/sheet.css">

<table class="key_info">
<tr><td>Level: Intermediate</td>
<td>Language: Python</td>
<td>Requires: Laptop with Python</td></tr>
</table>

<img src="inspiration-rain-lake-screenshot.png" class="leader_picture"/>

We'll use python and turtle to make it rain. Once you've got it raining,
have a go at making other things move around on the screen.

The drops could be snow, stars, faces or footballs.

We'll use some elements you've seen - variables, random numbers
and functions.

We'll be introducing one new element - lists.

And you'll get to do some simple animation! Stuff that moves!

This sheet recommends using Mu in Python 3 mode.

<!-- -- id="draw-raindrop" -->
## Drawing a raindrop

Lets start by setting up turtle to draw fast with `speed(0)`, hide the turtle with `hideturtle`, and pull up the pen with `penup`.

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

![Drawing 3 drops](drawing-3-drops.png) \

## More rain
<!-- -- id="more-rain" -->
There are many raindrops in rain. Let's use a list to hold them:

<pre><code><del>draw_drop(0, 0)
draw_drop(30, -40)
draw_drop(50, 20)
</del>
<b>drops = [[0, 0], [30, -40], [50, 20]]</b>

for drop in drops:
    draw_drop(drop[0], drop[1])
</code></pre>

Drops is a list of (x,y) pairs - each a small list too. When we draw this - x is drop[0] and y is drop[1]. This should show the same 3 drops as before, but you can change the list to add more drops.

### Random rain

Now we can make the list bigger. Let's add 100 raindrops using `random` to scatter them around the screen. First we need to import random at the top of our code:

<pre><code>
import turtle
<b>import random</b>
</code></pre>

Then we replace our fixed list with an empty list, and fill it with random drop positions:

<pre><code>
<del>drops = [[0, 0], [30, 40], [50, 20]]</del>
<b>drops = []
for n in range(100):
    drop = [random.randint(-400, 400), random.randint(-400, 400) ]
    drops.append(drop)
</b>
for drop in drops:
    draw_drop(drop[0], drop[1])
</code></pre>

![many raindrops screenshot](many-raindrops.png) \

Each time you run it - you'll get different drops!

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

## Preparing to animate
<!-- -- id="prep-animate" -->

You may have noticed that drawing the drops was a bit slow - one drop at a time. If we are going to animate this, we need to be able to draw a lot faster. Add the bold line near the top of the file.
Note that this should be `turtle` and not `t`.
<pre><code>import turtle
import random

<b>turtle.tracer(0, 0)</b>
t = turtle.Turtle()
t.speed(0)
</code></pre>

This tells the turtle not to animate itself, so we can animate instead.
This will be very quick, but it's actually drawn on a background/hidden screen. To actually see it you'll need to add this at the end of the code:

<pre><code>for drop in drops:
    draw_drop(drop[0], drop[1])

<b>turtle.update()</b></code></pre>

This will now make the random raindrops draw much faster.

## Moving the raindrops

We can start to make these raindrops move now.

<pre><code>
drops = []
for n in range(100):
    drop = [random.randint(-400, 400), random.randint(-400, 400) ]
    drops.append( drop )

<del>for drop in drops:
    draw_drop(drop[0], drop[1])

turtle.update()
</del>
<b>while True:
    t.clear()
    for drop in drops:
        drop[1] -= 3
        draw_drop(drop[0], drop[1])
    turtle.update()</b>
</code></pre>

Our animation is in the while loop. It clears the drawings, then moves them down by 3 (subtracting 3 from Y), and draws the drop.

After drawing all drops, we update the screen. This makes a different picture every time, which will look like the drops are moving.

You'll note all the drops fall off the screen here. You may see an "invalid command name" and a large number when you close the window, don't worry - this can be ignored for now.

## Rain from the top again

We can stop them falling off. The bottom of the screen here is -400. So if we are below that, we can put them back at the top. Add the following in the loop after we subtract 3 from the drop y:

<pre><code>
   for drop in drops:
        drop[1] -= 3<b>
        if drop[1] < -400:
            drop[1] = 400</b>
        draw_drop(drop[0], drop[1])
    turtle.update()
</code></pre>

## Checkpoint 2

Your code at this point should look like this:

```python
import turtle
import random

turtle.tracer(0, 0)
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

while True:
    t.clear()
    for drop in drops:
        drop[1] -= 3
        if drop[1] < -400:
            drop[1] = 400
        draw_drop(drop[0], drop[1])
    turtle.update()
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

### Background images

You can use `turtle.bgcolor` near the top of the code to change the background colour, or you can use a GIF or PNG as a background image:

<pre><code>
import turtle
import random
<b>
screen = turtle.Screen()
screen.bgpic("lake-background.gif")
</b>
turtle.tracer(0, 0)
t = turtle.Turtle()
</code></pre>

<img src="inspiration-rain-lake-screenshot.png" style="height: 200px; margin-right: 10px"><img src="inspiration-space-scene.png" style="height: 200px">

You can create a rainy, space or snowy scenes. Making the dots small with a space background. Get creative!

Stars:

```python
t.shape("circle")
t.color("lightblue")
turtle.bgcolor("black")
screen = turtle.Screen()
screen.bgpic("space-background.png")
t.shapesize(0.1)
```

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