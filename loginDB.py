from tkinter import *
import tkinter.messagebox
import mysql.connector


#connecting to the database
connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="",database="college_db")
cursordb = connectiondb.cursor()


def login():
    global root2
    root2 = Toplevel(root)
    root2.title("Account Login")
    root2.geometry("450x300")
    root2.config(bg="white")

    global username_verification
    global password_verification
    Label(root2, text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",width=300).pack()
    username_verification = StringVar()
    password_verification = StringVar()
    Label(root2, text="").pack()
    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=username_verification).pack()
    Label(root2, text="").pack()
    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
    Entry(root2, textvariable=password_verification, show="*").pack()
    Label(root2, text="").pack()
    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
    Label(root2, text="")

def logged_destroy():
    logged_message.destroy()
    root2.destroy()

def failed_destroy():
    failed_message.destroy()

def logged():
    global logged_message
    logged_message = Toplevel(root2)
    
    logged_message.title("Welcome")
    logged_message.geometry("600x600")
    root2.geometry("+300+200")#for center alignment
    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
    Label(logged_message, text="").pack()
    Button(logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()
    Button(logged_message, text="Exit Application", bg="red", fg='white', relief="groove", font=('arial', 12, 'bold'), command=root.destroy).pack()
    root.withdraw()#to hide window after login
    root2.withdraw()

def failed():
    global failed_message
    failed_message = Toplevel(root2)
    failed_message.title("Invalid Message")
    failed_message.geometry("500x100")
    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
    Label(failed_message, text="").pack()
    Button(failed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()


def login_verification():
    user_verification = username_verification.get()
    pass_verification = password_verification.get()
    sql = "select * from user_details where user = %s and passw = %s"
    cursordb.execute(sql,[(user_verification),(pass_verification)])
    results = cursordb.fetchall()
    if results:
        for i in results:
            logged()
            import college_det as cd
            break
    else:
        failed()

def Exit():
    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return

def main_display():
    global root
    root = Tk()
    root.config(bg="white")
    root.title("Application")
    root.geometry("500x300")
    root.geometry("+300+200")#for center alignment
    Label(root,text='Welcome to the system', font=('arial', 20, 'bold'), fg="blue",
                   bg="orange",width=300).pack()
    Label(root,text="").pack()
    Button(root,text='Log In', height="1",width="20",font=('arial', 12, 'bold'),  fg="white",
                   bg="green",command=login).pack()
    Label(root,text="").pack()
    Button(root,text='Exit', height="1",width="20",  font=('arial', 12, 'bold'),  fg="white",
                   bg="green",command=Exit).pack()
    Label(root,text="").pack()
    
   

main_display()
root.mainloop()
