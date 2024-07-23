import xlrd
import unicodecsv
import sys

def xls2csv (xls_filename, csv_filename):
    # Converts an Excel file to a CSV file.
    # If the excel file has multiple worksheets, only the first worksheet is converted.
    # Uses unicodecsv, so it will handle Unicode characters.
    # Uses a recent version of xlrd, so it should handle old .xls and new .xlsx equally well.

    wb = xlrd.open_workbook(xls_filename)
    sh = wb.sheet_by_index(0)

    fh = open(csv_filename,"wb")

    #utf-8 is important for opening nicely in excel which doesn't accept some encoding types
    #e.g. UCS-2 LE BOM
    csv_out = unicodecsv.writer(fh, encoding='utf-8')
    num_rows = sh.nrows

    # sh.row_values(0) returns first row in list form
    # sh.col_values(0) returns first col in list form
    
    for row_number in range(num_rows):
        csv_out.writerow(sh.row_values(row_number))
    fh.close()



if __name__ == '__main__':
    #sys.argv = ['xls2csv.py', 'input.xlsx', 'output.csv']
    if len(sys.argv) == 3:
        xls2csv (sys.argv[1], sys.argv[2])
        print("{} has been successfully converted to {}".format(sys.argv[1],sys.argv[2]))
    else:
        print("USAGE: python xls2csv.py input.xlsx output.csv")
