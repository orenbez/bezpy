#################################################################################################
#!/usr/bin/python
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
# c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
# c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
# 1mm = 2.83 pts on the pdf document
# LANDSCAPE page dimensions  791 x 611
# PORTRAIT page dimensions   611 x 791
# c.drawString(791,611,'.') = TOP RIGHT CORNER (LANDSCAPE)
# c.drawString(0,0,'.')	= BOTTOM LEFT CORNER (PORTRAIT)
# c.setTitle("Title of PDF")
# print(c.getAvailableFonts()) displays to screen all the available fonts

#################################################################################################
def printOutLine(line_str, y_cord):
	line_lst = list(line_str)
	indent = margin_indent  
	i = 0
	while i < len(line_lst):
		print ('i =',i)
		print ('indent =',indent)
		print (line_str[i:])
		char = line_lst[i]
		if char == ' ':
		  c.drawString(indent,y_cord,char)
		  indent += char_indent * 1
		  i += 1
		else: 
			increment = line_str[i:].find(' ',i)
			if increment == -1: # no more spaces till end of string
				c.drawString(indent, y_cord, line_str[i:])
				break
			else:
				c.drawString(indent, y_cord, line_str[i:i + increment])
				print(line_str[i:i + increment])
				i += increment			
				indent += char_indent * increment

#################################################################################################				
font_size = 12
margin_indent = 35
char_indent = 6

#https://www.blog.pythonlibrary.org/2010/03/08/a-simple-step-by-step-reportlab-tutorial/
#https://stackoverflow.com/questions/10112244/convert-plain-text-to-pdf-in-python
 
 
c = canvas.Canvas("form.pdf", pagesize=letter)
c.setLineWidth(.3)
c.setFont("Courier-Bold", 12)	
print(c.getAvailableFonts()) #displays to screen all the available fonts
# count each line as 15 points 
c.drawString(30,750,'OFFICIAL COMMUNIQUE')
c.drawString(30,735,'OF ACME INDUSTRIES')
c.drawString(500,750,"12/12/2010")
c.line(480,747,580,747)
 
c.drawString(275,725,'AMOUNT OWED:')
c.drawString(500,725,"$1,000.00")
c.line(378,723,580,723)
 
c.drawString(30,703,'RECEIVED BY:')
c.line(120,700,580,700)
c.drawString(120,703,"JOHN DOE")
c.drawString(1,1,"A") 
c.drawString(1,785,"B") 
c.drawString(604,785,"C")
c.drawString(604,1,"D") 



c.setFont("Times-Roman", font_size)
str1 = "Y                                                                                Y"
str2 = "Y12345678901234567890123456789012345678901234567890123456789012345678901234567890Y"
str3 = "Yabcdefgh ijklGHI KLMNOPQGHIJK MNOPQmnGHI KLMNOP opq rstuvwxyz ABCDEF Gklm uvwxyzY"


printOutLine(str1,70)
c.drawString(margin_indent,60,str1)
printOutLine(str2,50)
c.drawString(margin_indent,40,str2)
printOutLine(str3,30)
c.drawString(margin_indent,20,str3)

c.save()
