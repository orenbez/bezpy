# from PyPDF2 import PdfFileReader, PdfFileWriter  deprecated and removed in PyPDF2 3.0.0

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('x.pdf','r')
# reader = PdfFileReader(open('x.pdf','rb')) same as above
num_of_pages = reader.getNumPages()  # Number of pages
metadata = reader.getDocumentInfo()  # Dictionary of metadata

page = reader.getPage(0)      # object of first page
page.cropBox.getLowerLeft()   # returns bottom left coordinate points(x,y) = (0, 0)
page.cropBox.getUpperRight()  # top right coordinate points(x,y) = (612, 792)


page.cropBox.setLowerLeft((30, 85))
page.cropBox.setUpperRight((575, 734))


writer = PdfWriter()
writer.addPage(page)

outstream = open('cropped_doc.pdf', 'wb')
writer.write(outstream)

#writer has no close() attribute
outstream.close()
