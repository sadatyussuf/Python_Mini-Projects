import turtle,time

t = turtle.Turtle()
t.pencolor('white')

s= turtle.Screen()
s.title("Stop watch")
s.bgcolor('black')
t.hideturtle()

second_count =0
minute_count = 0
hour_count = 0
t.speed(0)
def layout(hour_count,minute_count,second_count):
    t.clear()

    t.penup()
    t.pensize(3)
    t.goto(-80,100)
    t.pencolor('white')
    t.write('STOP WATCH',font=25)
    t.goto(-100, 40)
    t.pendown()
    for i in range(2):
        t.forward(140)
        t.right(90)
        t.forward(55)
        t.right(90)
    t.penup()
    t.goto(-70, 25)
    t.pencolor('green')
    t.write('hh')

    t.goto(-70,0)
    t.pencolor('green')
    t.pendown()
    t.write(hour_count,font=25)

    t.penup()
    t.goto(-45, 0)
    t.pendown()
    t.write(':', font=25)

    t.penup()
    t.goto(-35, 25)
    t.write('mm')
    t.goto(-35,0)
    t.pendown()

    t.write(minute_count, font=25)
    t.penup()
    t.goto(-5, 0)
    t.pendown()
    t.write(':', font=25)

    t.penup()
    t.goto(5, 25)
    t.write('ss')
    t.goto(5, 0)
    t.pendown()
    t.write(second_count, font=25)


def seconds(hour_count,minute_count,second_count):
    while True:
        second_count += 1
        time.sleep(1)
        t.undo()
        t.write(second_count, font=25)

        if second_count >= 60:
            minute_count += 1
            second_count = 0
            layout(hour_count,minute_count,second_count)

        if minute_count >= 60:
            hour_count += 1
            minute_count = 0
            second_count = 0
            layout(hour_count, minute_count, second_count)


layout(hour_count,minute_count,second_count)
seconds(hour_count,minute_count,second_count)



turtle.done()