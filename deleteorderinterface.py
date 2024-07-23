from tkinter.ttk import *
import tkinter.ttk as ttk
from tkinter import*
import tkinter
import os
import mysql.connector as mycon
from tkinter import messagebox
import tkinter as tk
import winsound
orderr=["Burger","Pizza","Coldrink","Coffee","Tea","French Fries","Ice Cream","Donut","Cake","Pastry","Salad"]
ratelist=['59','99','29','49','19','49','58','89','299','39','39',]
li=["January","February","March","April","May","June","July","August","September","October","November","December"]
count=0
globalid=0
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
def reset():
    wind.geometry("400x100+300+150")
    identity.set("")
    order.set("Select")
    quantity.set(1)
    date.set("Date")
    month.set("Month")
    year.set("Year")
    amount.set("0")
    name.set("Enter Table Number")
    wind.mainloop()
def add():
        global globalidd
        mainmonth='0'
        c=""
        ids=str(identity.get())
        o=str(order.get())
        d=str(date.get())
        m=str(month.get())
        n=int(name.get())
        y=str(year.get())
        q=int(quantity.get())
        s=str(amount.get())
        if n=="":
            messagebox.showinfo("RMS","Please Enter Table No.")
        elif n>=21:
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
            maindate=str(d)+"/"+str(m)+"/"+str(y)
            ans=messagebox.askquestion("RMS","Are you Sure To Delete")
            if ans=='yes':
                cur.execute("delete from orderinfo where order_id="+str(globalid))
                cn.commit()
                messagebox.showinfo("RMS","Deletion Sucessful")
                winsound.PlaySound(r'Data\pysound\operationsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
                wind.destroy()
                os.system("python orderinterface.py")
def rollback():
    wind.destroy()
    os.system("python orderinterface.py")
def findrec():
    try:
        global globalid
        idd=identity.get()
        globalid=idd
        if int(idd)>int(count):
            messagebox.showinfo("RMS","No Such Order")
            identity.set("")
            order.set("Select")
            quantity.set(1)
            date.set("Date")
            month.set("Month")
            year.set("Year")
            amount.set("0")
            name.set("Enter Table Number")
        else:
            wind.geometry("400x335+300+150")
            e1=ttk.Entry(wind,textvariable=name).place(x=140,y=30)
            datelist=[]
            cur.execute("select * from orderinfo")
            result=cur.fetchall()
            for i in result:
                if str(i[0])==str(idd):
                    identity.set(str(idd))
                    order.set(str(i[1]))
                    quantity.set(str(i[3]))
                    date.set(str(i[2]))
                    amount.set(str(i[4]))
                    name.set(str(i[5]))
    except ValueError:
        messagebox.showinfo("RMS","Please Enter ID to Find")
            
wind=Tk()
wind.title('Order Info')
wind.geometry("400x100+300+150")
wind.config(bg=None)
wind.resizable(False,False)
wind.iconbitmap(r"Data\pyimage\logo.ico")
back=PhotoImage(file=r"Data\pyimage\babut.png")
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
l1=tkinter.Label(wind,text="Delete Order",fg="red",bg=None,font=("Segoe Print",14))
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
idd=ttk.Entry(wind,state="normal",textvariable=identity).place(x=150,y=75)
quantity.set(1)
b1=ttk.Button(wind,text="Find",command=findrec).place(x=300,y=73)
orde=ttk.OptionMenu(wind,order,"Select","Burger","Pizza","Coldrink","Coffee","Tea","French Fries","Ice Cream","Donut","Cake","Pastry","Salad").place(x=150,y=103)
dt=ttk.Entry(wind,textvariable=date,state='readonly').place(x=150,y=133)
amt=ttk.Entry(wind,state="readonly",textvariable=amount).place(x=150,y=195)
b2=ttk.Button(wind,image=back,command=rollback).place(x=80,y=280)
b3=ttk.Button(wind,text="Delete",command=add).place(x=150,y=230)
b4=ttk.Button(wind,image=res,command=reset).place(x=250,y=277)
b5=ttk.Button(wind,text="-",width=2).place(x=150,y=160)
b5=ttk.Button(wind,text="+",width=2).place(x=310,y=160)
wind.mainloop()
