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
def discc():
    m=membership.get()
    if m=="Select":
        messagebox.showinfo("RMS","Please Select Membership First")
    elif m=="Temporary":
        discount.set("2%")
    elif m=="Basic":
        discount.set("5%")
    elif m=="Premium":
        discount.set("10%")
    elif m=="Platinum":
        discount.set("20%")
def reset():
    identity.set("")
    name.set("")
    address.set("")
    mobile.set("")
    membership.set("Select")
    discount.set("")
def add():
    try:
        i=identity.get()
        n=name.get()
        a=address.get()
        mb=mobile.get()
        m=membership.get()
        d=discount.get()
        if i=="":
            messagebox.showinfo("RMS","Please Generate ID")
        elif n=="":
            messagebox.showinfo("RMS","Please Enter Name")
        elif a=="":
            messagebox.showinfo("RMS","Please Enter Address")
        elif mb=="":
            messagebox.showinfo("RMS","Please Enter Mobile Number")
        elif m=="Select":
            messagebox.showinfo("RMS","Please Select Membership")
        elif d=="":
            messagebox.showinfo("RMS","Please Check Discount")
        else:
            if len(mb)==10:
                if m=="Temporary":
                    d="2%"
                elif m=="Basic":
                    d="5%"
                elif m=="Premium":
                    d="10%"
                elif m=="Platinum":
                    d="20%"
                cur.execute("insert into custinfo values ("+str(i)+",'"+str(n)+"','"+str(a)+"','"+str(mb)+"','"+str(m)+"','"+str(d)+"')")
                cn.commit()
                wind.destroy()
                os.system("python customerloading.py")
            else:
                messagebox.showinfo("RMS","Please Enter Valid Mobile No.")
    except:
        winsound.PlaySound(r'Data\pysound\opunsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
        messagebox.showerror("RMS","Something Went Wrong\nTry to Check The Following:\n1)remove ( ' , : , ; , \ , / , > , < )\n2)no Quotes Allowed \n3) Use Numeric Digits In Mobile No.")
def rollback():
    wind.destroy()
    os.system("python custinterface.py")
def generateid():
    global count
    identity.set(str(count+1))
wind=Tk()
wind.title('Customer Info')
wind.geometry("400x365+300+150")
wind.config(bg=None)
wind.resizable(False,False)
wind.iconbitmap(r"Data\pyimage\logo.ico")
back=PhotoImage(file=r"Data\pyimage\babut.png")
ins=PhotoImage(file=r"Data\pyimage\insert.png")
res=PhotoImage(file=r"Data\pyimage\ref.png")
################################
identity=StringVar()
name=StringVar()
address=StringVar()
mobile=StringVar()
membership=StringVar()
discount=StringVar()
################################
l1=tkinter.Label(wind,text="Add New Customer",fg="red",bg=None,font=("Segoe Print",14))
l1.pack()
cur.execute("select * from custinfo")
result=cur.fetchall()
for i in result:
    count+=1
sett=count+1
l3=tkinter.Label(wind,text="---------------------------------------------------------------",fg="red",bg=None,font=(None,16)).pack()
l2=tkinter.Label(wind,text="Customer ID",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=70)
l3=tkinter.Label(wind,text="Name",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=100)
l4=tkinter.Label(wind,text="Address",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=130)
l5=tkinter.Label(wind,text="Mobile no.",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=160)
l6=tkinter.Label(wind,text="Membership",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=190)
l7=tkinter.Label(wind,text="Discount",fg="blue",bg=None,font=("Constantia",12)).place(x=30,y=220)
idd=ttk.Entry(wind,state="readonly",textvariable=identity).place(x=150,y=75)
b1=ttk.Button(wind,text="Generate ID",command=generateid).place(x=300,y=73)
#################################################
nme=ttk.Entry(wind,textvariable=name,state="normal").place(x=150,y=103)
ad=ttk.Entry(wind,textvariable=address,state="normal",width=35).place(x=150,y=133)
mn=ttk.Entry(wind,textvariable=mobile,state="normal").place(x=150,y=163)
mship=ttk.OptionMenu(wind,membership,"Select","Temporary","Basic","Premium","Platinum").place(x=150,y=193)
disc=ttk.Entry(wind,textvariable=discount,state="readonly").place(x=150,y=223)
b5=ttk.Button(wind,text="Check Discount",command=discc).place(x=300,y=220)
#################################################
b2=ttk.Button(wind,image=back,command=rollback).place(x=80,y=310)
b3=ttk.Button(wind,image=ins,command=add).place(x=150,y=260)
b4=ttk.Button(wind,image=res,command=reset).place(x=250,y=307)
wind.mainloop()
