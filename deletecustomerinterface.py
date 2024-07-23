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
globalid=0
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
def rollback():
    wind.destroy()
    os.system("python employeeinterface.py")
def findrec():
    try:
        global globalid
        idd=int(identity.get())
        globalid=idd
        if idd>count:
            messagebox.showinfo("RMS","No Such Customer")
            identity.set("")
            name.set("")
            address.set("")
            mobile.set("")
            membership.set("Select")
            discount.set("")
        else:
            wind.geometry("400x365+300+150")
            cur.execute("select * from custinfo")
            result=cur.fetchall()
            for i in result:
                if str(i[0])==str(idd):
                    identity.set(str(idd))
                    name.set(str(i[1]))
                    address.set(str(i[2]))
                    mobile.set(str(i[3]))
                    membership.set(str(i[4]))
                    discount.set(str(i[5]))
    except ValueError:
        messagebox.showinfo("RMS","Please Enter ID to Find")
def dell():
    ans=messagebox.askquestion("RMS","Are You Sure To Delete")
    if ans=="yes":
        idd=identity.get()
        cur.execute("delete from custinfo where cust_id="+str(idd))
        cn.commit()
        winsound.PlaySound(r'Data\pysound\operationsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
        messagebox.showinfo("RMS","Operation Sucessful")
        wind.destroy()
        os.system("python custinterface.py")
        
wind=Tk()
wind.title('Customer Info')
wind.geometry("400x100+300+150")
wind.config(bg=None)
wind.resizable(False,False)
wind.iconbitmap(r"Data\pyimage\logo.ico")
back=PhotoImage(file=r"Data\pyimage\babut.png")
ins=PhotoImage(file=r"Data\pyimage\update.png")
res=PhotoImage(file=r"Data\pyimage\ref.png")
################################
################################
identity=StringVar()
name=StringVar()
address=StringVar()
mobile=StringVar()
membership=StringVar()
discount=StringVar()
################################
l1=tkinter.Label(wind,text="Delete Customer",fg="red",bg=None,font=("Segoe Print",14))
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
idd=ttk.Entry(wind,state="normal",textvariable=identity).place(x=150,y=75)
b1=ttk.Button(wind,text="Find",command=findrec).place(x=300,y=73)
#################################################
nme=ttk.Entry(wind,textvariable=name,state="readonly").place(x=150,y=103)
ad=ttk.Entry(wind,textvariable=address,state="readonly",width=35).place(x=150,y=133)
mn=ttk.Entry(wind,textvariable=mobile,state="readonly").place(x=150,y=163)
mship=ttk.OptionMenu(wind,membership,"Select","Temporary","Basic","Premium","Platinum").place(x=150,y=193)
disc=ttk.Entry(wind,textvariable=discount,state="readonly").place(x=150,y=223)
b5=ttk.Button(wind,text="Check Discount",command=discc).place(x=300,y=220)
#################################################
b2=ttk.Button(wind,image=back,command=rollback).place(x=80,y=310)
b3=ttk.Button(wind,text="Delete",command=dell).place(x=150,y=260)
b4=ttk.Button(wind,image=res,command=reset).place(x=250,y=307)
wind.mainloop()
