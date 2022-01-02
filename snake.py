from turtle import Turtle

class Snake:
    STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
    MOVE = 20
    UP = 90
    DOWN = 270
    RIGHT = 0
    LEFT = 180

    def __init__(self) -> None:
        self.body = []
        self. create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for pos in self.STARTING_POSITIONS:
           self.add_body(pos)

    def add_body(self, pos):
        snake_body = Turtle('square')
        snake_body.color('white')
        snake_body.penup()
        snake_body.goto(pos) 
        self.body.append(snake_body)

    def extend(self):
        self.add_body(self.body[-1].position())

    def move(self):
        for bdy_num in range(len(self.body) - 1, 0, -1):
            new_x = self.body[bdy_num - 1].xcor()
            new_y = self.body[bdy_num - 1].ycor()
            self.body[bdy_num].goto(new_x, new_y)

        self.body[0].forward(20)

    def left(self):
        if self.head.heading() != self.RIGHT:
            self.body[0].setheading(self.LEFT)

    def right(self):
        if self.head.heading() != self.LEFT:
            self.body[0].setheading(self.RIGHT)

    def up(self):
        if self.head.heading() != self.DOWN:
            self.body[0].setheading(self.UP)

    def down(self):
        if self.head.heading() != self.UP:
            self.body[0].setheading(self.DOWN)

