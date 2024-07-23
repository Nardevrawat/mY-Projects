import tkinter
from tkinter import *
from tkinter.ttk import *
import time
from tkinter import messagebox
import os
import winsound
winsound.PlaySound(r'Data\pysound\operationsucessful.wav',winsound.SND_ALIAS | winsound.SND_ASYNC)
def showProgress():
                global val
                while val<100:
                        val+=15
                        mypb['value']=val
                        mypb.update()
                        if val<=100:
                                perc.set("Deleting Data..."+str(val)+" % complete")
                        time.sleep(.1)
                mypb['value']=0
                val=0
                messagebox.showinfo("RMS","Data Deleted Sucessfully")
                os.system("python employeeinterface.py")
	
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
