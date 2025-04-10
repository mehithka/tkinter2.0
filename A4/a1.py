from tkinter import *

root = Tk()
root.geometry('400x500')
root.title('Main')

def topwin():
    top = Toplevel()
    top.geometry('180x100')
    top.title('toplvl')
    l2 = Label(top,text = 'This is toplvl window')
    l2.pack()

    top.mainloop()

l = Label(root,text ='this is the root window or main window')
btn = Button(root,text = 'Click here to open another window', command=topwin)

l.pack()
btn.pack()
root.mainloop()