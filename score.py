from turtle import Turtle

class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Red")
        self.penup()
        self.goto(0,260)
        self.score=0
        self.shapesize(20)
        self.write(f"Score = {self.score}", False , align="center",font=('Courier', 24, 'normal'))
        self.hideturtle()

    def increasescore(self):
        self.score+=1
        self.clear()
        self.write(f"Score = {self.score}", False , align="center",font=('Courier', 24, 'normal'))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", False , align="center",font=('Courier', 24, 'normal'))