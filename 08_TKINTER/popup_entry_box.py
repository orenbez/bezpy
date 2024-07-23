import tkinter as tk

class InputBox:

    def __init__(self, rt):
        # The Tkinter Toplevel Widget (c.f. with frame)
        top = self.top = tk.Toplevel(rt)
        #Label
        self.myLabel = tk.Label(top, text='Enter your username below')
        self.myLabel.pack()
        #Entry Box
        self.myEntryBox = tk.Entry(top)
        self.myEntryBox.pack()
        #Submit Button
        self.mySubmitButton = tk.Button(top, text='Submit', command=self.send)
        self.mySubmitButton.pack()

    def send(self):
        self.username = self.myEntryBox.get()
        self.top.destroy()


def onClick():
    ip = InputBox(root)
    root.wait_window(ip.top)
    print('Username: ', ip.username)



root = tk.Tk()
mainLabel = tk.Label(root, text='Example for pop up input box')
mainLabel.pack()

mainButton = tk.Button(root, text='Click me', command=onClick)
mainButton.pack()

root.mainloop()
