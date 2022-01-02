from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
from time import sleep


'''
TODO
    create screen
    create snake body
    movethe snake
    create the food
    detect collision with food
    create a score board 
    detect collision with wall
    detect collision with body
'''
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snakemania')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()
    sleep(0.1)
    snake.move()

    # Detect collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_on = False
        scoreboard.game_over()
       
    # Detect collision with body or tail
    for body in snake.body[1:]:
        if snake.head.distance(body) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()
if __name__ == "__main__":
    # main()
    pass
