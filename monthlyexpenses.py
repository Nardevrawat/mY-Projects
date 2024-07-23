from tkinter.ttk import *
from tkinter import*
import tkinter
import os
from tkinter import messagebox
import mysql.connector as mycon
cn = mycon.connect(host='localhost',user='root',password="admin",database='rmsazharansari')
cur = cn.cursor()
