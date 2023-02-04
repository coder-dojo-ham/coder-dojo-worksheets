"""Turtle asteroids"""
import turtle
import time
import random

screen = turtle.Screen()
width, height = screen.screensize()


turtle.tracer(0,0)
turtle.listen()

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

class Scene(object):
    def __init__(self, game):
        self.game = game
        
    def first_frame(self):
        pass

    def frame(self):
        pass

    def button_pressed(self):
        pass

class CircleBoundary(object):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def setpos(self, new_pos):
        self.pos = new_pos

    def intersects(self, other):
        dist_vec = self.pos - other.pos
        return abs(dist_vec) < (self.size + other.size)
    

class Asteroid(object):
    @staticmethod
    def random_asteroid():
        return Asteroid(random.randint(-width, width), random.randint(-height, height))

    def __init__(self, x, y):
        self.size = 50
        self.x = x
        self.y = y
        self.boundary = CircleBoundary(turtle.Vec2D(x, y), self.size)
        self.heading = random.randint(0, 360)
        self.speed = 2
        self.colour = "black"

    def frame(self):
        t.penup()
        t.goto(self.x, self.y)
        t.setheading(self.heading)
        # movement
        t.forward(self.speed)
        self.x, self.y = t.position()
        # rendering
        t.right(90)
        t.pendown()
        
        t.pencolor(self.colour)
        for n in range(5):
            t.left(60)
            t.forward(self.size)

        t.left(120)
        t.forward(self.size)
        self.boundary.setpos(t.position())
        t.right(120)
        t.forward(self.size)
        t.pencolor("black")

        self.constrain()
        
    def constrain(self):
        margin = self.size + 100
        mw = width + margin
        mh = height + margin
        
        if self.x > mw:
            self.x = -mw
        elif self.x < -mw:
            self.x = mw

        if self.y > mh:
            self.y = -mh
        elif self.y < -mh:
            self.y = mh


class Player(object):
    def __init__(self):
        self.inertia = turtle.Vec2D(0, 0)
        self.p = turtle.Turtle()
        self.p.shape("turtle")
        self.p.penup()
        self.size = 5
        self.turninertia = 0
        self.thrust = 0
        self.boundary = CircleBoundary(turtle.Vec2D(0, 0), self.size)
        
    def frame(self):
        # movement
        self.p.left(self.turninertia)

        if self.thrust:
            thrust = turtle.Vec2D(1.0, 0)
            thrust = thrust.rotate(self.p.heading())
            # thrust - add a thrust vector
            # this is - vector of current heading * current inertia
            # + vector of current tilt * thrust factor
            self.inertia = self.inertia + thrust
            # position
            
        self.p.goto(self.p.position() + self.inertia)
        self.inertia *= 0.98
        self.constrain()
        self.boundary.setpos(self.p.position())
        

    def constrain(self):
        x, y = self.p.position()
        if x > width + self.size:
            x = -width
        elif x < -(width  + self.size):
            x = width

        if y > (height  + self.size):
            y = -height
        elif y < -(height + self.size):
            y = height

        self.p.goto(x, y)
            
    def left_press(self):
        self.turninertia = 5

    def leftright_release(self):
        self.turninertia = 0
        
    def right_press(self):
        self.turninertia =- 5

    def thrust_on(self):
        self.thrust = True
        
    def thrust_off(self):
        self.thrust = False
        
    
class TitleScene(Scene):
    def first_frame(self):
        self.a = [Asteroid.random_asteroid() for n in range(10)]
        self.text = turtle.Turtle()
        self.text.speed(0)
        self.text.hideturtle()
        self.text.penup()
        self.text.goto(0, 40)
        self.text.pendown()
        self.text.write("Turtleroids", align="center", font=("arial", 48, "bold"))
        self.text.penup()
        self.text.goto(0, -44)
        self.text.pendown()
        self.text.write("Press space to play", align="center", font=("arial", 24, "bold"))
                
    def frame(self):
        t.clear()
        for sprite in self.a:
            sprite.frame()
        turtle.update()

    def enter_game(self):
        self.game.set_scene("game")
        
    def setup_events(self):
        turtle.onkey(self.enter_game, "space")

    def drop_events(self):
        turtle.onkey(None, "space")


class GameScene(Scene):
    def first_frame(self):
        self.a = [Asteroid.random_asteroid() for n in range(10)]
        self.p = Player()
        self.collision = False
        
        self.text = turtle.Turtle()
        self.text.speed(0)
        self.text.hideturtle()
        self.draw_text()

    def draw_text(self):
        self.text.clear()
        self.text.penup()
        self.text.goto(-380, -380)
        self.text.pendown()
        self.text.write("Score", align="center", font=("arial", 10, "bold"))
        self.text.penup()
        if self.collision:
            self.text.goto(320, - 380)
            self.text.pendown()
            self.text.write("Collision!", align="center", font=("arial", 10, "bold"))
            self.text.penup()
            
    def frame(self):
        t.clear()
        self.p.frame()
        for sprite in self.a:
            sprite.frame()
        turtle.update()
        self.collisions()

    def end_game(self):
        self.game.set_scene("title")
        
    def setup_events(self):
        turtle.onkeyrelease(self.end_game,      "space")
        turtle.onkeypress(self.p.thrust_on,       "Up")
        turtle.onkeyrelease(self.p.thrust_off,       "Up")
                   
        turtle.onkeypress(self.p.left_press,     "Left")
        turtle.onkeypress(self.p.right_press,    "Right")
        
        turtle.onkeyrelease(self.p.leftright_release, "Left")
        turtle.onkeyrelease(self.p.leftright_release, "Right")

    def drop_events(self):
        turtle.onkey(None, "space")

    def collisions(self):
        """Detect collisions"""
        # treat player and asteroid as circles -
        # with a position and radius.
        # Circle circle.
        collision = False
        for asteroid in self.a:
            if asteroid.boundary.intersects(self.p.boundary):
                asteroid.colour = "red"
                collision = True
            else:
                asteroid.colour = "black"
        # Avoid updating text unless needed - it's really slow
        if self.collision != collision:
            self.collision = collision
            self.draw_text()
                    

class Game(object):
    def __init__(self):
        self.scenes = {
            "title": TitleScene(self),
            "game": GameScene(self),
        #    "end":  EndScene()
        }
        self.scene = None
        self.set_scene("title")

    def set_scene(self, name):
        if self.scene:
            self.scene.drop_events()

        self.scene = None
        screen.clear()
        turtle.tracer(0,0)
        
        scene = self.scenes[name]
        scene.first_frame()
        scene.setup_events()
        self.scene = scene

    def run(self):
        while True:
            if self.scene:
                self.scene.frame()
            time.sleep(1/60.0)


g = Game()
g.run()

turtle.done()
