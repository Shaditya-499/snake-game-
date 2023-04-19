from turtle import Turtle
import random
from snake import Snake

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed("fastest")
        self.movefood()

    def movefood(self):
        randomx = random.randint(-290, 290)
        randomy = random.randint(-290, 290)
        self.goto(randomx, randomy)
