import turtle as t
MOVE_DISTANCE = 21
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self) -> None:
        self.s_name = "The snake from harry potter was massive so them. Basilisk I think."
        self.snake = []
        self.head = None
        self.create_snake()
        
            
    def create_snake(self) -> list:
        snake_length = 3
        color = "white"
        width = 20 #20px per block basically
        snake_shape ="square"
        
        snake_head = t.Turtle(shape=snake_shape)
        snake_head.color(color)    
        snake_head.penup()
        self.snake.append(snake_head)
        self.head = snake_head
        
        for _ in range(snake_length-1):
            self.increase_length()

    def reset(self):
        for _ in self.snake:
            _.hideturtle()
        self.snake.clear()
        self.create_snake()

    def move_upwards(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_downwards(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def set_snake_movement(self):
        screen = t.Screen()
        screen.listen()
        screen.onkey(key="Up", fun=self.move_upwards)
        screen.onkey(key="Down", fun=self.move_downwards)
        screen.onkey(key="Left", fun=self.move_left)
        screen.onkey(key="Right", fun=self.move_right)

    def move(self):
        snake = self.snake
        self.set_snake_movement()
        
        for block_num in range(len(snake)-1,0,-1):     
            new_x = snake[block_num-1].xcor()
            new_y = snake[block_num-1].ycor()
            curr_block = snake[block_num]
            curr_block.goto(new_x,new_y)
        snake[0].forward(MOVE_DISTANCE)
        

    def increase_length(self):
        previous_block = self.snake[len(self.snake)-1]
        snake_block = previous_block.clone()
        snake_block.goto(previous_block.xcor()-22,previous_block.ycor())
        previous_block = snake_block
        self.snake.append(snake_block)
    
    
