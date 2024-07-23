from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter import*
import tkinter
import os
import mysql.connector as mycon
from tkinter import messagebox
import tkinter as tk
orderr=["Burger","Pizza","Coldrink","Coffee","Tea","French Fries","Ice Cream","Donut","Cake","Pastry","Salad"]
ratelist=['59','99','29','49','19','49','58','89','299','39','39',]
li=["January","February","March","April","May","June","July","August","September","October","November","December"]
count=0
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
import winsound
def price():
        ids=str(identity.get())
        o=str(order.get())
        d=str(date.get())
        m=str(month.get())
        n=str(name.get())
        y=str(year.get())
        q=int(quantity.get())
        s=str(amount.get())
        if n=="":
            messagebox.showinfo("RMS","Please Enter Table No.")
        elif n>=str(21):
            messagebox.showinfo("RMS","Please Enter Valid Table No.")
        elif ids=="":
            messagebox.showinfo("RMS","Please Generate ID")
        elif o=="Select":
            messagebox.showinfo("RMS","Please Select Order")
        elif d=="Date":
            messagebox.showinfo("RMS","Please Select Date")
        elif m=="Month":
            messagebox.showinfo("RMS","Please Select Month")
        elif y=="Year":
            messagebox.showinfo("RMS","Please Select Year")
        else:
            if n<=str(20):
                
                q=int(quantity.get())
                o=order.get()
                for i in orderr:
                    if str(i)==str(o):
                        index=orderr.index(i)
                        amountt=int(ratelist[index])
                        amount.set(amountt*q)
            else:
                messagebox.showerror("RMS","Invalid Table Number")
def plusorder():
    q=int(quantity.get())
    quantity.set(q+1)
    globalquantity=q+1
def minusorder():
    q=int(quantity.get())
    if q!=1:
        quantity.set(q-1)
        globalquantity=q-1
def reset():
    identity.set("")
    order.set("Select")
    quantity.set(1)
    date.set("Date")
    month.set("Month")
    year.set("Year")
    amount.set("0")
    name.set("Enter Table Number")
def add():
    amountt=0
    mainmonth='0'
    c=0
    globalindex=0
    ids=str(identity.get())
    o=str(order.get())
    d=str(date.get())
    m=str(month.get())
    y=str(year.get())
    q=str(quantity.get())
    s=str(amount.get())
    n=name.get()
    if n=="":
        messagebox.showinfo("RMS","Please Enter Table No.")
    elif n>=str(21):
        messagebox.showinfo("RMS","Please Enter Valid Table No.")
    elif ids=="":
        messagebox.showinfo("RMS","Please Generate ID")
    elif o=="Select":
        messagebox.showinfo("RMS","Please Select Order")
    elif d=="Date":
        messagebox.showinfo("RMS","Please Select Date")
    elif m=="Month":
        messagebox.showinfo("RMS","Please Select Month")
    elif y=="Year":
        messagebox.showinfo("RMS","Please Select Year")
    elif s=='0' or s=="" or s==0:
        messagebox.showinfo("RMS","Please Generate Price")
    else:
        for i in li:
            if m==i:
                c=li.index(i)
        maindate=str(d)+"/"+str(m)+"/"+str(y)
        cur.execute("insert into orderinfo values ("+str(ids)+",'"+str(o)+"','"+str(maindate)+"','"+str(q)+"',"+str(s)+",'"+str(n)+"')")
        cn.commit()
        winsound.PlaySound(r'Data\pysound\operationsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
        messagebox.showinfo("RMS","Order Added Sucessfully")
        wind.destroy()
        os.system("python orderinterface.py")
def rollback():
    wind.destroy()
    os.system("python orderinterface.py")
def generateid():
    global count
    identity.set(str(count+1))
wind=Tk()
wind.title('Order Info')
wind.geometry("400x335+300+150")
wind.config(bg=None)
wind.resizable(False,False)
wind.iconbitmap(r"Data\pyimage\logo.ico")
back=PhotoImage(file=r"Data\pyimage\babut.png")
ins=PhotoImage(file=r"Data\pyimage\insert.png")
res=PhotoImage(file=r"Data\pyimage\ref.png")
################################
identity=tk.StringVar()
order=StringVar()
date=StringVar()
month=StringVar()
year=StringVar()
quantity=StringVar()
amount=IntVar()
name=StringVar()
################################
l1=tkinter.Label(wind,text="Add New Order",fg="red",bg=None,font=("Segoe Print",14))
l1.pack()
cur.execute("select * from orderinfo")
result=cur.fetchall()
for i in result:
    count+=1
sett=count+1
l3=tkinter.Label(wind,text="---------------------------------------------------------------",fg="red",bg=None,font=(None,16)).pack()
l2=tkinter.Label(wind,text="Order ID",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=70)
l3=tkinter.Label(wind,text="Order",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=100)
l4=tkinter.Label(wind,text="Date",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=130)
l5=tkinter.Label(wind,text="Quantity",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=160)
qty=ttk.Entry(wind,textvariable=quantity,state="readonly").place(x=180,y=163)
l6=tkinter.Label(wind,text="Amount",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=190)
idd=ttk.Entry(wind,state="readonly",textvariable=identity).place(x=150,y=75)
quantity.set(1)
b1=ttk.Button(wind,text="Generate ID",command=generateid).place(x=300,y=73)
orde=ttk.OptionMenu(wind,order,"Select","Burger","Pizza","Coldrink","Coffee","Tea","French Fries","Ice Cream","Donut","Cake","Pastry","Salad").place(x=150,y=103)
dt=ttk.OptionMenu(wind,date,"Date"," 01 "," 02 "," 03 "," 04 "," 05 "," 06 "," 07 "," 08 "," 09 "," 10 "," 11 "," 12 "," 13 "," 14 "," 15 "," 16 "," 17 "," 18 "," 19 "," 20 "," 21 "," 22 "," 23 "," 24 "," 25 "," 26 "," 27 "," 28 "," 29 "," 30 "," 31 ").place(x=150,y=135)
mn=ttk.OptionMenu(wind,month,"Month","01","02","03","04","05","06","07","08","09","10","11","12").place(x=210,y=135)
yr=ttk.OptionMenu(wind,year,"Year"," 2017 "," 2018 "," 2019 "," 2020 ").place(x=300,y=135)
amt=ttk.Entry(wind,state="readonly",textvariable=amount).place(x=150,y=195)
b2=ttk.Button(wind,image=back,command=rollback).place(x=80,y=280)
b3=ttk.Button(wind,image=ins,command=add).place(x=150,y=230)
b4=ttk.Button(wind,image=res,command=reset).place(x=250,y=277)
b5=ttk.Button(wind,text="-",command=minusorder,width=2).place(x=150,y=160)
b5=ttk.Button(wind,text="+",command=plusorder,width=2).place(x=310,y=160)
b6=ttk.Button(wind,text="Generate Price",command=price).place(x=300,y=195)
e1=ttk.Entry(wind,textvariable=name).place(x=140,y=30)
name.set("Enter Table No.")
wind.mainloop()
