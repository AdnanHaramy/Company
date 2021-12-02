import turtle
window = turtle.Screen()
window.title("Ping Pong Game By Rama")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

score_a = 0
score_b = 0

paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.speed(0)
paddle_a.penup()
paddle_a.goto(-350, 0)


paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.speed(0)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.color("white")
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.goto(0, 0)
ball.dx = 3
ball.dy = 0.1

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.goto(0, 260)
score.hideturtle()
score.write("Player A : 0 Player B : 0 ", align="center",
            font=("Courier", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    if y <= 240:
        paddle_a.sety(y)
    else:
        paddle_a.sety(240)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    if y <= 240:
        paddle_b.sety(y)
    else:
        paddle_b.sety(240)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    if y >= -230:
        paddle_a.sety(y)
    else:
        paddle_a.sety(-230)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    if y >= -230:
        paddle_b.sety(y)
    else:
        paddle_b.sety(-230)


window.listen()
window.onkey(paddle_a_up, "w")
window.onkey(paddle_b_up, "Up")
window.onkey(paddle_a_down, "s")
window.onkey(paddle_b_down, "Down")


while True:
    window.update()
    print(ball.ycor())
    print(paddle_b.ycor())
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() > 390:
        score_a += 1
        score.clear()
        score.write("Player A : {} Player B : {} ".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if ball.xcor() < -390:
        score_b += 1
        score.clear()
        score.write("Player A : {} Player B : {} ".format(score_a, score_b), align="center",
                    font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
