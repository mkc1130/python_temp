import turtle
t = turtle.Turtle()
t.shape("classic")

t.penup()               # 펜을 올려서 그림이 그려지지 않게한다.
t.goto(100, 100)        # 포인터를 (100, 100)으로 이동시킨다.
t.color("red")
t.write("포인터가 여기로 오면 양수입니다.")
t.goto(100, 0)
t.color("black")
t.write("포인터가 여기로 오면 0입니다.")
t.goto(100, -100)
t.color("blue")
t.write("포인터가 여기로 오면 음수입니다.")
while (1) :
    t.color("black")
    t.goto(0, 0)            # (0, 0) 위치로 포인터를 이동시킨다.
    t.pendown()             # 펜을 내려서 그림이 그려지게 한다.
    s = int(turtle.textinput("", "숫자를 입력하시오 "))

    if( s > 0 ) :
        t.color("red")
        t.goto(100, 100)
        t.penup()
    if( s == 0 ) :
        t.color("black")
        t.goto(100, 0)
        t.penup()
    if( s < 0 ) :
        t.color("blue")
        t.goto(100, -100)
        t.penup()
