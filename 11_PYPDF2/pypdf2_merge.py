""" Appends all pdf files in 'sub' directory  for merging on the same canvas see pypdf2_template.py"""

# APPEND first 3 pages of input1 document to output
# merger.append(fileobj=input1, pages=(0,3))

# INSERT the first page of input2 into the output beginning after the second page
# merger.merge(position=2, fileobj=input2, pages = (0,1))

# APPEND entire input3 document to the end of the output document
# merger.append(input3)


#  from PyPDF2 import PdfFileMerger, PdfFileReader   deprecated and removed in PyPDF2 3.0.0

from PyPDF2 import PdfMerger, PdfReader
merger = PdfMerger()

# Append all files in path    (BETTER METHOD BELOW)
# for file in ['01.pdf', '02.pdf']:
#     with open(file, "rb") as pdf:
#         merger.append(PdfReader(pdf))


for file in ['01.pdf', '02.pdf']:
    reader = PdfReader(file,'r')
    merger.append(reader)

# Write to an output PDF document
outstream = open("merged_doc.pdf", "wb")
merger.write(outstream)

merger.close()
outstream.close()


