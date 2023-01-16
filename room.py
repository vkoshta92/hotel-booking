from tkinter import *
from PIL import Image,ImageTk
# for tyle entry
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox


class Roombooking:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        # where to start and where to end
        self.root.geometry("1295x550+230+220")
        
        # ...............make variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()

        
        
         
        # ........title
        lb1_title=Label(self.root,text="ROOM BOOKING DETAILS",font=("arial",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_title.place(x=0,y=0, width=1295,height=50)

        # .........................logo
        
        img2=Image.open(r"G:\coding\data\My Data\python\project\hotel booking\images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # LABELFRAME
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Romm Booking Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        
        # labels and entrys
        # customer Contact
        lb1_cust_contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
        lb1_cust_contact.grid(row=0, column=0,sticky=W)
        
        enty_contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
        enty_contact.grid(row=0,column=1,sticky=W)
        
        # fetch data button
        btnFetchData=Button(labelframeleft,command=self.Fetch_contact,text="Fetch Data",font=("arial",8,"bold"),bg="black",fg="gold",width=8)
        btnFetchData.place(x=347,y=4)
        
        # check_in Date
        
        check_in_date=Label(labelframeleft,text="check_in Date",font=("arial",12,"bold"),padx=2,pady=6)
        check_in_date.grid(row=1, column=0,sticky=W)
        
        txtcheck_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
        txtcheck_in_date.grid(row=1,column=1)
        
        # check_out Date
        
        lb1_Check_out=Label(labelframeleft,text="check_out Date",font=("arial",12,"bold"),padx=2,pady=6)
        lb1_Check_out.grid(row=2, column=0,sticky=W)
        
        txt_Check_out=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
        txt_Check_out.grid(row=2,column=1)
        
        # Room Type
        label_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        label_RoomType.grid(row=3, column=0,sticky=W)
        
        combo_RoomType=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
        combo_RoomType["value"]=("Single","Double","Luxary")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3,column=1)
        
        # Avaible Rooms
        lb1Room=Label(labelframeleft,text="Avaible Rooms",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Room.grid(row=4, column=0,sticky=W)
        
        textRoomAvailable=ttk.Entry(labelframeleft,textvariable=self.var_roomavailable,width=29,font=("arial",13,"bold"))
        textRoomAvailable.grid(row=4,column=1)
        
        
        # Meal
        lb1Meal=Label(labelframeleft,text="Meal",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Meal.grid(row=5, column=0,sticky=W)
        
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_meal,width=29,font=("arial",13,"bold"))
        txtMeal.grid(row=5,column=1)
        
        # No of Days
        lb1NoOfDays=Label(labelframeleft,text="No of Days",font=("arial",12,"bold"),padx=2,pady=6)
        lb1NoOfDays.grid(row=6, column=0,sticky=W)
        
        txtNoOfDays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
        txtNoOfDays.grid(row=6,column=1)
        
        
        # paid tax
        lb1Meal=Label(labelframeleft,text="paid tax",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Meal.grid(row=7, column=0,sticky=W)
        
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_paidtax,width=29,font=("arial",13,"bold"))
        txtMeal.grid(row=7,column=1)
        
        # Sub Total
        lb1Meal=Label(labelframeleft,text="Sub Total",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Meal.grid(row=8, column=0,sticky=W)
        
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_actualtotal,width=29,font=("arial",13,"bold"))
        txtMeal.grid(row=8,column=1)
        
        # Total Cost
        lb1Meal=Label(labelframeleft,text="Total Cost",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Meal.grid(row=9, column=0,sticky=W)
        
        txtMeal=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
        txtMeal.grid(row=9,column=1)
        
        # bill button
        btnBill=Button(labelframeleft,text="Bill",font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnBill.grid(row=10,column=0,padx=1,sticky=W)
        
        
        
        # .....buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=381,width=412,height=30)
        
        # frame ke andr kr rhe h isliye grid use kiya hai.
        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnAdd.grid(row=0,column=0,padx=1)
        
        
        # button2
        btnUpdate=Button(btn_frame,text="Update",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        # button 3
        btndelete=Button(btn_frame,text="Delete",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btndelete.grid(row=0,column=3,padx=1)
        
        # button 4
        btnReset=Button(btn_frame,text="Reset",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnReset.grid(row=0,column=4,padx=1)
        
        # ......... right side image
        img3=Image.open(r"G:\coding\data\My Data\python\project\hotel booking\images\bed.jpg")
        img3=img3.resize((520,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
        lblimg.place(x=760,y=55,width=520,height=200)
        
        
        
        
        #  table frame serach system
        table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        table_Frame.place(x=435,y=280,width=850,height=260)
        
        lb1SearchBy=Label(table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lb1SearchBy.grid(row=0, column=0,sticky=W,padx=2)
        
        
        self.search_var=StringVar()
        combo_Search=ttk.Combobox(table_Frame,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Contact","Room")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        
        self.txt_search=StringVar()
        txtSearch=ttk.Entry(table_Frame,textvariable=self.txt_search,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(table_Frame,text="Serach",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowall=Button(table_Frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowall.grid(row=0,column=4,padx=1)
        
         
        # ................Show data tabledetails
        details_table=Frame(table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=180)
        
        # for scroll bar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        
        # make table
        self.room_table=ttk.Treeview(details_table,columns=("contact","checkin","checkout","roomtype","roomavailable","meal","noOfdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)
        
        # show coloum name
        self.room_table.heading("contact",text="Contact")
        self.room_table.heading("checkin",text="Check-in")
        self.room_table.heading("checkout",text="Check-out")
        self.room_table.heading("roomtype",text="Room Type")
        self.room_table.heading("roomavailable",text="Room No")
        self.room_table.heading("meal",text="Meal")
        self.room_table.heading("noOfdays",text="NoOfDays")
        
        
        self.room_table["show"]="headings"
        
        self.room_table.column("contact",width=100)
        self.room_table.column("checkin",width=100)
        self.room_table.column("checkout",width=100)
        self.room_table.column("roomtype",width=100)
        self.room_table.column("roomavailable",width=100)
        self.room_table.column("meal",width=100)
        self.room_table.column("noOfdays",width=100)
        self.room_table.pack(fill=BOTH,expand=1)
        
        
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,)",(
                                                    self.var_contact.get(),
                                                    self.var_checkin.get(),
                                                    self.var_checkout.get(),
                                                    self.var_roomtype.get(),
                                                    self.var_roomavailable.get(),
                                                    self.var_meal.get(),
                                                    self.var_noofdays.get()
                                                        
                                                 ))
                conn.commit()
                # self.fetch_data()
                conn.close()
                    
                # parent se message box usi wndow par show hoga, khi bhi nhi hoga.
                messagebox.showinfo("Success","customer has been added",parent=self.root) 
            except Exception as es:
                # f string
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)
        
    # for fetch sql data
    
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
        my_cursor=conn.cursor()
       
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()   
        
        
        
        # all data fetch
    def Fetch_contact(self):
        if self.var_contact.get()=="":
            # parent isliye  use hota h kyokiusi page me show ho new pag par na jae.
            messagebox.showerror("Error","Please enter Contact Number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
            my_cursor=conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=450,y=55,width=300,height=180)
                
                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl.place(x=90,y=0)
            
            # gender database
                conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)
                    
                lbl2=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl2.place(x=90,y=30)
                
            # email database
                conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblemail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblemail.place(x=0,y=60)
                    
                lbl3=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl3.place(x=90,y=60)
                
            # nationality
                conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
                my_cursor=conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lblnationality=Label(showDataframe,text="Nationality:",font=("arial",12,"bold"))
                lblnationality.place(x=0,y=90)
                    
                lbl4=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl4.place(x=90,y=90)
                
            # address
                conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                row=my_cursor.fetchone()
                
                lbladdress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lbladdress.place(x=0,y=120)
                    
                lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
                lbl5.place(x=90,y=120)
            
            # # idnumber
            #     conn=mysql.connector.connect(host="localhost",username="root",password="Noida37@",database="management")
            #     my_cursor=conn.cursor()
            #     query=("select Idnumber from customer where Mobile=%s")
            #     value=(self.var_contact.get(),)
            #     my_cursor.execute(query,value)
            #     row=my_cursor.fetchone()
                
            #     lbladdress=Label(showDataframe,text="Idnumber:",font=("arial",12,"bold"))
            #     lbladdress.place(x=0,y=150)
                    
            #     lbl5=Label(showDataframe,text=row,font=("arial",12,"bold"))
            #     lbl5.place(x=90,y=150)
        
        
        
        
        
        
if __name__=="__main__":
    root=Tk()
    obj=Roombooking(root)
    root.mainloop()