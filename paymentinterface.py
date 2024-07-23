from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import mysql.connector as mycon
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
def history():
    win=Tk()
    win.title('Payments')
    win.geometry("565x250+180+150")
    win.config(bg="white")
    win.resizable(False,False)
    win.iconbitmap(r"Data\pyimage\logo.ico")
    cur.execute("select * from payinfo")
    result=cur.fetchall()
    scrollbar=ttk.Scrollbar(win)
    scrollbar.pack(side=RIGHT,fill=Y)
    mylist=Listbox(win,yscrollcommand=scrollbar.set,width=90)
    l1=tkinter.Label(win,text="Payments",fg="red",bg="white",font=("Segoe Print",14))
    l1.pack()
    l2=tkinter.Label(win,text="Pay ID",fg="red",bg="white",font=("Segoe Print",10)).place(x=10,y=40)
    l2=tkinter.Label(win,text="Ord ID",fg="red",bg="white",font=("Segoe Print",10)).place(x=70,y=40)
    l2=tkinter.Label(win,text="Cust ID",fg="red",bg="white",font=("Segoe Print",10)).place(x=140,y=40)
    l2=tkinter.Label(win,text="Amount",fg="red",bg="white",font=("Segoe Print",10)).place(x=230,y=40)
    l2=tkinter.Label(win,text="Discount",fg="red",bg="white",font=("Segoe Print",10)).place(x=320,y=40)
    l2=tkinter.Label(win,text="Membership",fg="red",bg="white",font=("Segoe Print",10)).place(x=440,y=40)
    for i in result:
        mylist.insert(END,str("%10s"%i[0])+str("%20s"%i[1])+str("%20s"%i[2])+str("%30s"%i[3])+str("%30s"%i[4])+str("%40s"%i[5])) 
    mylist.place(x=1,y=70)
    scrollbar.config(command=mylist.yview)
    win.mainloop()
def receivepayment():
    os.system("python receivepaymentinterface.py")
def homepress():
    win.destroy()
    os.system("python interface.py")
def lock():
    ans=messagebox.askquestion("RMS","Are you Sure Want to Logout")
    if ans=="yes":
        win.destroy()
        os.system("python ••••••Main••••••.py")
def sewin():
    os.system("python settingmain.py")
def qui():
    win.destroy()
win=Tk()
win.title('Resturant Management System')
win.geometry("300x200+350+200")
win.config(bg="white")
win.iconbitmap(r"Data\pyimage\logo.ico")
win.resizable(False,False)
l1=tkinter.Label(win,text="Payments",fg="red",bg="white",font=("Segoe Print",14))
l1.pack()
hb=PhotoImage(file=r"Data\pyimage\hom.png")
aboutimage=PhotoImage(file=r"Data\pyimage\abt.png")
logo=PhotoImage(file=r"Data\pyimage\logout.png")
ex=PhotoImage(file=r"Data\pyimage\exet.png")
sett=PhotoImage(file=r"Data\pyimage\sett.png")
user=PhotoImage(file=r"Data\pyimage\user.png")
p1=PhotoImage(file=r"Data\pyimage\interface\paymentinterface\receive.png")
p3=PhotoImage(file=r"Data\pyimage\interface\paymentinterface\ph.png")
b1=ttk.Button(win,image=p1,command=receivepayment)
b1.place(x=40,y=50)
b3=ttk.Button(win,image=p3,command=history)
b3.place(x=40,y=100)
##############################
homebutton=ttk.Button(win,image=hb,command=homepress)
homebutton.place(x=70,y=155)
logoutbutton=ttk.Button(win,image=logo,command=lock)
logoutbutton.place(x=110,y=155)
settingbutton=ttk.Button(win,image=sett,command=sewin)
settingbutton.place(x=150,y=155)
quitbutton=ttk.Button(win,image=ex,command=qui)
quitbutton.place(x=190,y=155)
win.mainloop()
