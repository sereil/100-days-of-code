import turtle as t
MOVE_DISTANCE = 22
class Snake:
    
    def __init__(self) -> None:
        self.s_name = "The snake from harry potter was massive so them. Basilisk I think."
        self.s_length = 3
        self.s_color = "white"
        self.s_width = 20 #20px per block basically
        self.snake_shape ="square"
        self.snake = self.create_snake(self.snake_shape,self.s_color,self.s_length)


    
    def create_snake(self,snake_shape,color,start_size) -> list:
        snake = []

        snake_head = t.Turtle(shape=snake_shape)
        snake_head.color(color)    
        snake_head.penup()
        snake.append(snake_head)

        previous_block = snake_head
        for _ in range(start_size-1):
            snake_block = previous_block.clone()
            snake_block.goto(previous_block.xcor()-22,previous_block.ycor())
            previous_block = snake_block
            snake.append(snake_block)
        return snake    


    def move_upwards(self):
        self.snake[0].setheading(90)

    def move_downwards(self):
        self.snake[0].setheading(270)

    def move_left(self):
        self.snake[0].setheading(180)

    def move_right(self):
        self.snake[0].setheading(0)

    def move(self):
        screen = t.Screen()
        snake = self.snake
        screen.listen()
        screen.onkey(key="Up", fun=self.move_upwards)
        screen.onkey(key="Down", fun=self.move_downwards)
        screen.onkey(key="Left", fun=self.move_left)
        screen.onkey(key="Right", fun=self.move_right)
        for block_num in range(len(snake)-1,0,-1):     
            new_x = snake[block_num-1].xcor()
            new_y = snake[block_num-1].ycor()
            curr_block = snake[block_num]
            curr_block.goto(new_x,new_y)
        snake[0].forward(MOVE_DISTANCE)
        
    
        

    def increase_length(self):
        self.s_length +=1
    
    
