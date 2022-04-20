from tkinter import*
from prettytable import PrettyTable
x=PrettyTable()
window=Tk()
window.title('Library Details')
window.geometry('650x200')

sr=Label(window,width=20,text='Enter Book ID',bg='yellow')
txt1=Entry(window,width=20)
sr.grid(column=0,row=0)
txt1.grid(column=1,row=0)

def clicked():
    import mysql.connector as sql
    import pandas as pd
    db_connection=sql.connect(host='localhost',database='college_db',user='root',password='')
    db_cursor=db_connection.cursor()
    t1=txt1.get()

    ch=pd.read_sql('SELECT * FROM library_details WHERE Book_ID={}'.format(t1),con=db_connection)
    db_connection.commit()
    lb=Label(window,text=ch,width=50).grid(column=3,row=0)

btn=Button(window,text='Search Record',width=20,bg='blue',fg='white',command=clicked)
btn.grid(column=1,row=3)

window.mainloop()
