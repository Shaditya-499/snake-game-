from turtle import Turtle

STARTINGPOSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVEDISTANCE = 20


class Snake:
    def __init__(self):
        self.snakesegments = []
        self.snakemake()
        self.head=self.snakesegments[0]

    def snakemake(self):
        for position in STARTINGPOSITION:
            self.addsegement(position)

    def snakemove(self):
        for seg_i in range(len(self.snakesegments) - 1, 0, -1):
            newx = self.snakesegments[seg_i - 1].xcor()
            newy = self.snakesegments[seg_i - 1].ycor()
            self.snakesegments[seg_i].goto(newx, newy)
        self.snakesegments[0].forward(10)

    def addsegement(self,position):
        segment = Turtle("square")
        segment.penup()
        segment.color("white")
        segment.goto(position)
        self.snakesegments.append(segment)

    def longersnake(self):
        self.addsegement(self.snakesegments[-1].position())

    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)