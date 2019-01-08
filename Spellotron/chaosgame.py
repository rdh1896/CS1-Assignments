import turtle as tt
import random as rand
import math

def setup():
    tt.speed(0)
    tt.pensize(2)
    tt.up()
    tt.goto(-200, -200)
    tt.down()
    tt.circle(1)
    tt.up()
    tt.goto(200, -200)
    tt.down()
    tt.circle(1)
    tt.up()
    tt.goto(0, 346.410161514 - 200)
    tt.down()
    tt.circle(1)
    tt.up()

def execute():
    tt.goto(0, -200)
    tt.down()
    tt.circle(1)
    tt.up()
    while True:
        pos = tt.pos()
        pos = (pos[0], pos[1])
        pointA = (-200, -200)
        pointB = (200, -200)
        pointC = (0, 346.410161514 - 200)
        roll = rand.randint(1, 6)
        if roll == 1 or roll == 2:
            distance = tt.distance(pointA[0], pointA[1]) / 2
            tt.left(tt.towards(pointA[0], pointA[1]) - tt.heading())
            tt.fd(distance)
            tt.down()
            tt.circle(1)
            tt.up()
        elif roll == 3 or roll == 4:
            distance = tt.distance(pointB[0], pointB[1]) / 2
            tt.left(tt.towards(pointB[0], pointB[1]) - tt.heading())
            tt.fd(distance)
            tt.down()
            tt.circle(1)
            tt.up()
        else:
            distance = tt.distance(pointC[0], pointC[1]) / 2
            tt.left(tt.towards(pointC[0], pointC[1]) - tt.heading())
            tt.fd(distance)
            tt.down()
            tt.circle(1)
            tt.up()

setup()
execute()