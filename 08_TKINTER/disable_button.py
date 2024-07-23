from tkinter import *

# Normal State is the default State
# Disables State is obvious
# Active State allows for mouseover button appearance changes


win = Tk()
win.title("Window")

def switch():
    if b1["state"] == "normal":
        b1["state"] = "disabled"
        b1["text"] = "disabled"

    elif b1["state"] == "disabled":
        b1["state"] = "active"
        b1["text"] = "active"
    else:
        b1["state"] = "normal"
        b1["text"] = "normal"

#--Buttons
b1 = Button(win, text="normal", height=5, width=7)
b1.grid(row=0, column=0)    

b2 = Button(text="switch_state", command=switch)
b2.grid(row=0, column=1)

win.mainloop()
