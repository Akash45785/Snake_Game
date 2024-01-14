from turtle import Turtle
from random import randint
L_END = -270
R_END = 270


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.color("black")
        self.refresh()

    def refresh(self):
        x_random = randint(L_END, R_END)
        y_random = randint(L_END, R_END)
        self.goto(x_random, y_random)
