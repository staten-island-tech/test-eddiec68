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




""" def square(x):
    for i in range(4):
        t.forward(90)
        t.left(90)
        
    for i in range(61):
    t.right(5)
    square(90) """


""" length = 5
def square(x,y):
    for i in range(4):
        t.forward(length)
        t.left(90)
        
for i in range(60):
    t.right(5)
    square(length, 90)
    length += 5
turtle.done() """

t.speed(10)
length=5
def star (x,y):
    for i in range (5):
        t.forward(length)
        t.left(144)

for i in range (60):
    star(length,144)
    length += 5
    t.right(5)
turtle.done()



