import turtle


wn = turtle.Screen()
wn.title("Pong by me")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

scoreA = 0
scoreB = 0


paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5.5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)


paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5.5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)


ball = turtle.Turtle()
ball.speed()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = -2


pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PlayerA: 0  PlayerB: 0", align="center", font=("Courier", 24, "normal"))

def paddleAUP():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleADown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)


def paddleBUP():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddleBDown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)

wn.listen()
wn.onkeypress(paddleAUP, "w")
wn.onkeypress(paddleADown, "z")
wn.onkeypress(paddleBUP, "i")
wn.onkeypress(paddleBDown, "m")



while True:
    wn.update()

    ball.setx(ball.xcor() + ball.dx / 11)
    ball.sety(ball.ycor() + ball.dy / 11)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    
    if ball.xcor() > 390:
        ball.goto(390, ball.ycor())  # Set x-coordinate to the right wall
        ball.dx *= -1  # Reverse x-direction
        scoreA += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(-390, ball.ycor())  # Set x-coordinate to the left wall
        ball.dx *= -1  # Reverse x-direction
        scoreB += 1
        pen.clear()
        pen.write("PlayerA: {}  PlayerB: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))


    if (ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() -40)):
        ball.dx *= -1
        ball.setx(340)

    if (ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() -40)):
        ball.setx(-340)
        ball.dx *= -1

