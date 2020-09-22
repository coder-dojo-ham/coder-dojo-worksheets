"""Turtle invaders"""
import turtle
import time

class GameScene():
    def __init__(self, game):
        self.game = game
        self.t = turtle.Turtle()
        self.t.speed(0)
        #self.t.hideturtle()
        self.angle = 0
        
    def frame(self):
        self.t.reset()
        self.t.pendown()
        self.t.left(self.angle)
        self.t.forward(100)
        self.angle += 1
        
        

class Game():
    def __init__(self):
        self.scene = GameScene(self)

    def run(self):
        turtle.tracer(0, 0)
        turtle.listen()

        # main loop
        while True:
            if self.scene:
                self.scene.frame()
                turtle.update()
            time.sleep(1/60)
        
game = Game()
game.run()


