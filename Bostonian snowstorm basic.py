import random
from turtle import*
pencolor("white")
shape("classic")
speed(10)
pensize(5)
Screen().bgcolor("blue")
def vshape(size):
    right(25)
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
def snowflakearm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)
def snowflake(size):
    for y in range(0,6):
        snowflakearm(size)
        right(60)
for i in range(0,12):
    size=random.randint(5,10)
    x=random.randint(-300,300)
    y=random.randint(-300,300)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)

    
    




