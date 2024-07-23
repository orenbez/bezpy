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
#Draws an octagon with turtle 'x', side lenght 'y'
def oct (x,y):            
  for i in [1,2,3,4,5,6,7,8]:
    x.right(45)
    x.forward(y)


################################################################################################################

import turtle


turtle.speed(1) # doesn't seem to change the speed

tony = turtle.Turtle()
tony.reset()
tony.width(2)
tony.color('purple','orange')

lsqu (tony,100)
tony.forward(100)
tony.pu()
tony.left(90)
tony.forward(100)
tony.pd()
oct(tony,100)
tony.pu()
tony.right(45)
tony.forward(100)
tony.right(45)
tony.pd()
lsqu(tony,100)
tony.pu()
tony.forward(100)
tony.right(45)
tony.forward(100)
tony.right(45)
tony.pd()
lsqu(tony,100)
tony.pu()
tony.forward(100)
tony.right(45)
tony.forward(100)
tony.left(45)
tony.pd()
rsqu(tony,100)



# tony.begin_fill()

# for i in [1,2,3,4]:
  # tony.forward(100)
  # tony.right(90)

# tony.color('blue')
# tony.end_fill()

# tony.reset()

# x=200
# for i in range(40):
  # tony.forward(x)
  # tony.right(90)
  # x = x - 5


turtle.done()



