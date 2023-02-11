import turtle,time,random

segments = []
highscore =0
score =0
counter = 0
#screen
screen = turtle.Screen()
screen.title("Snake Game by Sadat")
screen.bgcolor('green')
screen.setup(width=700,height=700)
screen.tracer(0)



#food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.shapesize(0.50, 0.50)
food.penup()
food.goto(30, 0)


# food_extra
food_extra = turtle.Turtle()
food_extra.speed(0)
food_extra.shape('circle')
food_extra.color('red')
food_extra.shapesize(2)
food_extra.penup()
food_extra.goto(100, 100)
#food_extra.hideturtle()

#Snake Head
snake = turtle.Turtle()
snake.speed(0)
snake.shape('square')
snake.color('black')
snake.shapesize(1)
snake.penup()
snake.direction = 'stop'

#border
border = turtle.Turtle()
border.hideturtle()
border.speed(0)
border.pencolor('black')
border.pensize(3)
border.penup()
border.goto(-300,300)
border.pendown()
for i in range(4):
    border.forward(600)
    border.right(90)


# score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 300)
pen.write("Score: {} High Score: ".format(score), align="center", font=("Courier", 24, "normal"))



def move_segments():
    # move the end segment in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    if snake.direction == 'up':
        y = snake.ycor()
        y += 10
        snake.sety(y)


    if snake.direction == 'down':
        y = snake.ycor()
        y -= 10
        snake.sety(y)

    if snake.direction == 'right':
        x = snake.xcor()
        x += 10
        snake.setx(x)

    if snake.direction == 'left':
        x = snake.xcor()
        x -= 10
        snake.setx(x)


def food_pos():
    global  score,highscore,counter
    X = random.randint(-280, 280)
    Y = random.randint(-280, 280)

    if  snake.distance(food)<15:
        #the food should change to a random position on the screen
        food.goto(X, Y)
        # adding the snake's body segment
        segment = turtle.Turtle()
        segment.speed(0)
        segment.shape('square')
        segment.color('grey')
        segment.penup()
        segments.append(segment)

       #Keeping track of the score
        score+=1
        pen.undo()
        pen.write("Score: {} High Score: {}".format(score, highscore), align="center",
                  font=("Courier", 24, "normal"))
        if score > highscore:
            #updating the highscore
            highscore += 1
            pen.undo()
            pen.write("Score: {} High Score: {}".format(score, highscore), align="center",
                      font=("Courier", 24, "normal"))


    #hide the bonus food untill the condition below is met
    food_extra.hideturtle()
    if score!=0 and score%2==0:
        #since the condition is met show the bonus food
        food_extra.showturtle()

        counter+=1
        pen.undo()
        pen.write("Score: {} High Score: {} counter: {}".format(score, highscore, counter), align="center",
                  font=("Courier", 24, "normal"))
        if counter == 30:
            counter = 0
            score += 1
            highscore +=1
            pen.undo()
            pen.write("Score: {} High Score: {} counter: {}".format(score, highscore, counter), align="center",
                      font=("Courier", 24, "normal"))
            food_extra.goto(X, Y)
            food_extra.hideturtle()

        if snake.distance(food_extra) < 30:
            food_extra.goto(X, Y)
            counter = 0
            score += 3
            highscore += 3
            pen.undo()
            pen.write("Score: {} High Score: {} counter: {}".format(score, highscore, counter), align="center",
                      font=("Courier", 24, "normal"))
            food_extra.hideturtle()

    move_segments()




def boundry_col():
    x = snake.xcor()
    y = snake.ycor()
    global  segments,score
    if (x==290 or x==-290) or (y == 290 or y == -290):

        time.sleep(1)
        snake.goto(0,0)
        food.goto(30, 0)
        snake.direction = 'stop'


        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        #clear segment list
            segments =[]

      #After collosion reset the score
        score = 0
        pen.undo()
        pen.write("Score: {} High Score: {}".format(score, highscore), align="center", font=("Courier", 24, "normal"))

def body_col():
    global segments
    for segment in segments:
        if segment.distance(snake)==0:
            time.sleep(1)
            snake.goto(0, 0)
            food.goto(30, 0)
            snake.direction = 'stop'

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
                # clear segment list
                segments = []



            # After collosion reset the score
            score = 0
            pen.undo()
            pen.write("Score: {} High Score: {}".format(score, highscore), align="center",
                          font=("Courier", 24, "normal"))

    pass
def move_snake_up():
    if snake.direction != 'down':
        snake.direction = 'up'

def move_snake_down():
    if snake.direction != 'up':
        snake.direction = 'down'



def move_snake_right():
    if snake.direction != 'left':
        snake.direction = 'right'


def move_snake_left():
    if snake.direction != 'right':
        snake.direction = 'left'



#Keyboard binding
screen.listen()
screen.onkey(move_snake_up, 'Up')
screen.onkey(move_snake_left, 'Left')
screen.onkey(move_snake_right, 'Right')
screen.onkey(move_snake_down, 'Down')



while True:
    boundry_col()
    body_col()

    food_pos()


    screen.update()
    time.sleep(0.1)
