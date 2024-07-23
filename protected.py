from tkinter.ttk import *
from tkinter import *
import os
import tkinter
import winsound
import time
ret=0
winsound.PlaySound(r'Data\pysound\protected.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
def tick():
    global ret
    if ret==30:
        win.destroy()
        os.system("python returning.py")
    else:
        ret+=1
        cur_time=time.strftime("%H:%M:%S")
        clock.config(text=cur_time)
        clock.after(1000,tick)
win=Tk()
win.geometry("225x225+400+200")
win.overrideredirect(1)
p1=PhotoImage(file=r"Data\pyimage\protectedd.png")
Label(win,image=p1).pack()
t1=tkinter.Label(win,text="Protected",fg="red",bg="white",font=("Consolas",15))
t1.place(x=60,y=30)
clock = Label(win,font=('times',100,'bold'),bg='white',fg='black')
clock.pack()
tick()
win.mainloop()
