# ======================================================================================================================
# Based on https://towardsdatascience.com/how-to-supercharge-excel-with-python-726b0f8e22c2
# Documentation: https://docs.xlwings.org/
# It seems that python needs to be installed on the users PC for this to work
# ======================================================================================================================
# ALSO SEE pyXLL which is a Excel Add-in for python
# ======================================================================================================================
# ALSO SEE "Python in Excel" which is only available for some versions of Excel
# ======================================================================================================================

# ======================================================================================================================
# 1.  In terminal type 'pip install xlwings'
# 2.  Close all instances of Excel
# 3.  In terminal type xlwings addin install this will download file: to  'C:\\Users\\costa\\AppData\\Roaming\\Microsoft\\Excel\\XLSTART\\xlwings.xlam'
# 4.  Enabling User Defined Functions for xlwings on your spreadsheet  Developer->Excel Add-ins and browse to the above file and hit 'Ok'
# 5.  Enable Trust access to the VBA project object model (File > Options > Trust Center > Trust Center Settings > Macro Settings)
# 7.  In terminal, navigate to a directory and type 'xlwings quickstart <excel file name>'
#     e.g. (venv) C:\Users\orenb\OneDrive\PYTHON\myfiles>xlwings quickstart pyxlwings
# 8.  Note this creates a directory pyxlwings with files  pyxlwings.py, pyxlwings.xlsm
# 9.  Open pyxlwings.xlsm, notice a new Excel sheet called _xlwings.conf. If you want to rely on the settings in
#     the addin xlwings menu or an xlwings.conf file, you can delete this sheet. Should you wish to override the default
#     settings of xlwings, all you have to do is rename this sheet and remove the starting underscore
# 10. Open Excel VBA editor (Alt + F11) and notice module 1 has the following procedure:
# ======================================================================================================================
#           Sub SampleCall()
#               mymodule = Left(ThisWorkbook.Name, (InStrRev(ThisWorkbook.Name, ".", -1, vbTextCompare) - 1))
#               RunPython "import " & mymodule & ";" & mymodule & ".main()"
#           End Sub
# ======================================================================================================================
#  SampleCall() does the following:
#       i) Look for a Python Script in the same location as the spreadsheet
#       ii) Look for a Python Script with the same name as the spreadsheet (but with a .py extension)
#       iii) From the Python Script, call the function “main()”
# Note: main() can be executed in the python script or from the SampleCall() in Excel, or clicking RUN on the xling ribbon tab
#       User Defined functions  (udf) like the =hello('name') example below require you to click on Import Python UDFs in the xlwings tab
# ======================================================================================================================
# C:\Users\orenb\OneDrive\PYTHON\myfiles\pyxlwings.py automatically contains the following code
# ======================================================================================================================
import xlwings as xw

def main():
    wb = xw.Book.caller()
    sheet = wb.sheets[0]
    if sheet["A1"].value == "Hello xlwings!":
        sheet["A1"].value = "Bye xlwings!"
    else:
        sheet["A1"].value = "Hello xlwings!"

@xw.func
def hello(name):
    return f"Hello {name}!"

@xw.func
def double_sum(x, y):
    """Returns twice the sum of the two arguments"""
    return 2 * (x + y)


if __name__ == "__main__":
    xw.Book("pyxlwings.xlsm").set_mock_caller()
    main()


# ======================================================================================================================

# ================================
# Write Dataframe to spreadsheet:
# ================================
# wb.sheets[0].range('A1').value = df

# or use
# sheet = wb.sheets[0]
# sheet["A3"].value = df

# ====================================
# User Defined Funcion in Excel (udf)
# ====================================
# Enter code for double_sum above with the decorator,  and click on Import Python UDFs in the xlwings tab on spreadsheet
# Then enter in any cell on sheet. =double_sum(4,3)

