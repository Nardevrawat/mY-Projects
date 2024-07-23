from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import mysql.connector as mycon
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
def deleteorder():
    win.destroy()
    os.system("python deleteorderinterface.py")
def neworder():
    win.destroy()
    os.system("python neworderinterface.py")
def allorders():
    cur.execute("create table if not exists orderinfo (order_id int,order_name varchar(2000),date varchar(2000),quantity varchar(2000),amount int,table_no int)")
    win=Tk()
    win.title('Orders Info')
    win.geometry("800x500+180+150")
    win.config(bg="white")
    win.resizable(False,False)
    win.iconbitmap(r"Data\pyimage\logo.ico")
    cur.execute("select * from orderinfo")
    result=cur.fetchall()
    scrollbar=ttk.Scrollbar(win)
    scrollbar.pack(side=RIGHT,fill=Y)
    mylist=Listbox(win,yscrollcommand=scrollbar.set,width=150)
    l1=tkinter.Label(win,text="Order Info",fg="red",bg="white",font=("Segoe Print",14))
    l1.pack()
    l2=tkinter.Label(win,text="Order ID\t\t   Order\t\tDate\t\tQuantity\t\tAmount\tTable No.",fg="red",bg="white",font=("Segoe Print",10))
    l2.pack()
    for i in result:
        mylist.insert(END,str("%10s"%i[0])+str("%60s"%i[1])+str("%45s"%i[2])+str("%40s"%i[3])+str("%50s"%i[4])+str("%30s"%i[5])) 
    mylist.pack(side=LEFT,fill=BOTH)
    scrollbar.config(command=mylist.yview)
    win.mainloop()
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
win.geometry("340x270+350+200")
win.config(bg="white")
win.iconbitmap(r"Data\pyimage\logo.ico")
win.resizable(False,False)
l1=tkinter.Label(win,text="Orders Info",fg="red",bg="white",font=("Segoe Print",14))
l1.pack()
hb=PhotoImage(file=r"Data\pyimage\hom.png")
aboutimage=PhotoImage(file=r"Data\pyimage\abt.png")
logo=PhotoImage(file=r"Data\pyimage\logout.png")
ex=PhotoImage(file=r"Data\pyimage\exet.png")
sett=PhotoImage(file=r"Data\pyimage\sett.png")
user=PhotoImage(file=r"Data\pyimage\user.png")
p1=PhotoImage(file=r"Data\pyimage\interface\orderinterface\allorders.png")
p2=PhotoImage(file=r"Data\pyimage\interface\orderinterface\neworder.png")
p3=PhotoImage(file=r"Data\pyimage\interface\orderinterface\pendingorder.png")
p4=PhotoImage(file=r"Data\pyimage\interface\orderinterface\deleteorder.png")
b1=ttk.Button(win,image=p1,command=allorders)
b1.place(x=20,y=80)
b2=ttk.Button(win,image=p2,command=neworder)
b2.place(x=20,y=130)
b4=ttk.Button(win,image=p4,command=deleteorder)
b4.place(x=20,y=180)
##############################
homebutton=ttk.Button(win,image=hb,command=homepress)
homebutton.place(x=300,y=60)
logoutbutton=ttk.Button(win,image=logo,command=lock)
logoutbutton.place(x=300,y=100)
settingbutton=ttk.Button(win,image=sett,command=sewin)
settingbutton.place(x=300,y=140)
quitbutton=ttk.Button(win,image=ex,command=qui)
quitbutton.place(x=300,y=180)
win.mainloop()
