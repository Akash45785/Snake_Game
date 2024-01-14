from turtle import Turtle, Screen
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

position = [(0, 0), (-20, 0), (-40, 0)]
screen = Screen()


class Snake:
    def __init__(self):
        self.segment = []
        for cord in position:
            self.adding(cord)

        self.head = self.segment[0]

    def adding(self, place):
        segment1 = Turtle()
        segment1.penup()
        segment1.shape('square')
        segment1.color('white')
        segment1.goto(place)
        self.segment.append(segment1)

    def extend(self):
        pos = self.segment[-1].position()
        self.adding(pos)

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)

        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()
