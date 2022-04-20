import tkinter as tk
from tkinter import messagebox
from tkinter import*
import os
import sys
root=tk.Tk()
root.geometry('450x600+0+0')
root.title('College Details')
root.configure(bg='khaki')

lb=tk.Label(root,text='College Information',font='sans 14',bg='green',fg='white').pack(fill='both')
lb3=tk.Label(root,text='',font='sans 14',bg='#f0f288',fg='blue').pack(fill='both')

def std():
    import Std_regno as srn
b1=tk.Button(root,text='Student Details',command=std,bg='cyan',fg='black',font='sans 14',height=2,width=25).pack()

def fac():
    import search_fac_det as sfd
b1=tk.Button(root,text='Faculty Details',command=fac,bg='pink',fg='black',font='sans 14',height=2,width=25).pack()

def lib():
    import search_lib_det as sld
b1=tk.Button(root,text='Library Details',command=lib,bg='yellow',fg='black',font='sans 14',height=2,width=25).pack()

b3=tk.Button(root,text='Close Application',command=root.destroy,bg='red',fg='white',font='sans 14',height=2,width=25).pack()
lb2=tk.Label(root,text='THANK YOU',font='sans 14',bg='green',fg='white').pack(fill='both',side=tk.BOTTOM)

root.mainloop()
