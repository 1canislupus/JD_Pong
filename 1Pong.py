import turtle as t
import os
import pygame
from pygame import mixer

pygame.init()
pygame.mixer.init()

wall_hit_sound = pygame.mixer.Sound("button_10.wav")


# playerAscore = 0
# playerBscore = 0
player_a_score = 0
player_b_score = 0

window = t.Screen()
window.title("JD Pong")
window.bgcolor("blue")
window.setup(width=800, height=600)
window.tracer(0)

leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("yellow")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(5, 5)
ballxdirection = 0.2
ballydirection = 0.2
ball_dx = 1

pen = t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("score", align="center", font=('Arial', 24, 'normal'))



# code for moving the leftpaddle
def leftpaddleup():
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sety(y)


def leftpaddledown():
    y = leftpaddle.ycor()
    y = y + 90
    leftpaddle.sety(y)


# code for moving the rightpaddle
def rightpaddleup():
    y = rightpaddle.ycor()
    y = y + 90
    rightpaddle.sety(y)


def rightpaddledown():
    y = rightpaddle.ycor()
    y = y + 90
    rightpaddle.sety(y)


window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'p')
window.onkeypress(rightpaddledown, 'l')
# window.onkeypress(rightpaddleup,'Up')
# window.onkeypress(rightpaddledown,'Down')

while True:
    window.update()

    # moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballxdirection)

    # border set up
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection = ballydirection * -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection = ballydirection * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        #os.system("afplay wallhit.wav&")
        wall_hit_sound.play()

    if (ball.xcor()) < -390:  # Left width paddle Border
        ball.goto(0, 0)
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(player_a_score, player_b_score),
                  align="center", font=('Monaco', 24, "normal"))
        #os.system("afplay wallhit.wav&")
        wall_hit_sound.play()

    # Handling the collisions with paddles.

    hit_sound_played = False

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        if not hit_sound_played:
            wall_hit_sound.play()
            hit_sound_played = True
        ball.setx(340)
        ball_dx = ball_dx * -1
        #os.system("afplay paddle.wav&")
        wall_hit_sound.play()

    else:
        hit_sound_played = False


    hit_sound_played = False

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        if not hit_sound_played:
            wall_hit_sound.play()
            hit_sound_played = True
        ball.setx(-340)
        ball_dx = ball_dx * -1
        #os.system("afplay paddle.wav&")
        wall_hit_sound.play()

    else:
        hit_sound_played = False

