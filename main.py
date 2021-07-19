from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Creating Screen:
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

# Creaging paddles and ball:
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Moving paddles up and down:
screen.listen()
scoreboard = Scoreboard()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Start Game:
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detecting wall collision:
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detecting paddle collision:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detecting when paddle misses:
    if ball.xcor() > r_paddle.xcor():
        ball.reset_position()
        scoreboard.l_point()
    elif ball.xcor() < l_paddle.xcor():
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
