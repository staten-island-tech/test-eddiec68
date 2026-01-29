import turtle
from turtle import *
t = Turtle()

""" def rectangle(x):
    t.forward(x)
    t.left(90)
    t.forward(100)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(100)
    t.left(90)
rectangle(125) """


""" def equaltriangle(x):
    t.forward(x)
    t.left(120)
    t.forward(x)
    t.left(120)
    t.forward(x)
equaltriangle(90)  """

""" turtle.done() """

def square(x):
    for i in range(4):
        t.forward(90)
        t.left(90)
        

for i in range(61):
    t.right(5)
    square(90)
