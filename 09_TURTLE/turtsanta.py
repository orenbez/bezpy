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


####################################################################
################# PROGRAM TO DRAW SANTA'S HOUSE ####################
####################################################################
tony = turtle.Turtle()
tony.reset()

tony.width(3)
tony.color('red','white')  # object.color(x,y)  x = pen color, y = turtle color
tony.shape("turtle")

diag = pyth(100,100)

print(tony.heading())
print(tony.position())

tony.left(90)
lsqu(tony,100)
print(tony.heading())


tony.left(45)
tony.forward(diag)
tony.right(90)
tony.forward(diag/2)
tony.right(90)
tony.forward(diag/2)
tony.right(90)
tony.forward(diag)


print(tony.heading())
print(tony.position())

tony.end_fill()  
turtle.done()

####################################################################
