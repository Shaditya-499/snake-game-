from turtle import Screen
import time
from snake import Snake
from food import Food
from score import scoreboard

s = Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("My Snake Game")
s.tracer(0)
sn = Snake()
f = Food()
scr=scoreboard()
s.listen()
s.onkeypress(sn.up,"Up")
s.onkeypress(sn.down,"Down")
s.onkeypress(sn.left,"Left")
s.onkeypress(sn.right,"Right")
gameison = True
while gameison:
    s.update()
    time.sleep(0.1)
    sn.snakemove()

    #detects collision with food
    if sn.head.distance(f)<=15:
        scr.increasescore()
        f.movefood()
        sn.longersnake()

    #detects collision with wall
    if sn.head.xcor()>290 or sn.head.xcor()<-290 or sn.head.ycor()>290 or sn.head.ycor()<-290:
        gameison=False
        scr.gameover()

    #detects collision with its own body
    for seg in sn.snakesegments[2:]:
        if sn.head.distance(seg)<=10:
            gameison=False
            scr.gameover()


s.exitonclick()
