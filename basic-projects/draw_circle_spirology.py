import turtle
wn = turtle.Screen()
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(2)

for i in range(6):
    for col in ['red','magenta','blue','cyan','green','yellow','white']:
        turtle.color(col)
        turtle.circle(100)
        turtle.left(10)
wn.mainloop()