"""Turtle invaders"""
import turtle
import time
import random


class CircleBoundary(object):
    def __init__(self, pos, size):
        self.pos = pos
        self.size = size

    def goto(self, pos, y=None):
        if y:
            pos = turtle.Vec2D(pos, y)
        self.pos = pos

    def intersects(self, other):
        dist_vec = self.pos - other.pos
        return abs(dist_vec) < (self.size + other.size)


class CollisionSprite():
    def __init__(self, pos, size):
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.penup()
        self.t.goto(pos)
        self.boundary = CircleBoundary(pos, 5)

    def goto(self, pos, y=None):
        self.t.goto(pos, y)
        self.boundary.goto(pos, y)


class Bullet(CollisionSprite):
    def __init__(self, pos, heading=90, colour='black'):
        super().__init__(pos, 5)
        self.t.hideturtle()
        self.t.left(heading)
        self.t.pencolor(colour)
        self.live = True

    def frame(self):
        self.t.clear()
        self.t.forward(5)
        self.boundary.goto(self.t.position())
        if self.t.position()[1] > 400 or self.t.position()[1] < -400:
            self.die()
        else:
            self.t.dot()

    def die(self):
        self.t.clear()
        self.live = False
        self.t = None


class Alien(CollisionSprite):
    """An alien sprite is a turtle with an alien image"""
    def __init__(self, pos, scene, start_frame=0):
        super().__init__(pos, 10)
        self.t.shape("triangle")
        self.frame_count = start_frame
        self.speed = turtle.Vec2D(100/120.0, 0)
        self.scene = scene

    def frame(self):
        if self.frame_count < 120:
            self.goto(self.t.position() + self.speed)
        elif self.frame_count < 240:
            self.goto(self.t.position() -self.speed)
        else:
            self.frame_count = 0
        self.frame_count += 1
        if random.randint(0, 400) == 1:
            self.scene.add_alien_bullet(Bullet(self.t.position(), heading=-90, colour='red'))

    def die(self):
        self.t.clear()
        self.t.hideturtle()
        self.t = None


class Player(CollisionSprite):
    def __init__(self, pos, scene):
        super().__init__(pos, 10)
        self.t.shape("turtle")
        self.t.color("green")
        self.t.left(90)
        self.scene = scene
        self.moving = False
        self.dying = 0

    def die(self):
        self.t.color('red')
        self.dying = 10
        
    def frame(self):
        if self.moving:
            self.goto(self.t.position() + self.moving)
        if self.dying:
            self.dying -= 1
            if self.dying == 0:
                self.t.color('green')

    def left_press(self):
        self.moving = turtle.Vec2D(-5, 0)
        
    def right_press(self):
        self.moving = turtle.Vec2D(5, 0)

    def leftright_release(self):
        self.moving = False

    def fire(self):
        self.scene.add_player_bullet(Bullet(self.t.position()))

    
class GameScene():
    def __init__(self, game):
        self.game = game
        self.t = turtle.Turtle()
        self.t.speed(0)
        self.t.hideturtle()
        self.angle = 0
        self.wave = [Alien(turtle.Vec2D(n, 100), self) for n in range(-350, 350, 50)]
        self.wave += [Alien(turtle.Vec2D(n, 200), self, start_frame=120) for n in range(-350, 350, 50)]
        self.player = Player(turtle.Vec2D(0, -380), self)
        self.player_bullets = []
        self.alien_bullets = []

                                 
    def frame(self):
        self.player.frame()
        for alien in self.wave:
            alien.frame()
        for bullet in self.player_bullets:
            if bullet.live:
                bullet.frame()
                # Bullet alien collisions
                for alien in self.wave:
                    if alien.boundary.intersects(bullet.boundary):
                        self.wave.remove(alien)
                        alien.die()
                        bullet.die()
            else:
                self.player_bullets.remove(bullet)
        for bullet in self.alien_bullets:
            if bullet.live:
                bullet.frame()
                if self.player.boundary.intersects(bullet.boundary):
                    self.player.die()
                    bullet.die()
            else:
                self.alien_bullets.remove(bullet)
                    
                

    def add_player_bullet(self, bullet):
        self.player_bullets.append(bullet)

    def add_alien_bullet(self, bullet):
        self.alien_bullets.append(bullet)
        
    def enter_scene(self):
        turtle.onkeypress(self.player.left_press,     "Left")
        turtle.onkeypress(self.player.right_press,    "Right")
        
        turtle.onkeyrelease(self.player.leftright_release, "Left")
        turtle.onkeyrelease(self.player.leftright_release, "Right")
        turtle.onkeyrelease(self.player.fire, "space")

    def exit_scene(self):
        turtle.onkeypress(None,     "Left")
        turtle.onkeypress(None,    "Right")
        
        turtle.onkeyrelease(None, "Left")
        turtle.onkeyrelease(None, "Right")
        
class Game():
    def __init__(self):
        turtle.tracer(0, 0)
        turtle.listen()
        self.scene = None
        self.set_scene(GameScene(self))

    def set_scene(self, scene):
        if self.scene:
            self.scene.exit_scene()

        self.scene = None
        scene.enter_scene()
        self.scene = scene
        
    def run(self):

        # main loop
        while True:
            if self.scene:
                self.scene.frame()
                turtle.update()
            time.sleep(1/60)
        
game = Game()
game.run()


