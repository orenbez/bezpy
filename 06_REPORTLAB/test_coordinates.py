# c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
# c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
# 1mm = 2.83 pts on the pdf document
# LANDSCAPE page dimensions  791 x 611
# PORTRAIT page dimensions   611 x 791
# c.drawString(791,611,'.') = TOP RIGHT CORNER (LANDSCAPE)
# c.drawString(0,0,'.')	= BOTTOM LEFT CORNER (PORTRAIT)
# c.setTitle("Title of PDF")
# print(c.getAvailableFonts()) displays to screen all the available fonts

from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas

cvs = canvas.Canvas('test_portrait.pdf', pagesize=letter)
cvs.setFont('Courier', 1)  


cvs.setFillColorRGB(1, 0, 0) # RED
cvs.drawString(-1,0,'.(-1,0)')  # THIS is off the page

cvs.setFillColorRGB(0, 1, 0) # GREEN
cvs.drawString(0,0,'.(0,0)')

cvs.setFillColorRGB(0, 0, 1) # BLUE
cvs.drawString(1,1,'.(1,1)')



cvs.setFillColorRGB(0, 0, 1) # BLUE
cvs.drawString(610,790,'.(610, 790)')

cvs.setFillColorRGB(0, 1, 0) # GREEN
cvs.drawString(611,791,'.(611, 791)')

cvs.setFillColorRGB(1, 0, 0) # RED
cvs.drawString(612,792,'.(612, 792)')  #THIS IS OFF THE PAGE


cvs.setFillColorRGB(0, 0, 0) # BLACK
cvs.drawString(300,10,'. (300,10)')
cvs.drawString(300,775,'. (300,775)')
cvs.save()



cvs = canvas.Canvas('test_landscape.pdf', pagesize=landscape(letter))
cvs.setFont('Courier', 1)  


cvs.setFillColorRGB(1, 0, 0) # RED
cvs.drawString(-1,0,'.(-1,0)')  # THIS is off the page

cvs.setFillColorRGB(0, 1, 0) # GREEN
cvs.drawString(0,0,'.(0,0)')

cvs.setFillColorRGB(0, 0, 1) # BLUE
cvs.drawString(1,1,'.(1,1)')



cvs.setFillColorRGB(0, 0, 1) # BLUE
cvs.drawString(790,610,'.(790,610)')

cvs.setFillColorRGB(0, 1, 0) # GREEN
cvs.drawString(791, 611,'.(791,611)')

cvs.setFillColorRGB(1, 0, 0) # RED
cvs.drawString(792, 612,'.(792, 612)')  #THIS IS OFF THE PAGE

cvs.save()
