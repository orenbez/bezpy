# see https://alexanderankin.github.io/pyfpdf/mkdocs_docs/index.html
# see https://medium.com/better-programming/how-to-create-a-pdf-in-python-71fac9f7bcd6
# see https://towardsdatascience.com/how-to-create-pdf-reports-with-python-the-essential-guide-c08dd3ebf2ee
# also see 11_PYPDF2

# ======================================================================================================================
# Generates quick and easy low resolution pdf, alternative to reportlab
# ======================================================================================================================
from fpdf import FPDF
output_file = '.\\myfiles\\example3.pdf'
class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.WIDTH = 210
        self.HEIGHT = 297
        self.orientation='P'
        self.unit='mm'
        self.format='Letter'

    def header(self):
        self.image('.\\myfiles\\example.jpg', 50, 30, 100)
        self.set_font('Arial', 'B', 15)
        self.set_text_color(255, 255, 255)
        self.cell(0, 10, 'Title', 1, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, 'Page ' + str(self.page_no()) + '/{nb}', 0, 0, 'C')

pdf = PDF()
pdf.alias_nb_pages()  # This allows the footer refrence {nb} = total number of pages
pdf.add_page()        # Creates a blankpage

pdf.set_font('Times', '', 12)
for i in range(1, 50):
    pdf.cell(0, 10, 'Cell number ' + str(i), 0, 1)  # cell(w, h, txt, border, align, fill)
    # pdf.text(x, y, txt)


try:
    pdf.output(output_file, 'F')
except PermissionError:
    print(f'ERROR: Close {output_file} and rerun')
