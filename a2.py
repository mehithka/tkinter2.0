from tkinter import *

root =Tk()
root.title("login app")
root.geometry('400x400')


frame =  Frame(master=root, height = 200, width = 360,bg='#d0efff')

lbl1 = Label(frame,text = 'Full Name',bg ='#3895D3',fg = 'white',width=12)
lbl2 = Lable(frame,text = 'Email ID', bg = '#3895D3',fg = 'white', width=12)
lbl3 = Label(frame,text = 'Password', bg = '#3895D3',fg = 'white', width=12)