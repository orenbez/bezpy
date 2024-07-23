#!/usr/bin/python
# fontSize.py  .  Helps to Measure correct font-size for page length

# c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
# c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
# 1mm = 2.83 pts on the pdf document
# LANDSCAPE page dimensions  791 x 611
# PORTRAIT page dimensions   611 x 791
# c.drawString(791,611,'.') = TOP RIGHT CORNER (LANDSCAPE)
# c.drawString(0,0,'.')	= BOTTOM LEFT CORNER (PORTRAIT)
# c.setTitle("Title of PDF")
# print(c.getAvailableFonts()) displays to screen all the available fonts
# For all fonts FontSize = 10 => height of font = 5 pts  = 5 x 2.83 mm

from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
import sys
import os

def print_fonts():
	x = 500
	c.setTitle("print coords")
	for font in c.getAvailableFonts():
		if font == 'Symbol':
			line = '\u03BE\u0394\u0023\u03BC\u2287\u2202\u2261'  # see https://en.wikipedia.org/wiki/Symbol_(typeface)
		elif font == 'ZapfDingbats':  # see https://en.wikipedia.org/wiki/Zapf_Dingbats
			line = '\u27BD\u2785\u260E\u2702\u2714\u2718\u261B\u2709'
		else:
			line = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ abcdefghijklmnopqrstuvwxyz\u27BD\u2785\u260E\u261B\u2709\u03BE\u0394\u0023\u03BC\u2287'
		c.setFont('Helvetica', 14)
		c.drawString(margin_indent, x, font)
		c.setFont(font, 14)
		c.drawString(200, x, line)
		x = x - 16  # a bit more than the font-size
	c.showPage()  # ends page
	try:
		c.save()
		print('Saved .pdf file')
	except PermissionError:
		print("Close .pdf file and try again")

def print_page():
	row = 500
	x = margin_indent
	c.setTitle("print_page")
	for font_size in range(7,40):
		c.setFont("Times-Roman", font_size)
		c.drawString(x, row, 'font size = ' + str(font_size) + ":" +  line)
		row = row - font_size - 2  # a bit more than the font-size
		x = x + 1
	c.showPage() #ends page
	try:
		c.save()
		print('Saved .pdf file')
	except PermissionError:
		print("Close open .pdf file and try again")

def print_cords():
	c.setTitle("print coords")
	c.setFont("Courier-Bold", 7)
	for x in range(1,604,45):
		for y in range(1,785,10):
			c.drawString(x, y, f'x({x},{y})')
	c.showPage() #ends page
	try:
		c.save()
		print('Saved .pdf file')
	except PermissionError:
		print("Close open .pdf file and try again")

def print_font_sizes():
	x = 791
	c.setTitle("print font size")
	for size in range(1,50):
		line = f'Font Size = {size}, line skip = {size}'
		c.setFont('Courier', size)
		c.drawString(margin_indent, x, line)
		x = x - size
	c.showPage()  # ends page
	try:
		c.save()
		print('Saved .pdf file')
	except PermissionError:
		print("Close .pdf file and try again")

########################################################################################################################

if __name__ == "__main__":
	margin_indent = 15
	line ='123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890'

	#SET UP FOR LANDSCAPE
	c = canvas.Canvas('landscape.pdf', pagesize=landscape(letter))
	print_page()

	#SET UP FOR PORTRAIT
	c = canvas.Canvas('portrait.pdf', pagesize=letter)
	print_page()

	# NOTE - you never need to use ZapfDingbats or 'symbol' fonts as their characters can print in any font using Unicode
	c = canvas.Canvas('fonts.pdf', pagesize=landscape(letter))
	print_fonts()

	#SET UP FOR PORTRAIT
	c = canvas.Canvas('coordinates.pdf', pagesize=letter)
	print_cords()


	#SET UP FONT SIZE
	c = canvas.Canvas('font_size.pdf', pagesize=letter)
	print_font_sizes()




