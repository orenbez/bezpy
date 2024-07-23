#=======================================================================================================================
# Module: pywinauto
# Manages windows applications
# Documentation: https://pywinauto.readthedocs.io/en/latest
# Requires: pip install pywinauto
# Dependencies: pyWin32, comtypes, six, Pillow (for screenshots)
#=======================================================================================================================
# Dialog — a window containing several other GUI elements/controls like buttons, edit boxes etc. Dialog is not necessarily a main window. Message box on top of main form is also a dialog. Main form is also considered a dialog by pywinauto.
# Control — a GUI element at any level of a hierarchy. This definition includes window, button, edit box, grid, grid cell, bar, etc.
#=======================================================================================================================
# Backend Type1: Win32 API (backend=”win32") — a default backend for nowMFC, VB6, VCL, simple WinForms controls and most of the old legacy apps.
# Backend Type2: MS UI Automation (backend=”uia”) — WinForms, WPF, Store apps, Qt5, browsers. Chrome requires force-renderer-accessibility cmd flag before starting. Custom properties and controls are not supported because of comtypes Python library restrictions.
#=======================================================================================================================


from pywinauto import application
import pywinauto.mouse as mouse
import pywinauto.keyboard as keyboard

# Automating Notepad
app = application.Application()  # selects default backend
app.start('notepad.exe')    # app.start(r"c:\windows\system32\notepad.exe")
# app.start('notepad.exe', timeout=10)  # with timeout value if fails to open


dlg = app.windows()[0]
# dlg = app.top_window()  # Alternatively - this gives the active window
# dlg = app[‘Untitled – Notepad’] # Alternatively
# dlg = app.window(title_re=".*Notepad.*")   # alternatively using regex


dlg.type_keys('message goes here!', with_spaces=True)
if dlg.is_maximized() == False:
    dlg.maximize()

# After opening a text file 'temp.txt'
x = app.connect(path=r"c:\windows\system32\notepad.exe")  # connect to a running process
# app.connect(process=1234)  # alternate to above
# app.connect(title_re=".*Notepad*")  #alternate to above


app.windows() # [<hwndwrapper.DialogWrapper - 'temp.txt - Notepad', Notepad, 67652>, <hwndwrapper.DialogWrapper - 'M', MSCTFIME UI, 67698>, <hwndwrapper.DialogWrapper - 'Default IME', IME, 67666>]
dlg = app['temp.txt - Notepad']
dlg.print_control_identifiers()
# Control Identifiers:

# Notepad - 'temp.txt - Notepad'    (L656, T218, R1752, B977)
# ['temp.txt - NotepadNotepad', 'Notepad', 'temp.txt - Notepad']
# child_window(title="temp.txt - Notepad", class_name="Notepad")
#    |
#    | Edit - ''    (L664, T269, R1744, B946)
#    | ['temp.txt - NotepadEdit', 'Edit']
#    | child_window(class_name="Edit")
#    |
#    | StatusBar - ''    (L664, T946, R1744, B969)
#    | ['StatusBar  Ln 1, Col 1', 'temp.txt - NotepadStatusBar', 'StatusBar Windows (CRLF)', 'StatusBar 100%', 'StatusBar UTF-8', 'StatusBar']       
#    | child_window(class_name="msctls_statusbar32")


# Use non-default backend
app = application.Application(backend="uia")
app.connect(path=r"c:\windows\system32\notepad.exe")

app.dlg.control  # <pywinauto.application.WindowSpecification object at 0x0000021EE0FC1510>
app['dlg']['control']  # same as above

dlg.menu_select("View -> Status Bar")
dlg.menu_select("File -> Save as")
dlg.menu_select("Edit -> Replace")
dlg.Replace.Cancel.click()  # Cancels above menu

dlg.Edit.type_keys('Welcome{SPACE}to{SPACE}Medium')  # type in window
dlg.typekeys('my message', with_spaces=True)

# Use Keyboard
dlg.set_focus()
keyboard.send_keys('Hello')

# Use Mouse
dlg.set_focus()
mouse.click(coords=(1850, 60))

# Capture image
dlg.set_focus()
image = dlg.capture_as_image()   # requires library PIL or Pillow
image.save('file.png')

# for manipulating word document in python use: https://medium.com/@HeCanThink/python-docx-a-comprehensive-guide-to-creating-and-manipulating-word-documents-in-python-a765cf4b4cb9
# Microsoft Word - not working too well
app.connect(path=r"C:\Program Files (x86)\Microsoft Office\root\Office16\WINWORD.EXE")  # Connect to open word document
dlg = app.window(title_re='Sample_Doc.*')  # Find document by name using regex
dlg.Microsoft_Word.type_keys('^s')         # Save document my typing keys CTRL-S

app.connect(path=r"C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")  # Connect to open word document
dlg = app.window(title_re='Sample_Excel.*')  # Find document by name using regex
dlg.Microsoft_Excel.type_keys('^s')        # Save document my typing keys CTRL-S

