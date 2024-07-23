# Uses template pdf file as a canvas for reportlab

import os
import sys
from io import BytesIO
from reportlab.lib.pagesizes import letter, landscape
from reportlab.pdfgen import canvas
# from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter   deprecated and removed in PyPDF2 3.0.0
from PyPDF2 import PdfMerger, PdfReader, PdfWriter


def get_page_height(p):
    h = float(p.mediaBox.getHeight()) * 0.352
    return h

def get_page_width(p):
    w = float(p.mediaBox.getWidth()) * 0.352
    return w

def set_canvas(template, packet):
    # Blank Canvas Matching the template dimensions
    width = get_page_width(template)
    height = get_page_height(template)
    return canvas.Canvas(packet, pagesize=(width, height))

def write_to_page(c):
    c.setFont("Times-Roman", 8)
    c.setFillColorRGB(1, 0, 0)          # Set Color RED
    c.drawString(400,705,'x (405,705)')
  
def save_page(c, template, packet, writer):
    c.save()
    packet.seek(0) # Reset stream pointer of Canvas
    new_pdf = PdfReader(packet)
    template.mergePage(new_pdf.getPage(0))  # Merge the page onto the same Canvas
    writer.addPage(template) # can add additional pages with this command


# n = required page from the template
def merge_to_template(path_to_template, path_to_dest):
    reader = PdfReader(path_to_template, 'r')  # Template document
    writer = PdfWriter()
    outstream = open(path_to_dest, 'wb')           # Output file

    # Useful info about the Template
    # num_of_pages = reader.getNumPages()  # Number of pages
    # metadata = reader.getDocumentInfo()  # Dictionary of metadata

    # ==============================================================================
    template = reader.getPage(0)
    packet = BytesIO()
    c = set_canvas(template, packet)
    write_to_page(c) # Write to New Canvas
    save_page(c, template, packet, writer)
    # ==============================================================================
    template = reader.getPage(1)
    packet = BytesIO()
    c = set_canvas(template, packet)
    write_to_page(c) # Write to New Canvas
    save_page(c, template, packet, writer)
    # ==============================================================================
    # WARNING - if you wish to access the 1st template page again with reader.getPage(0)
    # you will be accessing the merged template and writing on top of that.
    # do this instead
    template = PdfReader(path_to_template, 'r').getPage(0)
    # ==============================================================================
    writer.write(outstream)
    #writer has no close() function
    outstream.close()



def merge_two_files(file1, file2, merged_file):
    reader1 = PdfReader(file1, 'r').getPage(0)  # Read First Page
    reader2 = PdfReader(file2, 'r').getPage(0)  # Read First Page
    reader1.mergePage(reader2)  # Merge the pages onto the same Canvas
    writer = PdfWriter()
    writer.addPage(reader1) # can add additional pages with this command
    outstream = open(merged_file, 'wb')           # Output file
    writer.write(outstream)
    #writer has no close() function
    outstream.close()



if __name__ == "__main__":

    merge_to_template('template.pdf', 'output2.pdf' )
    merge_two_files('file1.pdf', 'file2.pdf', 'merged_file.pdf')  # WARNING - Sometimes compressed pdf files do not merge so well to other pdf files




