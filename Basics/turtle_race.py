import time,turtle
from turtle import Turtle
from random import randint

#window setup
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor('forestgreen')
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140,200)
turtle.write("TURTLE RACE",font=('Arial',30,'bold'))
turtle.penup()


#DIRC
turtle.setpos(-400,-100)
turtle.color('chocolate')
turtle.begin_fill()
turtle.pendown()
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(800)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()

#FINISH LINE
stamp_size = 20
square_size = 15
finish_line = 200

turtle.color('black')
turtle.shape('square')
turtle.shapesize(square_size/stamp_size)
turtle.penup()

for i in range(10):
    turtle.setpos(finish_line,(150-(i * square_size * 2)))
    turtle.stamp()

for j in range(10):
    turtle.setpos(finish_line+ square_size,((150- square_size)-(j * square_size * 2)))
    turtle.stamp()
#turtle.hideturtle()


#turtle 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.shape('turtle')
turtle1.color('black')
turtle1.penup()
turtle1.setpos(-250,100)
turtle1.pendown()


#turtle 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.shape('turtle')
turtle2.color('cyan')
turtle2.penup()
turtle2.setpos(-250,50)
turtle2.pendown()


#turtle 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.shape('turtle')
turtle3.color('magenta')
turtle3.penup()
turtle3.setpos(-250,0)
turtle3.pendown()

#turtle 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.shape('turtle')
turtle4.color('yellow')
turtle4.penup()
turtle4.setpos(-250,-50)
turtle4.pendown()


time.sleep(1) # pause the game for one second before the race begins

#Move The Turtles
for i in range(150):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1, 5))
    turtle3.forward(randint(1, 5))
    turtle4.forward(randint(1, 5))

turtle.exitonclick()
window.mainloop()