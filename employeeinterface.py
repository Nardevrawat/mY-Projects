from tkinter.ttk import *
from tkinter import*
import tkinter
import os
import mysql.connector as mycon
from tkinter import messagebox
count=0
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
def deleteemployee():
    win.destroy()
    os.system("python deleteemployeeinterface.py")
def updateemployee():
    win.destroy()
    os.system("python updateemployeeinterface.py")
def newemployee():
    win.destroy()
    os.system("python newemployeeinterface.py")
def allemployee():
    cur.execute("create table if not exists empinfo (emp_id int,emp_name varchar(2000),post varchar(2000),joining_date varchar(2000),salary int)")
    win=Tk()
    win.title('Employee Info')
    win.geometry("730x500+180+150")
    win.config(bg="white")
    win.resizable(False,False)
    win.iconbitmap(r"Data\pyimage\logo.ico")
    cur.execute("select * from empinfo")
    result=cur.fetchall()
    scrollbar=ttk.Scrollbar(win)
    scrollbar.pack(side=RIGHT,fill=Y)
    mylist=Listbox(win,yscrollcommand=scrollbar.set,width=150)
    l1=tkinter.Label(win,text="Employee Info",fg="red",bg="white",font=("Segoe Print",14))
    l1.pack()
    l2=tkinter.Label(win,text="Emp ID\t\tEmp Name\t\tEmpPost\t\tJoining Date\tSalary",fg="red",bg="white",font=("Segoe Print",10))
    l2.pack()
    for i in result:
        mylist.insert(END,str("%10s"%i[0])+str("%60s"%i[1])+str("%45s"%i[2])+str("%40s"%i[3])+str("%50s"%i[4])) 
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
l1=tkinter.Label(win,text="Employee Info",fg="red",bg="white",font=("Segoe Print",14))
l1.pack()
hb=PhotoImage(file=r"Data\pyimage\hom.png")
aboutimage=PhotoImage(file=r"Data\pyimage\abt.png")
logo=PhotoImage(file=r"Data\pyimage\logout.png")
ex=PhotoImage(file=r"Data\pyimage\exet.png")
sett=PhotoImage(file=r"Data\pyimage\sett.png")
user=PhotoImage(file=r"Data\pyimage\user.png")
p1=PhotoImage(file=r"Data\pyimage\interface\employeeinterface\allemp.png")
p2=PhotoImage(file=r"Data\pyimage\interface\employeeinterface\newemp.png")
p3=PhotoImage(file=r"Data\pyimage\interface\employeeinterface\updateemp.png")
p4=PhotoImage(file=r"Data\pyimage\interface\employeeinterface\deleteemp.png")
b1=ttk.Button(win,image=p1,command=allemployee)
b1.place(x=20,y=60)
b2=ttk.Button(win,image=p2,command=newemployee)
b2.place(x=20,y=110)
b3=ttk.Button(win,image=p3,command=updateemployee)
b3.place(x=20,y=160)
b4=ttk.Button(win,image=p4,command=deleteemployee)
b4.place(x=20,y=210)
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
