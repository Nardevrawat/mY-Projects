import tkinter
from tkinter import *
from tkinter.ttk import *
import time
import os
def showProgress():
                global val
                while val<100:
                        val+=20
                        mypb['value']=val
                        mypb.update()
                        if val<=100:
                                perc.set("Returning..."+str(val)+" % complete")
                        time.sleep(.1)
                mypb['value']=0
                val=0
                mywin.destroy()
                os.system("python ••••••Main••••••.py")
	
mywin = Tk()
val=0
perc=StringVar()
mywin.overrideredirect(1) # To hide title bar of tkinter window
mywin.geometry("400x130+300+300")
mywin.config(bg='white')
mypb = Progressbar(mywin,orient=HORIZONTAL,length=300,value=val)
mypb.pack(side=TOP,pady=20)
#Button(mywin,text="close",command=mywin.quit).pack(side=BOTTOM)
lb1 = tkinter.Label(mywin,textvariable=perc,text='.')
lb1.config(font=('arial',15,'bold'),bg='white',fg='black')
lb1.pack(side=TOP)
#Button(mywin,text="start",command=showProgress).pack(side=BOTTOM)
showProgress()
mywin.mainloop()
