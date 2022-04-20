# GUI - Event
from tkinter import *
#for tab data
from prettytable import PrettyTable
x = PrettyTable()
#object on class Tk
window = Tk()
window.title("Welcome to GUI Python")
window.geometry('650x200')
#declaring controls
sr=Label(window,width=20, text="Enter RegNo", bg="yellow")
txt1 = Entry(window,width=20)
#placing controls, using grid
sr.grid(column=0, row=0)
txt1.grid(column=1, row=0)
#function to establish db connection and db operations
def clicked():
    import mysql.connector as sql
    import pandas as pd
    db_connection = sql.connect(host='localhost', database=' college_db', user='root', password='')
    db_cursor = db_connection.cursor()
    t1=txt1.get()
    #with column heads
    ch = pd.read_sql("SELECT * FROM student_info WHERE  Student_RegNo like '%{}%' ".format(t1) , con=db_connection)
    #ch3= pd.read_sql("select  fee_master.totfee-sum(fee_det.feeamt) as 'Bal' from fee_master INNER JOIN fee_det ON fee_master.regno = fee_det.regno where fee_master.regno='1001' GROUP BY fee_det.regno", con=db_connection)
    db_connection.commit()
    lb=Label(window, text=ch, width=50).grid(column=3, row=0)
    #x.field_names = ["RegNum", "Name", "Course", "Academic Year"]
    #print(ch)
btn = Button(window, text="Search Record",width=20,bg="blue",fg="white", command=clicked)
btn.grid(column=1, row=3)
#infinite loop to run application,
#wait for an event to occur and process event as long as win is not closed.
window.mainloop()
#print(ch)
