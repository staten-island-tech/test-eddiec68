import turtle
from turtle import *
t = Turtle()

length = 5
def square(x,y):
    for i in range(4):
        t.forward(length)
        t.left(90)
        
for i in range(60):
    t.right(5)
    square(length, 90)
    length += 5
turtle.done()
