import os, sys
import win32print
import win32api
from time import sleep


# Windows API: http://docs.activestate.com/activepython/2.5/pywin32/win32print.html
#############################################################################################################
### MAIN function starts here
#############################################################################################################
if __name__ == '__main__':
    sys.argv = ['print_pdf.py',r'C:\temp\MVR.pdf']

    file_name = sys.argv[1]

    printer_name = r'\\tsc-print12\HP LaserJet 4100tn - Letterhead'

    # Return default printer
    current_default = win32print.GetDefaultPrinter()

    # Change default printer
    #win32print.SetDefaultPrinter(printer_name)

    handle = win32print.OpenPrinter(printer_name)
    # returns tuple of jobs
    j = win32print.EnumJobs(handle, 0, 1)

    # returns list of printers
    p = win32print.EnumPrinters(5)
    for x in p:
        print(x[1][:x[1].find(',')])

    # returns list of printer drivers
    d = win32print.EnumPrinterDrivers(None, None) #None = Local Server, Local Environment

    win32api.ShellExecute (0, "print", file_name, printer_name, ".", 0)
    sleep(5)
    os.system("TASKKILL /F /IM Acrobat.exe")
    #os.system("TASKKILL /F /IM AcroRD32.exe")



