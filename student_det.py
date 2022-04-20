import tkinter as tk
from tkinter import*
w=tk.Tk()
w.title("College Records")
w.geometry("300x250")
l1=Label(w,text="Student details",font="sans 14",fg="red",bg="yellow").grid(row=0,column=0,columnspan=4)
our_canvas=Canvas(w,width=500,height=5,bg="blue").grid(row=1,column=0,columnspan=4)

import mysql.connector as sql
db_connection=sql.connect(host='localhost',database='college_db',user='root',password='')                                          
db_cursor=db_connection.cursor()
db_cursor.execute('SELECT * FROM student_info')
r_set=db_cursor.fetchall()

i=2
for student in r_set:
    for j in range(len(student)):
        e=Entry(w,width=10,fg='blue')
        e.grid(row=i,column=j)
        e.insert(END,student[j])
    i=i+1
    
w.mainloop()
