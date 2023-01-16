# tkinter is a modules or a library in python to dovelop window application in python.
# tkinter provide the gui in python.
# pip install pymql

from tkinter import *
from tkinter import ttk
import os
vishnu=Tk()
vishnu.geometry('1000x600')
vishnu.title("Login page")
from tkinter import messagebox
from hotel import HotelManagementSytem




def Login():
    import pymysql as sql
    singh=sql.connect(host='localhost',user='root',password='Noida37@',db='school')
    cur=singh.cursor()
    cur.execute("select * from ranu where name=%s and lastname=%s",(e1.get(),e2.get()))
    row=cur.fetchone()
    
    if row==None:
        messagebox.showerror("Error","Invalid User Name And Password")
    
    else:
        vishnu.destroy()
        os.system("python hotel.py")
    
    

l=Label(vishnu,text='Hotel Management Login',bg='green',fg='white',font=('Arial 25 bold'))
l.place(x=350,y=60)

l2=Label(vishnu,text='User Name',bg='green',fg='white',font=('Arial 20 bold'))
l2.place(x=300,y=200)

e1=Entry(vishnu,font=('arial 20 bold'))
e1.place(x=450,y=200)


l3=Label(vishnu,text='password',bg='green',fg='white',font=('Arial 20 bold'))
l3.place(x=300,y=300)


e2=Entry(vishnu,font=('arial 20 bold'),show="*")
e2.place(x=450,y=300)

b1=Button(vishnu,text='Login',font=('arial 15 bold'),fg='red',command=Login)
b1.place(x=500,y=400)

vishnu.config(bg='pink')



vishnu.mainloop()
