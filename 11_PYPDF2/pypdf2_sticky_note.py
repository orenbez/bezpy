import os
# from PyPDF2 import PdfFileReader  deprecated and removed in PyPDF2 3.0.0
from PyPDF2 import PdfReader
# Sticky notes inserted in pdf by right click on page -> add sticky note
# ======================================================================================================================
# Prints Message box / Sticky Notes info
# ======================================================================================================================
if __name__ == '__main__':

    reader = PdfReader(open('x.pdf', "rb"))
    metadata = reader.getDocumentInfo()
    num_pages = reader.getNumPages()

    for i in range(num_pages) :
        try:
            page_i = reader.getPage(i)['/Annots']
            for annot in page_i:
                print ('PageNumber:', i + 1, '; Date:', annot.getObject()['/CreationDate'], '; Msg:', annot.getObject()['/Contents'])
        except :
            # there are no annotations on this page
            pass
