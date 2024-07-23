from tkinter.ttk import *
from tkinter import*
import tkinter
import os
import mysql.connector as mycon
from tkinter import filedialog
from tkinter import messagebox
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
def importt():
    filename=filedialog.askopenfilename(initialdir="/Desktop",title="Select File To Import ",filetype=(("azhar files","*.azhar"),("all files","*")))
    stri=""
    for line in open(filename):
        print("hello")
        if len(line)==0 or line[0]=="-" or line[0]=="/":
            pass
        else:
            if line[len(line)-2]!=';':
                stri+=line
            else:
                stri+=line
                cur.execute(stri)
                stri=""

def export():
    ans=messagebox.askquestion("RMS","Are You Sure to Export Database")
    if ans=="yes":
        os.system("mysqldump rmsazharansari -uroot -padmin  > RMS.azhar")
        messagebox.showinfo("RMS","Sucessfully Export to Program Directory \nFile name - RMS.azhar")
def aboutt():
    os.system("about.png")
win=Tk()
win.title("Resturant Management System")
win.config(bg="white")
win.geometry("220x180+400+150")
win.iconbitmap(r"Data\pyimage\logo.ico")
importimage=PhotoImage(file=r"Data\pyimage\import.png")
exportimage=PhotoImage(file=r"Data\pyimage\export.png")
aboutimage=PhotoImage(file=r"Data\pyimage\abt.png")
l1=tkinter.Label(win,text="Setting",fg="red",bg="white",font=("Constantia",13)).pack()
l2=tkinter.Label(win,text="Import Data",fg="blue",bg="white",font=("Georgia",10)).place(x=10,y=30)
b1=ttk.Button(win,image=importimage,command=importt).place(x=30,y=50)
l3=tkinter.Label(win,text="Export Data",fg="blue",bg="white",font=("Georgia",10)).place(x=125,y=30)
b2=ttk.Button(win,image=exportimage,command=export).place(x=140,y=50)
l4=tkinter.Label(win,text="About",fg="blue",bg="white",font=("Georgia",10)).place(x=85,y=90)
b3=ttk.Button(win,image=aboutimage,command=aboutt).place(x=87,y=110)

win.mainloop()
