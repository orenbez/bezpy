#! /usr/bin/python
# 
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

def	pyth (a,b):
  return sqrt(a**2 + b**2)
	
################################################################################################################

import turtle
from math import sqrt


window = turtle.Screen() # new window
turtle.bgcolor('lightyellow')
turtle.color('magenta', 'cyan')
turtle.pensize(3)
turtle.shape()

turtle.begin_fill()
turtle.circle(200)
turtle.end_fill()


mouse = turtle.Turtle()
mouse.reset()
mouse.width(1)
mouse.color('blue','green')  # object.color(x,y)  x = pen color, y = turtle color
mouse.shape("classic") # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”


cat = turtle.Turtle()
cat.reset()
cat.width(1)
cat.color('brown','orange')  # object.color(x,y)  x = pen color, y = turtle color
cat.shape("classic") # “arrow”, “turtle”, “circle”, “square”, “triangle”, “classic”


cat.left(90)
cat.forward(200)

mouse.right(90)
mouse.forward(50)


turtle.done()
window.exitonclick() # closes turtle window on click

####################################################################
