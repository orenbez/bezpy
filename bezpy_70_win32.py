#=======================================================================================================================
# Printing files to printer
#=======================================================================================================================
# REQUIRES pip install pypiwin32
#=======================================================================================================================
# Requires a pdf reader to print pdf files otherwise you will get the following error
# pywintypes.error: (31, 'ShellExecute', 'A device attached to the system is not functioning.')
#=======================================================================================================================
# Also requires full security access to the printer
# Print = Allow, Manage This Printer = Allow, Manage Documents = Allow
#=======================================================================================================================
# also see the wrapper for win32print which is https://github.com/Solomoriah/MSWinPrint
#=======================================================================================================================

import os
import sys
import win32api
import win32print
from win32con import  DMORIENT_PORTRAIT, DMORIENT_LANDSCAPE, DMCOLOR_COLOR, DMCOLOR_MONOCHROME   # constants


# computer information on a windows machine
def printInfo():
    device = win32api.EnumDisplayDevices()
    print((device.DeviceName, device.DeviceString))
    settings = win32api.EnumDisplaySettings(device.DeviceName, -1)
    for varName in ['Color', 'BitsPerPel', 'DisplayFrequency']:
        print("%s: %s"%(varName, getattr(settings, varName)))

original_printer = win32print.GetDefaultPrinter ()
all_printers = [printer[2] for printer in win32print.EnumPrinters(win32print.PRINTER_ENUM_CONNECTIONS)] # A List containing the system printers

# win32print.PRINTER_ENUM_CONNECTIONS = 4   # Network Printers
# win32print.PRINTER_ENUM_LOCAL = 2         # Local Printers

# Full list
# [PRINTER_ENUM_CONNECTIONS, PRINTER_ENUM_CONTAINER, PRINTER_ENUM_DEFAULT, PRINTER_ENUM_EXPAND, PRINTER_ENUM_ICON1,PRINTER_ENUM_ICON2,PRINTER_ENUM_ICON3, PRINTER_ENUM_ICON4, PRINTER_ENUM_ICON5, PRINTER_ENUM_ICON6,
#  PRINTER_ENUM_ICON7,PRINTER_ENUM_ICON8,PRINTER_ENUM_LOCAL,PRINTER_ENUM_NAME,PRINTER_ENUM_NETWORK,PRINTER_ENUM_REMOTE,PRINTER_ENUM_SHARED]
# [4, 32768, 1, 16384, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 2, 8, 64, 16, 32]
 
printer_num = 2  # Choose a Printer
win32print.SetDefaultPrinter(all_printers[printer_num])  # set another printer as default
default_printer = win32print.GetDefaultPrinter ()
print(default_printer, original_printer)
pdf_dir = r'W:\TSCDIRECT\TSC111\PRINTPDF\TESTDIR'
file = os.path.join(pdf_dir, 'Auto_CancelNoticeUnder50.pdf')

printdefaults = {"DesiredAccess": win32print.PRINTER_ALL_ACCESS}
#printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_USE}   # DO NOT USE
#printdefaults = {"DesiredAccess": win32print.PRINTER_ACCESS_ADMINISTER}  # DO NOT USE

for i in all_printers:
    try:
        handle = win32print.OpenPrinter(i, printdefaults)
        print('Yes Access for ', i)

    except:
        print('No Access for ', i )  # You don't have sufficient privelages on the security tab

sys.exit()

handle = win32print.OpenPrinter(default_printer, printdefaults)
level = 2
attributes = win32print.GetPrinter(handle, level)


attributes['pDevMode'].DeviceName           # Returns Device Name
attributes['pDevMode'].Orientation          # 1=DMORIENT_PORTRAIT, 2=DMORIENT_LANDSCAPE
attributes['pDevMode'].Duplex               # 1=DMDUP_SIMPLEX, 2=DMDUP_VERTICAL, 3=DMDUP_HORIZONTAL (Flip on Short Edge)
attributes['pDevMode'].Collate              # DMCOLLATE_TRUE, DMCOLLATE_FALSE
attributes['pDevMode'].Color                # DMCOLOR_COLOR, DMCOLOR_MONOCHROME
attributes['pDevMode'].Copies               # Number of copies to print
attributes['pDevMode'].PaperLength          # Specified in 1/10 millimeters  2794 = 11 inches (letter), 3556=14 inches (legal)
attributes['pDevMode'].Scale                # Specified as percentage 0 to 100  FOR SOME REASON NOT WORKING FOR ME
attributes['pDevMode'].Size                 # Defaults to 220 - not sure what this is
attributes['pDevMode'].PaperSize            # Defaults to 1 - not sure, for number 10 envelope is 20
attributes['pDevMode'].Position_x           # 65537
attributes['pDevMode'].Position_y           # 141495018  
attributes['pDevMode'].DefaultSource        # Tray Number
attributes['pDevMode'].Color = DMCOLOR_MONOCHROME    # Set an attribute
attributes['pDevMode'].Orientation = DMORIENT_LANDSCAPE
attributes['pDevMode'].Scale = 75

win32print.SetPrinter(handle, level, attributes, 0)  # Apply Changes

# Print Operation
cmd = '.\pdfprint_cmd\pdfprint.exe -$ 57WER6432487742ASF67  -printer \"' + printer + '\" \"' + file + '\"'
returned_value = os.system(cmd)  # returns the exit code in unix

# did not have success with the below print operations. If i was running multiple prints with different settings, by the time
# the first print executed it used the last prints settings!!!!  used pdfprint.exe from VeryPDF instead
# win32api.ShellExecute(0, "print", file, None,  ".",  0)    # None => use the default printer
# win32api.ShellExecute(0, "printto", file, '"%s"' % printer, ".", 0)  # Specific Printer (this opens the pdf file for some reason)

win32print.ClosePrinter(handle)
win32print.SetDefaultPrinter(original_printer)  # reset default printer



# win32api.MessageBox(None,"Do you want to open a file?", "MsgBoxTitle",1)
# win32api.MessageBox(0,"msgbox", "title")
# win32api.MessageBox(0,"ok cancel?", "title",1)
# win32api.MessageBox(0,"abort retry ignore?", "title",2)
# win32api.MessageBox(0,"yes no cancel?", "title",3)



# ======================================================================================================================
# Connect to a UNC Path (Universal Naming Convention) / Network Drive also see non-standard library 'win_unc'
# ======================================================================================================================

import os
import pywintypes  # standard library
import win32wnet   # standard libray


CONNECT_INTERACTIVE = 0x00000008

# FQDN (Fully Qualified Domain Name) e.g.  'wang.pandcins.local' is best to use. for hostname
HOST_NAME = "192.168.1.3"  # or 'wang' or 'wang.pandcins.local'
SHARE_NAME = "Work"        # top directory of fileshare
SHARE_FULL_NAME = os.path.sep * 2 + os.path.sep.join((HOST_NAME, SHARE_NAME))
SHARE_USER = "TRISTATEINS\oren.bez"  # this will assume user=oren.bez, domain=TRISTATEINS
SHARE_PWD = "badge7383"


def unc_connect():
    net_resource = win32wnet.NETRESOURCE()
    net_resource.lpRemoteName = SHARE_FULL_NAME
    flags = 0
    #flags |= CONNECT_INTERACTIVE
    print("Trying to create connection to: {:s}".format(SHARE_FULL_NAME))
    try:
        win32wnet.WNetAddConnection2(net_resource, SHARE_PWD, SHARE_USER, flags)
    except pywintypes.error as e:
        print(e)
    else:
        print("Success!")


# if you get this error:
# "Multiple connections to a server or shared resource by the same user"
# "NET USE * /delete"  will close all connections from the command line
