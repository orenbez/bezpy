#! /usr/bin/python
# Turtle functions http://interactivepython.org/runestone/static/IntroPythonTurtles/Summary/summary.html
################################################################################################################
#Draws a square with turtle 'x',  side length = y
def lsqu (x,y):            
  for i in [1,2,3,4]:
    x.forward(y)
    x.left(90)
def rsqu (x,y):            
  for i in [1,2,3,4]:
    x.forward(y)
    x.right(90)	
#Draws an octagon with turtle 'x', side length 'y'
def oct (x,y):            
  for i in [1,2,3,4,5,6,7,8]:
    x.right(45)
    x.forward(y)
################################################################################################################

import turtle


tony = turtle.Turtle()
tony.reset()
tony.begin_fill()
tony.width(1)
tony.color('purple','green')  # object.color(x,y)  x = pen color, y = turtle color
tony.shape("turtle")

x=100
for _ in range(18):  # y = 0,1,2,3, ... , 17
  x = x - 5
  rsqu (tony,x)
  tony.right (20)

tony.end_fill()   # fill color is the turtle color
  
turtle.done()



