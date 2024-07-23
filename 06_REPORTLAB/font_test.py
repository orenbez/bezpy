#!/usr/bin/python
# fontSize.py  .  Helps to Measure correct font-size for page length

# LANDSCAPE page dimensions  785 x 604
# PORTRAIT page dimensions   604 x 785
# c.drawString(785,604,'Y') = TOP RIGHT CORNER (LANDSCAPE)
# c.drawString(1,1,'X')	= BOTTOM LEFT CORNER (PORTRAIT)
# c.setTitle("Title of PDF")
# print(c.getAvailableFonts()) displays to screen all the available fonts
# c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
# c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
# 1mm = 2.95 units (approx 3 units)

from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
import sys
import os


# H = 80
# I = 90
# J = 100
# K = 110

test_str = '123456789A123456789B123456789C123456789D123456789E123456789F123456789G123456789H123456789I123456789J123456789K123456789L123456789M123456789N123456789'



if __name__ == "__main__":

    portrait = True
    if portrait:
        top = 785
    else:
        top = 604

    file = 'test.pdf'

    lines_per_page = 63
    font = 'Courier'
    font_size = 10
    top_margin = 15
    left_margin = 15
    bottom_margin = 15
    
    top_row = top - top_margin
    line_skip = (top_row - bottom_margin)/lines_per_page  
    

    
    c = canvas.Canvas(file, pagesize=letter)
    c.setTitle(file)
    c.setFont(font, font_size)

    c.drawString(1, top, test_str) # Print TOP LINE
    
    row = top_row

    for i in range(1,100):
        c.drawString(left_margin, row, str(i))                
        row = row - line_skip
        if row < bottom_margin:
            break

    try:
        c.save()
        print('Saved .pdf file')
    except PermissionError:
        print("Close open .pdf file and try again")


                 
