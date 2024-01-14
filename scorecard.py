from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_card = 0
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-70, 270)
        self.color('white')
        self.evaluate()

    def evaluate(self):
        self.clear()
        message = " score = " + str(self.score_card)
        self.write(message, move=False, font=('Arial', 20, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over.", align="center", move=False, font=('Arial', 24, 'normal'))

