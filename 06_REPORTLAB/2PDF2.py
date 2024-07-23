#!/usr/bin/python
# CONVERTS SPECIFIED FILE TO PDF
# 02/28/2018 ONB 1st Version - Converts Wang Report text files to .pdf
# 02/29/2018 ONB Requests source directory from the command line
# 03/09/2018 ONB Calibrates font based on length of longest line
# 03/23/2018 ONB Adjusted font size based on results of fontsize.py
#            ONB Changed for only specific file passed


from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image
import sys  #used for sys.exit() or to retrieve command line arguments
import os


def printOutLine(line_str, y_cord):
	c.drawString(margin_indent,y_cord,line_str)


#LANDSCAPE page dimensions  785 x 604
#PORTRAIT page dimensions   604 x 785
#c.drawString(785,604,'Y') = TOP RIGHT CORNER (LANDSCAPE)
#c.drawString(1,1,'X')	= BOTTOM LEFT CORNER (PORTRAIT)
# print(c.getAvailableFonts()) displays to screen all the available fonts

font_size = 10
char_indent = 6
margin_indent = 15

#files = sys.argv[1:]  
# src = input("Please enter source directory path e.g. \"D:\TSCDIRECT\TSC111\#P030118\": ") 
# if(os.path.exists(src) == False):
	# print("This path is invalid, please try again.")
	# sys.exit()
# if(os.path.exists(src + '\pdf') == False):	
	# os.mkdir(src + '\pdf')
	

src = os.environ['SRC_PATH']	   # path only
file = os.environ['SRC_FILE_PATH'] # full path with extension
fileName = os.environ['SRC_FILE']  # extension removed
dest =  os.environ['DST_FILE_PATH']	 # new full path with pdf file name.

os.chdir(src) # it is required to change working directory in python
			  # just passing the full path is not sufficient for some reason

if os.path.isfile(file) == True:
	if (os.stat(file).st_size == 0):
		print(file, "is empty")
	with open(file, "r") as f_obj:
		lines = f_obj.readlines()
	# WILL USE TO DETERMINE THE LONGEST LINE
	line_lengths = []
	for line in lines:
		line_lengths.append(len(line))
	maxl = max(line_lengths)	
	if(maxl > 91 ): #SET UP FOR LANDSCAPE
		c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
		top_row = 580
	else: #SET UP FOR PORTRAIT
		c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
		top_row = 760

	if maxl > 127: #LANDSCAPE
		font_size = 9
	elif maxl > 116: #LANDSCAPE
		font_size = 10
	elif maxl > 106: #LANDSCAPE
		font_size = 11			
	elif maxl > 98: #LANDSCAPE
		font_size = 12
	elif maxl > 91: #LANDSCAPE
		font_size = 13			
	elif maxl > 86: #PORTRAIT
		font_size = 10
	elif maxl > 81: #PORTRAIT
		font_size = 11
	elif maxl > 73: #PORTRAIT
		font_size = 12
	elif maxl > 69: #PORTRAIT
		font_size = 13			
	else:           #PORTRAIT
		font_size = 14	
		
	c.setLineWidth(.3)
	c.setFont("Courier", font_size)
	page_number = 1
	row = top_row  #TOP ROW
	# lineNum = 1
	for line in lines:
		#START LINE
		PAGE_BREAK_FLAG = 'F'
		for i in line:
			if (i == '\x0c'):   # FORM FEED = NEW PAGE 
				PAGE_BREAK_FLAG = 'T'
				if page_number > 1: # ignore first page break
					c.showPage() #ends page since found file_break_char
				page_number += 1
				row = top_row
				c.setLineWidth(.3)
				c.setFont("Courier", font_size)
			else:
				pass
		if (PAGE_BREAK_FLAG == 'T'):
			line = line[1:]	  #removes next page char
		line = line.rstrip()  #removes next line chars
		printOutLine(line,row)
		row = row - (font_size)  # drop y-value by font-size
		#END LINE
	c.showPage() #ends last page
	try:
		c.save()
		print('Exporting:', file + ' -> ' + dest)
	except PermissionError:
		print("Close " + file + ".pdf file and try again")
