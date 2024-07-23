from tkinter.ttk import *
import tkinter
from tkinter import *
import os
import mysql.connector as mycon
from tkinter import messagebox
import hashlib
import winsound
count=1
chance=2
cn = mycon.connect(host='localhost',user='root',password="admin")
cur = cn.cursor()
cur.execute("create database if not exists rmsazharansari")
cur.execute("use rmsazharansari")
cur.execute("create table if not exists login (user_id varchar(2000),password varchar(2000))")
cur.execute("insert into login values ('AzharRMS',md5('passcode'))")
cur.execute("create table if not exists loginhistory (user_id varchar(2000),Details varchar(2000))")
cn.commit()
cur.execute("select*from login")
c=cur.fetchone()

def login():
    global count
    global chance
    global c,cp,u
    u=userr.get()
    p=pasw.get()
    result = hashlib.md5(p.encode())
    cp=result.hexdigest()
    if u=="":
        messagebox.showinfo("RMS","Please Enter User ID")
    elif p=="":
        messagebox.showinfo("RMS","Please Enter Password")
    elif u==c[0] and cp==c[1]:
        winsound.PlaySound(r'Data\pysound\loginsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
        messagebox.showinfo("RMS","|  Login Sucessful  |")
        win.destroy()
        os.system("python loading.py")
    else:
        if count<3:
            winsound.PlaySound(r'Data\pysound\accessdenied.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
            messagebox.showinfo("RMS","|  Acess Denied |\n  "+str(chance)+"Attempts Left")
            count+=1
            chance-=1
        elif count==3:
            win.destroy()
            os.system("python protected.py")
def qui():
    win.destroy()
def sewin():
    os.system("python settingmain.py")
win=Tk()
win.title('Resturant Management - User Authentication')
win.geometry("380x270+300+200")
win.config(bg="white")
win.iconbitmap(r"Data\pyimage\logo.ico")
win.resizable(False,False)
l1=tkinter.Label(win,text="Resturant Management System",fg="red",bg="white",font=("Segoe Print",14))
l1.pack()
user=PhotoImage(file=r"Data\pyimage\user.png")
userr=StringVar()
pasw=StringVar()
l2=tkinter.Label(win,image=user)
l2.pack()
l3=tkinter.Label(win,text="User ID",fg="blue",bg="white",font=("Cambria",12))
l3.place(x=60,y=160)
l4=tkinter.Label(win,text="Password",fg="blue",bg="white",font=("Cambria",12))
l4.place(x=50,y=190)
e1=tkinter.Entry(win,textvariable=userr,fg="white",bg="black")
e1.place(x=150,y=162)
e2=tkinter.Entry(win,textvariable=pasw,show="•",fg="white",bg="black")
e2.place(x=150,y=192)
sett=PhotoImage(file=r"Data\pyimage\sett.png")
b1=ttk.Button(win,image=sett,command=sewin)
b1.place(x=340,y=140)
ex=PhotoImage(file=r"Data\pyimage\exet.png")
b2=ttk.Button(win,image=ex,command=qui)
b2.place(x=340,y=180)
log=PhotoImage(file=r"Data\pyimage\log.png")
b3=ttk.Button(win,image=log,command=login)
b3.place(x=155,y=220)
win.mainloop()
