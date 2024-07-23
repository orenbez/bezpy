import pdfkit
pdfkit.from_file('output.html', 'output.pdf')


### THIS GAVE ERROR
#OSError: No wkhtmltopdf executable found: "b''"

### ADVISE WAS TO DO THIS BUT THINK I NEED TO INSTALL wkhtmltopdf
config = pdfkit.configuration(wkhtmltopdf=b"C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
pdfkit.from_file('output.html', 'output.pdf', configuration=config)
