from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter import*
import tkinter
import os
import mysql.connector as mycon
from tkinter import messagebox
import tkinter as tk
import winsound
li=["January","February","March","April","May","June","July","August","September","October","November","December"]
count=0
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
def reset():
    identity.set("")
    name.set("")
    position.set("Select")
    date.set("Date")
    month.set("Month")
    year.set("Year")
    salary.set("Select")
def add():
    mainmonth='0'
    c=""
    ids=str(identity.get())
    n=str(name.get())
    p=str(position.get())
    d=str(date.get())
    m=str(month.get())
    y=str(year.get())
    s=str(salary.get())
    if ids=="":
        messagebox.showinfo("RMS","Please Generate ID")
    elif n=="":
        messagebox.showinfo("RMS","Please Enter Name")
    elif p=="Select":
        messagebox.showinfo("RMS","Please Select Post")
    elif d=="Date":
        messagebox.showinfo("RMS","Please Select Date")
    elif m=="Month":
        messagebox.showinfo("RMS","Please Select Month")
    elif y=="Year":
        messagebox.showinfo("RMS","Please Select Year")
    elif s=="Select":
        messagebox.showinfo("RMS","Please Select Salary")
    else:
        for i in li:
            if m==i:
                c=li.index(i)
        
        mainmonth=c+1
        if len(str(mainmonth))==1:
            mainmonth="0"+str(mainmonth)
        maindate=str(y.strip())+"-"+str(mainmonth.strip())+"-"+str(d.strip())
        messagebox.showinfo(str(maindate))
        cur.execute("insert into empinfo values ("+str(ids)+",'"+str(n)+"','"+str(p)+"','"+str(maindate)+"',"+str(s)+")")
        cn.commit()
        wind.destroy()
        os.system("python insertloading.py")
def rollback():
    wind.destroy()
    os.system("python employeeinterface.py")
def generateid():
    global count
    identity.set(str(count+1))
wind=Tk()
wind.title('Employee Info')
wind.geometry("400x335+300+150")
wind.config(bg=None)
wind.resizable(False,False)
wind.iconbitmap(r"Data\pyimage\logo.ico")
back=PhotoImage(file=r"Data\pyimage\babut.png")
ins=PhotoImage(file=r"Data\pyimage\insert.png")
res=PhotoImage(file=r"Data\pyimage\ref.png")
################################
identity=tk.StringVar()
position=tk.StringVar()
name=StringVar()
salary=StringVar()
date=StringVar()
month=StringVar()
year=StringVar()
################################
l1=tkinter.Label(wind,text="Add New Employee",fg="red",bg=None,font=("Segoe Print",14))
l1.pack()
cur.execute("select * from empinfo")
result=cur.fetchall()
for i in result:
    count+=1
sett=count+1
l3=tkinter.Label(wind,text="---------------------------------------------------------------",fg="red",bg=None,font=(None,16)).pack()
l2=tkinter.Label(wind,text="Employee ID",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=70)
l3=tkinter.Label(wind,text="Name",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=100)
l4=tkinter.Label(wind,text="Post",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=130)
l5=tkinter.Label(wind,text="Joining Date",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=160)
l6=tkinter.Label(wind,text="Salary",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=190)
idd=ttk.Entry(wind,state="readonly",textvariable=identity).place(x=150,y=75)
b1=ttk.Button(wind,text="Generate ID",command=generateid).place(x=300,y=73)
na=ttk.Entry(wind,state="normal",textvariable=name).place(x=150,y=105)
post=ttk.OptionMenu(wind,position,"Select","Advertiser","Carpeneter","Cook","Decorator","Delivery Boy","Electrition","Manager","Mechanic","Sales","Sweeper","Waiter").place(x=150,y=135)
dt=ttk.OptionMenu(wind,date,"Date"," 01 "," 02 "," 03 "," 04 "," 05 "," 06 "," 07 "," 08 "," 09 "," 10 "," 11 "," 12 "," 13 "," 14 "," 15 "," 16 "," 17 "," 18 "," 19 "," 20 "," 21 "," 22 "," 23 "," 24 "," 25 "," 26 "," 27 "," 28 "," 29 "," 30 "," 31 ").place(x=150,y=163)
mn=ttk.OptionMenu(wind,month,"Month","January","February","March","April","May","June","July","August","September","October","November","December").place(x=210,y=163)
yr=ttk.OptionMenu(wind,year,"Year"," 2017 "," 2018 "," 2019 "," 2020 ").place(x=300,y=163)
sal=ttk.OptionMenu(wind,salary,"Select"," 30000 "," 40000 "," 50000 "," 60000 "," 70000 "," 80000 "," 90000 "," 100000 "," 110000 "," 120000 "," 130000 "," 140000 "," 150000 "," 160000 "," 170000 "," 180000 "," 190000 "," 200000 "," 210000 "," 220000 "," 230000 "," 240000 "," 250000 "," 260000 "," 270000 "," 280000 "," 290000 "," 300000 ").place(x=150,y=195)
b2=ttk.Button(wind,image=back,command=rollback).place(x=80,y=280)
b3=ttk.Button(wind,image=ins,command=add).place(x=150,y=230)
b4=ttk.Button(wind,image=res,command=reset).place(x=250,y=277)
wind.mainloop()
