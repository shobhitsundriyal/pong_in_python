import turtle
#coordinate (0,0) are in the centre of the screen

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#paddle A
paddle_a = turtle.Turtle()
paddle_a.penup()
paddle_a.speed = 0
paddle_a.shape('square')
paddle_a.color('white')
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.goto(-350,0)

#paddle B
paddle_b = turtle.Turtle()
paddle_b.penup()
paddle_b.speed = 0
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.penup()
ball.speed = 0
ball.shape('square')
ball.color('white')
#ball.shapesize(stretch_len=1, stretch_wid=5)
ball.goto(0,0)
ball.dx = 0.2
ball.dy = 0.2

#Move paddle A function "On pressing certain key perform a function"
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

# Movement of paddle b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, key='w')
wn.onkeypress(paddle_a_down, key='s')
wn.onkeypress(paddle_b_up, key='Up')
wn.onkeypress(paddle_b_down, key='Down')

#Main Game loop
while True:
    wn.update()

    #update position of ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #simple boundary collisions
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1

    #paddle collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1


