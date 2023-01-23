import turtle
from turtle import Turtle
import snake
import food


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 230)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Arial', 50, 'normal'))

        #self.score_update()

    def score_update(self):
        self.clear()
        self.goto(0, 230)
        self.hideturtle()
        self.score += 1
        self.write(arg=f"Score: {self.score}", move=False, align='center', font=('Arial', 50, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 50, "normal"))