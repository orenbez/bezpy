##############################################################################################################################################################
# Function: called by expense_report.py to generate monthly expense report
# File Name: report2pdf.py
# Notes:
# https://www.actian.com/company/blog/programming-easy-way-accessing-psql-zen-database-python-odbc/
# Queries can be run directly in PSQL Control Center using the Actian (Pervasive) Database
#
# Usage:
#
# Version History:
# 10/26/2018 ONB 1st Version
# 10/30/2018 ONB Order results, Flag values with large percentage change
# 11/13/2018 ONB Changed Color of data_2 set ... ('TEXTCOLOR',(0,end_data_1 + 1),(-2,-2)
##############################################################################################################################################################
# c = canvas.Canvas(fileName + '.pdf', pagesize=landscape(letter))
# c = canvas.Canvas(fileName + '.pdf', pagesize=letter)
# 1mm = 2.83 pts on the pdf document
# LANDSCAPE page dimensions  791 x 611
# PORTRAIT page dimensions   611 x 791
# c.drawString(791,611,'.') = TOP RIGHT CORNER (LANDSCAPE)
# c.drawString(0,0,'.')	= BOTTOM LEFT CORNER (PORTRAIT)
# c.setTitle("Title of PDF")
# print(c.getAvailableFonts()) displays to screen all the available fonts

from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Frame, Spacer, Image
from reportlab.lib import colors
from reportlab.lib.units import cm
#from reportlab.lib.pagesizes import A3, A4, landscape, portrait, letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.enums import TA_LEFT, TA_RIGHT, TA_CENTER, TA_JUSTIFY
#from reportlab.pdfgen import canvas


def printreport(title, data, name, increase_tuples, decrease_tuples, percent_change, end_data_1):

    pdfReportPages = name
    doc = SimpleDocTemplate(pdfReportPages, pagesize=(792.0, 612.0), rightMargin=18,
                            leftMargin=18, topMargin=18, bottomMargin=18)
 

    # container for the "Flowable" objects
    elements = []
    logo = Image('.\\image\\logo2.png', 200, 48)
    elements.append(logo)
    elements.append(Spacer(1, 12))
    
    styles = getSampleStyleSheet()
    #styleN = styles['Normal']
    #styleH = styles['Heading1']
    
    styles.add(ParagraphStyle(name='TitleLabel', alignment=TA_CENTER, fontName='Times-Roman'))
    ptext = f'<font size=12>{title}</font>'
    elements.append(Paragraph(ptext, styles['TitleLabel']))
    elements.append(Spacer(1, 12))

    # Assemble data for each column using simple loop to append it into data list
    wid = 1.6 * cm
    tableThatSplitsOverPages = Table(data, [5.5 * cm,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid,wid], repeatRows=1)
    tableThatSplitsOverPages.hAlign = 'LEFT'
    tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,0),colors.white),
                           ('TEXTCOLOR',(0,1),(-2,end_data_1),colors.black),
                           ('TEXTCOLOR',(0,end_data_1 + 1),(-2,-2),colors.darkred),
                           ('TEXTCOLOR',(1,-1),(-1,-1),colors.darkgreen),
                           ('TEXTCOLOR',(-1,1),(-1,-1),colors.darkgreen),
                           ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
                           ('ALIGN',(1,0),(-1,-1),'CENTER'),
                           ('LINEBELOW',(0,0),(-1,-1),1,colors.darkred),
                           ('BOX',(0,0),(-1,-1),1,colors.black),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (1,0), (-1,0),  8),
                           ('FONTSIZE', (0,1), (-1,-1), 7),
                           ])
    tblStyle.add('BACKGROUND',(0,0),(-1,0),colors.ReportLabGreen)
    tblStyle.add('BACKGROUND',(0,1),(-1,-1),colors.white)
    tblStyle.add('BACKGROUND',(1,-1),(-2,-1), colors.whitesmoke)
    tblStyle.add('BACKGROUND',(-1,1),(-1,-1), colors.whitesmoke)

    for i in increase_tuples:
        tblStyle.add('BACKGROUND',i,i, colors.mistyrose)
    for i in decrease_tuples:
        tblStyle.add('BACKGROUND',i,i, colors.fidlightblue)
        
    tableThatSplitsOverPages.setStyle(tblStyle)
    elements.append(tableThatSplitsOverPages)
    elements.append(Spacer(1, 24))


    styles.add(ParagraphStyle(name='Keys', alignment=TA_LEFT, fontName='Times-Roman'))
    ptext = f'<font size=12>Change From Previous Month:</font>'
    elements.append(Paragraph(ptext, styles['Keys']))
    elements.append(Spacer(1, 6))


    data = [['Increase ' + str(percent_change) + '%'],['Decrease ' + str(percent_change) + '%']]
    table2 = Table(data, [5.5 * cm], repeatRows=1)
    table2.hAlign = 'LEFT'
    tblStyle = TableStyle([('TEXTCOLOR',(0,0),(-1,-1),colors.black),
                           ('VALIGN',(0,0),(-1,-1),'BOTTOM'),
                           ('ALIGN',(0,0),(-1,-1),'CENTER'),
                           ('LINEBELOW',(0,0),(-1,-1),1,colors.black),
                           ('BOX',(0,0),(-1,-1),1,colors.black),
                           ('INNERGRID', (0,0), (-1,-1), 0.25, colors.black),
                           ('FONTSIZE', (1,0), (-1,-1),  8),
                           ])
    tblStyle.add('BACKGROUND',(0,0),(0,0),colors.mistyrose)
    tblStyle.add('BACKGROUND',(0,1),(0,1),colors.fidlightblue)

    table2.setStyle(tblStyle)
    elements.append(table2)
    elements.append(Spacer(1, 12))

    
    pie = Image('.\\image\\pie_chart.png', 744,564)
    elements.append(pie)
    doc.build(elements)
