from tkinter import *
from tkinter import messagebox, scrolledtext, filedialog, Menu
from tkinter.ttk import Progressbar
from tkinter import ttk
import tkinter.font as tkFont
import os
import winsound

# TRY: https://realpython.com/tic-tac-toe-python
# SEE THIS: https://github.com/TomSchimansky/CustomTkinter

# ======================================================================================================================
# These are the Four Variable types you can associate with a widget
# str_var = StringVar() # Holds a string; the default value is an empty string
#                       # to set str_var.set('HELLO').  str_var.get() returns the string value
# int_var = IntVar()    # Holds an integer; the default value is 0
# db_var = DoubleVar()  # Holds a float; the default value is 0.0
# bl_Var = BooleanVar() # Holds a Boolean, it returns 0 for False and 1 for True

# To Monitor these Variables use
# trace_add(mode, callback_name)     # Adds trace to a variable above  e.g. int_var.trace_add('read', 'function_name')
# trace_remove(mode, callback_name)  # Removes trace to a variable above
# trace_info()                       # Returns name of the callback that is to be deleted

# Note Mode is one of "read", "write", "unset", or a list or tuple of such strings if you want to trace multiple events
# 'read' - for when the variable is acessed
# 'write' - for when variable is modified
# 'unset' - for when variable is deleted



# ======================================================================================================================
# Window Settings
# ======================================================================================================================
win = Tk()
# win.withdraw()    # this would remove the gui so that it is hidden and only show dialogue boxes
# tkFont.families()  # font list
win.title("Tkinter Practice")
win.configure(background='white')
win.geometry('650x800') # set window size  pixel width x height
win.iconbitmap(".\\image\\tsc.ico") # icon to left corner
style = {'bg':'white', 'fg':'darkred', 'font':'Verdana 10 bold', 'height': '2'}  # can unpack style with **style


# ======================================================================================================================
# MENU BAR
# ======================================================================================================================
def click_new():
    print('New was clicked')

def click_old():
    print('Old was clicked')

def click_exit():
    win.destroy()   # Closes Window

def click_sound():
    winsound.PlaySound('willhelm.wav', winsound.SND_FILENAME)  # Plays .wav file


menu = Menu(win)
menu_1 = Menu(menu)
menu_2 = Menu(menu, tearoff=0) # tearoff=0 removes the dotted line at top of menu ---
menu_1.add_command(label='New', command=click_new)
menu_1.add_command(label='Old', command=click_old)
menu_1.add_separator()
menu_1.add_command(label='Exit', command=click_exit)
menu_2.add_command(label='Sound', command=click_sound)
menu.add_cascade(label='Menu1', menu=menu_1)
menu.add_cascade(label='Menu2', menu=menu_2)
win.config(menu=menu) 


# ======================================================================================================================
# Image Label ROW 0
# ======================================================================================================================
photo0 = PhotoImage(file='.\image\logo2.gif') #image width will limit window size if you don't set geometry
lbl0 = Label(win,image=photo0, bg='white')
lbl0.grid(row=0, column=1, sticky=W, columnspan=4)
#-column, -columnspan, -in, -ipadx, -ipady, -padx, -pady, -row, -rowspan, or -sticky=N/S/E/W
# Note: padx, pady = padding in pixels external to object dimensions.  ipadx,ipady are internal
#  Can use a single value to pad left/right 10   e.g. padx=10  or tuple padx=(10,20) ie 10 to left 20 to right

# Note: before grid() was available pack() was used, pack() places everything in  one row or column


# ======================================================================================================================
# Label ROW 1
# ======================================================================================================================
lbl1 = Label(win,text='Enter Text:', bg='white', fg='darkred', font='Verdana 12 bold')
lbl1.grid(row=1, column=2, sticky=W)

# to modify parameter of lbl1 at runtime e.g.   lbl1['bg'] = 'blue'


# ======================================================================================================================
# Entry Box ROW 1
# ======================================================================================================================
# this MUST return a boolean otherwise the check is only done once
def check():
    print('check - ', txt1.get(), len(txt1.get()))
    if (len(txt1.get()) == 4):
        return True
    else:
        return False

# validate can take one of below 'event' values for entry box
# none      Default.  This means no validation will occur.
# focus     validateCommand will be called when  the  entry  receives  or loses focus.
# focusin   validateCommand will be called when the entry receives focus.
# focusout  validateCommand will be called when the entry loses focus.
# key       validateCommand will be called when the entry is edited.
# all       validateCommand will be called for all above conditions.


# state='normal' is the default state and is not required
txt1 = Entry(win, width=20, bg='white', validate='focusout', validatecommand=check, state='normal')
txt1.grid(row=1, column=3, sticky=W)
txt1.focus() #sets focus on this object

# disable the entry box at runtime with ...   txt1['state'] = 'disabled'
# or with ... txt1.configure(state='disabled')
# ======================================================================================================================
# Label ROW 2
# ======================================================================================================================
lbl2a = Label(win, text='this is lbl2a', bg='darkred', fg='white', font='Verdana 12 bold')
lbl2a.grid(row=2, column=2, columnspan=2, sticky=W)
# Update message at run-time with lbl2a['text'] = 'New label text'

# ======================================================================================================================
# Label (TYPE 2)  ROW 2
# ======================================================================================================================
message = StringVar()
message.set('message2')  # You can update the message at run-time with this command
lbl2b = Label(win, textvariable=message, bg='white', fg='darkred', font='Verdana 12 bold')
lbl2b.grid(row=2, column=3, columnspan=2, sticky=N, pady=15)


# ======================================================================================================================
# Combobox ROW 3
# ======================================================================================================================
style =  {'bg': 'white',  'fg': 'darkred',   'font': 'Verdana 10 bold', 'height': '1'}
cmb_number = IntVar()
cmb_number.set(4) # default
choices = {1,2,3,4,5} # Can also be a list which can preserve sequence
cmb3 = OptionMenu(win, cmb_number, *choices)
cmb3.config(**style)
cmb3.grid(row=3, column=3, sticky=W)

# ======================================================================================================================
# Check box ROW 4
# ======================================================================================================================
chk_val = IntVar()
chk_val.set(0) # default to checked
chk4 = Checkbutton(win, text="Check If True", variable=chk_val,  **style).grid(row=4, column=3, sticky=W)

# ======================================================================================================================
# Radio Button ROW 5
# ======================================================================================================================

def change_radio(var, indx, mode):
    print('You have changed radio to ', rad_val.get())

rad_val = IntVar()
rad_val.set(3)
rad1 = Radiobutton(win,text='Option 1', value=1, **style, variable=rad_val)
rad2 = Radiobutton(win,text='Option 2', value=2, **style, variable=rad_val)
rad3 = Radiobutton(win,text='Option 3', value=3, **style, variable=rad_val)
rad1.grid(row=5, column=2, pady=10)
rad2.grid(row=5, column=3, pady=10)
rad3.grid(row=5, column=4, pady=10)
rad_val.trace_add('write', change_radio)  # Will call 'change_radio' whenever any radio button is pressed

# ======================================================================================================================
# Scrolled Text ROW 6
# ======================================================================================================================
stxt_value = IntVar()
stxt_value.set(3)
stxt = scrolledtext.ScrolledText(win,width=40,height=10) #dimensions are characters not pixels
stxt.grid(row=6, column=2, columnspan=3)
stxt.insert(INSERT,'Your text goes here')
#stxt.delete(1.0,END) # deletes text box DONT UNDERSTAND ARGUMENTS YET

# ======================================================================================================================
# Spin Box ROW 7
# ======================================================================================================================
sp_value = IntVar()
sp_value.set(3)
spin = Spinbox(win, from_=0, to=10, width=5, textvariable=sp_value)
spin.grid(row=7, column=3, pady=30)


# ======================================================================================================================
# Progressbar widget ROW 8
# ======================================================================================================================
bar = Progressbar(win, orient='horizontal', mode='determinate', length = 200, style = "black.Horizontal.TProgressbar")
bar['value'] = 70
# pass the objects bar and win to external function and you can update the bar['value']0 -> 100 followed by win.update()
bar.grid(row = 8, column = 3)


# ======================================================================================================================
# Open File Dialog ROW 9
# ======================================================================================================================
def openfile():
    file_name = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*")),
                                           initialdir= 'C:\\PICKUP') # current_path = os.path.dirname(__file__)
    print(file_name)
    #filedialog.askopenfilenames() # ask for multiple files
    #filedialog.askdirectory()     # ask for a directory

    
btn_a = Button(win, text = "OpenFiles2", bg = "darkred", fg = "white", font = ("Verdana Bold",10), command = openfile)
btn_a.grid(row=10, column = 3)


# ======================================================================================================================
# Button ROW 10
# ======================================================================================================================

def click():
    text_value = txt1.get()
    combo_value = cmb_number.get()
    check_value = chk_val.get()
    radio_value = rad_val.get()
    scroll_value = stxt.get(1.0, END) 
    spin_value = sp_value.get()
    bar['value'] = bar['value']  + 10
    print(text_value, combo_value, check_value, radio_value, scroll_value, spin_value)
    lbl2a.configure(text=text_value) #configure modifies values set with constructor 'Label'
    message.set(text_value)


# Message Boxes
##    messagebox.showinfo('Message title', 'Message content')
##    messagebox.showwarning('Message title', 'Message content')  #shows warning message
##    messagebox.showerror('Message title', 'Message content')    #shows error message
##    res = messagebox.askquestion('Message title','Message content') # Yes / No buttons that return  'yes' or 'no'
##    res = messagebox.askyesno('Message title','Message content') #appears same as askquestion
##    res = messagebox.askyesnocancel('Message title','Message content')
##    res = messagebox.askokcancel('Message title','Message content')
##    res = messagebox.askretrycancel('Message title','Message content')

btn_b = Button(win, text='ENTER', width=5,bg='white', fg='darkred', font = ("Verdana Bold",10), command=click)
btn_b. grid(row=10, column=4, sticky=W, pady=10)

# ======================================================================================================================
# bind the <Return> key to a function
# ======================================================================================================================
def func(event):
    print("You hit return.")
win.bind('<Return>', func)


# see https://likegeeks.com/python-gui-examples-tkinter-tutorial/

# ======================================================================================================================
# NOTEBOOK WIDGET === TABS
# ======================================================================================================================
# Add Notebook widget (tab) --> uses ttk
# -- tab_control = ttk.Notebook(win) 
# -- tab1 = ttk.Frame(tab_control)
# -- tab_control.add(tab1, text='First')
# -- tab_control.pack(expand=1, fill='both')

# Add widgets to Notebook
# -- tab_control = ttk.Notebook(window)
# -- tab1 = ttk.Frame(tab_control)
# -- tab2 = ttk.Frame(tab_control)
# -- tab_control.add(tab1, text='First')
# -- tab_control.add(tab2, text='Second')
# -- lbl1 = Label(tab1, text= 'label1')
# -- lbl1.grid(column=0, row=0)
# -- lbl2 = Label(tab2, text= 'label2')
# -- lbl2.grid(column=0, row=0)
# -- tab_control.pack(expand=1, fill='both')


win.mainloop()
