files = ['C:\\T1\\Referral_Nephrology_J_Cohen_2024_02.pdf', 'C:\\T1\\Referral_Nephrology_J_Cohen_2024_01.pdf']
merged_file = 'C:\\T1\\Referral_for_Oren_Bezalely_07_2024.pdf'



from PyPDF2 import PdfMerger, PdfReader
merger = PdfMerger()

for file in files:
    reader = PdfReader(file,'r')
    merger.append(reader)

# Write to an output PDF document
outstream = open(merged_file, "wb")
merger.write(outstream)

merger.close()
outstream.close()