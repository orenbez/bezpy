from turtle import *
from random import *

setworldcoordinates(-100, -200, 200, 200)
ht(); speed(0); color('blue')

drops = 500  # increase number of drops for better approximation
hits = 0    # hits counter

# draw parallel lines with distance 20 between adjacent lines
for i in range(0, 120, 20): 
    pu(); setpos(0, i); pd()
    fd(100) # length of line

# throw needles
color('red')
for j in range(drops):
    pu()
    goto(randrange(10, 90), randrange(0,100))
    y1 = ycor() # keep ycor of start point
    seth(360*random())
    pd(); fd(20)    # draw needle of length 20
    y2 = ycor() # keep ycor of end point

    if y1//20 != y2//20:    # decisive test: if it is a hit then ...
        hits += 1       # increase the hits counter by 1

print(2 * drops / hits)