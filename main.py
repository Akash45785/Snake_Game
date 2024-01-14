from turtle import Screen
from food import Food
from scorecard import Score
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("green")
screen.title("Snake Game ")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.left, "Left")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")

is_alive = 1
while is_alive:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_card += 1
        score.evaluate()
        snake.extend()

# collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_alive = 0
        score.game_over()

#  collision with itself
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            is_alive = 0
            score.game_over()

screen.exitonclick()

