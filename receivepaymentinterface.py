from tkinter.ttk import *
import tkinter
from tkinter import *
import os
import mysql.connector as mycon
from tkinter import messagebox
import winsound
count=0
ordercount=0
customercount=0
asliamount=0
aslidiscount=0
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
cur.execute("create table if not exists payinfo (payment_id varchar(2000),order_id varchar(2000),customer_id varchar(2000),amount varchar(2000),discount varchar(2000),membership varchar(2000))")
cn.commit()
cur.execute("select * from payinfo")
resulttt=cur.fetchall()
for i in resulttt:
     count+=1
def receive():
    global count
    global aslidiscount
    oid=orderid.get()
    cid=customerid.get()
    a=amount.get()
    d=discount.get()
    m=membership.get()
    cur.execute("insert into payinfo values ('"+str(count+1)+"','"+str(oid)+"','"+str(cid)+"','"+str(a)+"','"+str(d)+"','"+str(m)+"')")
    ans=messagebox.askquestion("RMS","Are You Sure Want To Insert Record With Payment ID "+str(count+1))
    if ans=="yes":
        winsound.PlaySound(r'Data\pysound\operationsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
        cn.commit()
        messagebox.showinfo("RMS","Sucessful")
        reset()
def reset():
    win.geometry("360x75+340+200")
    e1.config(state="normal")
    e2.config(state="normal")
    orderid.set("")
    customerid.set("")
    order.set("")
    quantity.set("")
    amount.set("")
    membership.set("")
    discount.set("")
    pamount.set("")
    b4.place(x=5000,y=5000)
def customercheck():
    global aslidiscount
    ci=customerid.get()
    if ci>str(customercount):
        messagebox.showinfo("RMS","No Such Customer")
    elif ci=="":
        messagebox.showinfo("RMS","Please Enter Customer ID")
    elif ci<=str(customercount):
        disc=[]
        win.geometry("360x430+340+200")
        e2.config(state="readonly")
        b4.pack(side=BOTTOM)
        cur.execute("select * from custinfo")
        results=cur.fetchall()
      #  print(results)
        for i in results:
            if i[0]==int(ci):
                membership.set(i[4])
                discount.set(i[5])
                aslidiscount=i[5]
                for i in aslidiscount:
                    disc.append(i)
                if len(disc)==3:
                    aslidiscount=str(disc[0])+str(disc[1])
                elif len(disc)==2:
                    aslidiscount=str(disc[0])
                disc=int(aslidiscount)/100*int(asliamount)
                #print("Discount = ",disc)
                rate=int(asliamount)-int(disc)
                #print(rate)
                pamount.set(str(rate))
def ordercheck():
    global asliamount
    oi=orderid.get()
    if oi>str(ordercount):
        messagebox.showinfo("RMS","No Such Orders")
    elif oi=="":
        messagebox.showinfo("RMS","Please Enter Order ID")
    elif oi<=str(ordercount):
        win.geometry("360x120+340+200")
        e1.config(state="readonly")
        cur.execute("select * from orderinfo")
        results=cur.fetchall()
        #print(results)
        for i in results:
            if i[0]==int(oi):
                order.set(i[1])
                quantity.set(i[3])
                amount.set(i[4])
                asliamount=i[4]
          #      print(asliamount)
win=Tk()
win.title('Payment')
win.geometry("360x75+340+200")
win.config(bg=None)
win.iconbitmap(r"Data\pyimage\logo.ico")
win.resizable(False,False)
orderid=StringVar()
customerid=StringVar()
order=StringVar()
quantity=StringVar()
amount=StringVar()
membership=StringVar()
discount=StringVar()
pamount=StringVar()
cur.execute("select*from orderinfo")
result=cur.fetchall()
for i in result:
    ordercount+=1
cur.execute("select*from custinfo")
result=cur.fetchall()
for i in result:
    customercount+=1
l1=tkinter.Label(win,text="Receive Payment",fg="red",bg=None,font=("Segoe Print",14))
l1.pack()
l2=tkinter.Label(win,text="Enter Order ID",fg="blue",bg=None,font=("Constantia",12)).place(x=20,y=50)
e1=ttk.Entry(win,textvariable=orderid)
e1.config(state="normal")
e1.place(x=140,y=50)
b1=ttk.Button(win,text="Check",command=ordercheck).place(x=270,y=47)
l3=tkinter.Label(win,text="Enter Customer ID",fg="blue",bg=None,font=("Constantia",12)).place(x=15,y=90)
e2=ttk.Entry(win,textvariable=customerid)
e2.config(state="normal")
e2.place(x=150,y=90)
b2=ttk.Button(win,text="Check",command=customercheck).place(x=280,y=87)
l4=tkinter.Label(win,text="Order",fg="blue",bg=None,font=("Constantia",12)).place(x=15,y=130)
e3=ttk.Entry(win,textvariable=order,state="readonly").place(x=150,y=130)
l5=tkinter.Label(win,text="Quantity",fg="blue",bg=None,font=("Constantia",12)).place(x=15,y=170)
e4=ttk.Entry(win,textvariable=quantity,state="readonly").place(x=150,y=170)
l6=tkinter.Label(win,text="Amount",fg="blue",bg=None,font=("Constantia",12)).place(x=15,y=210)
e5=ttk.Entry(win,textvariable=amount,state="readonly").place(x=150,y=210)
l6=tkinter.Label(win,text="Membership",fg="blue",bg=None,font=("Constantia",12)).place(x=15,y=250)
e5=ttk.Entry(win,textvariable=membership,state="readonly").place(x=150,y=250)
l6=tkinter.Label(win,text="Discount",fg="blue",bg=None,font=("Constantia",12)).place(x=15,y=290)
e5=ttk.Entry(win,textvariable=discount,state="readonly").place(x=150,y=290)
l6=tkinter.Label(win,text="Payable Amount",fg="blue",bg=None,font=("Constantia",12)).place(x=15,y=330)
e5=ttk.Entry(win,textvariable=pamount,state="readonly").place(x=150,y=330)
b3=ttk.Button(win,text="Receive",command=receive).place(x=150,y=370)
b4=ttk.Button(win,text="reset",width=5,command=reset)
win.mainloop()
