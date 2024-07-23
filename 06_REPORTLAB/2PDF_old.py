from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
from reportlab.lib.utils import ImageReader
from PIL import Image

# c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
# c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
# 1mm = 2.83 pts on the pdf document
# LANDSCAPE page dimensions  791 x 611
# PORTRAIT page dimensions   611 x 791
# c.drawString(791,611,'.') = TOP RIGHT CORNER (LANDSCAPE)
# c.drawString(0,0,'.')	= BOTTOM LEFT CORNER (PORTRAIT)
# c.setTitle("Title of PDF")
# print(c.getAvailableFonts()) displays to screen all the available fonts



ptr = open("PLBA0000", "r")  # text file I need to convert
lines = ptr.readlines()
ptr.close()
i = 750
numOfLines = 0


canvas = canvas.Canvas("LETTER.pdf", pagesize=letter)
canvas.setLineWidth(.3)
canvas.setFont('Helvetica', 12)


while numOfLines < len(lines):
    if numOfLines - len(lines) < 60: # I'm gonna write every 60 lines because I need it like that
        i=750
        for lines in lines[numOfLines:numOfLines+60]:      
            canvas.drawString(15, i, lines.strip())
            numOfLines += 1
            i -= 12
        canvas.showPage()
    else:
        i = 750
        for lines in lines[numOfLines:]:
           canvas.drawString(15, i, lines.strip())
           numOfLines += 1
           i -= 12
        canvas.showPage()
canvas.save()		
