#! /usr/bin/python
# Turtle functions http://interactivepython.org/runestone/static/IntroPythonTurtles/Summary/summary.html

import turtle


tony = turtle.Turtle()
tony.reset()
tony.width(2)
tony.color('purple','orange')
tony.begin_fill()

for i in [1,2,3,4]:
  tony.forward(100)
  tony.right(90)

tony.color('blue')
tony.end_fill()

tony.reset()

x=200
for i in range(40):
  tony.forward(x)
  tony.right(90)
  x = x - 5


turtle.done()



