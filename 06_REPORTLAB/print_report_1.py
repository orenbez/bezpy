#!/usr/bin/python3
##############################################################################################################################################################
# Function: Displays Reports for Penny
# File Name: print_report.py
# Notes:
# https://www.actian.com/company/blog/programming-easy-way-accessing-psql-zen-database-python-odbc/
# Queries can be run directly in PSQL Control Center using the Actian (Pervasive) Database
#
# Usage:
#
# Version History:
# 10/24/2018 ONB 1st Version
#
##############################################################################################################################################################
# c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
# c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
# 1mm = 2.83 pts on the pdf document
# LANDSCAPE page dimensions  791 x 611
# PORTRAIT page dimensions   611 x 791
# c.drawString(791,611,'.') = TOP RIGHT CORNER (LANDSCAPE)
# c.drawString(0,0,'.')	= BOTTOM LEFT CORNER (PORTRAIT)
# c.setTitle("Title of PDF")
# print(c.getAvailableFonts()) displays to screen all the available fonts##############################################################################################################################################################

from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
#from PIL import Image
import sys
import os


font_size = 12
char_indent = 6
margin_indent = 15

def printOutLine(line_str, y_cord):
	c.drawString(margin_indent,y_cord,line_str)

def resetpage():
    global row
    c.setFont("Times-Bold", font_size)
    row = 715

fileName = "ExpenseReport"			  
c = canvas.Canvas(fileName + '.pdf', pagesize=letter)

#logo = ImageReader('https://www.google.com/images/srpr/logo11w.png')
logo = '.\\image\\logo.png'

# all logo coordinates AND dimensions are based on the pdf scale i.e
# full width = 604, full height = 785
c.drawImage(logo, 202, 735,width=200, height=48,mask='auto') 

string = "ACTUARIAL FEES - RATES   $2,018 $2,018 $2,018 $2,018"
resetpage()
page_number = 1

for _ in range(500):
    printOutLine(string , row)
    row = row - (font_size + 2)  # drop y-value by font-size
    if row < 50:
        printOutLine("Page: " + str(page_number) , 20)
        c.showPage()
        resetpage()
        page_number += 1


printOutLine("Last Page: " + str(page_number) , 20)
c.showPage()

try:
    c.save()
    print('End')
except PermissionError:
    print("Close " + fileName + ".pdf file and try again")
