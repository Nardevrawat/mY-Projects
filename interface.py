from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import random
import winsound
colors=["red","blue","green","cyan"]
def tick():
    global h,m,s
    cur_time=("Azhar Ansari")
    clock.config(text=cur_time,fg=random.choice(colors))
    clock.after(1000,tick)
def employeepress():
    win.destroy()
    os.system("python employeeinterface.py")
def homepress():
    messagebox.showinfo("RMS","Already at Home")
def lock():
    ans=messagebox.askquestion("RMS","Are you Sure Want to Logout")
    if ans=="yes":
        win.destroy()
        os.system("python ••••••Main••••••.py")
def sewin():
    os.system("python settingmain.py")
def qui():
    win.destroy()
def orderpress():
    win.destroy()
    os.system("python orderinterface.py")
def custpress():
    win.destroy()
    os.system("python custinterface.py")
def paymentpress():
    win.destroy()
    os.system("python paymentinterface.py")
win=Tk()
win.title('Resturant Management System')
win.geometry("380x290+300+200")
win.config(bg="white")
win.iconbitmap(r"Data\pyimage\logo.ico")
win.resizable(False,False)
clock = Label(win,font=('Segoe Print',14,'bold'),bg='white')
clock.place(x=120,y=250)
tick()
l1=tkinter.Label(win,text="Resturant Management System",fg="red",bg="white",font=("Segoe Print",14))
l1.pack()
hb=PhotoImage(file=r"Data\pyimage\hom.png")
aboutimage=PhotoImage(file=r"Data\pyimage\abt.png")
logo=PhotoImage(file=r"Data\pyimage\logout.png")
ex=PhotoImage(file=r"Data\pyimage\exet.png")
sett=PhotoImage(file=r"Data\pyimage\sett.png")
p1=PhotoImage(file=r"Data\pyimage\interface\empinfo.png")
p5=PhotoImage(file=r"Data\pyimage\interface\custinfo.png")
p6=PhotoImage(file=r"Data\pyimage\interface\payments.png")
p7=PhotoImage(file=r"Data\pyimage\interface\orderinfo.png")
b1=ttk.Button(win,image=p1,command=employeepress)
b1.place(x=30,y=50)
b7=ttk.Button(win,image=p7,command=orderpress)
b7.place(x=30,y=100)
b5=ttk.Button(win,image=p5,command=custpress)
b5.place(x=30,y=150)
b6=ttk.Button(win,image=p6,command=paymentpress)
b6.place(x=30,y=200)
##############################
homebutton=ttk.Button(win,image=hb,command=homepress)
homebutton.place(x=340,y=60)
logoutbutton=ttk.Button(win,image=logo,command=lock)
logoutbutton.place(x=340,y=100)
settingbutton=ttk.Button(win,image=sett,command=sewin)
settingbutton.place(x=340,y=140)
quitbutton=ttk.Button(win,image=ex,command=qui)
quitbutton.place(x=340,y=180)
win.mainloop()
