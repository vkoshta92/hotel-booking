from tkinter import *
from PIL import Image,ImageTk
# for tyle entry
from tkinter import ttk

class Cust_Win:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        # where to start and where to end
        self.root.geometry("1295x550+230+220")

        
        # ........title
        lb1_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("arial",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lb1_title.place(x=0,y=0, width=1295,height=50)

        # .........................logo
        
        img2=Image.open(r"G:\coding\data\My Data\python\project\hotel booking\images\logohotel.png")
        img2=img2.resize((100,40),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

        # LABELFRAME
        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Cuustomer Details",font=("arial",12,"bold"),padx=2)
        labelframeleft.place(x=5,y=50,width=425,height=490)
        
        # labels and entrys(cust ref)
        lb1_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
        lb1_cust_ref.grid(row=0, column=0,sticky=W)
        
        enty_ref=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        enty_ref.grid(row=0,column=1)
        
        # cust name
        cname=Label(labelframeleft,text="Customer Name:",font=("arial",12,"bold"),padx=2,pady=6)
        cname.grid(row=1, column=0,sticky=W)
        
        txtcname=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtcname.grid(row=1,column=1)
        
        # mother name
        lb1mname=Label(labelframeleft,text="Mother Name:",font=("arial",12,"bold"),padx=2,pady=6)
        lb1mname.grid(row=2, column=0,sticky=W)
        
        txtmname=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtmname.grid(row=2,column=1)
        
        # gender combobox
        label_gender=Label(labelframeleft,text="Gender:",font=("arial",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=3, column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender["value"]=("Male","Female","Other")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        # postcode
        lb1PostCode=Label(labelframeleft,text="PostCode:",font=("arial",12,"bold"),padx=2,pady=6)
        lb1PostCode.grid(row=4, column=0,sticky=W)
        
        txtPostCode=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtPostCode.grid(row=4,column=1)
        
        
        # mobilenumber
        lb1Mobile=Label(labelframeleft,text="Mobile:",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Mobile.grid(row=5, column=0,sticky=W)
        
        txtMobile=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtMobile.grid(row=5,column=1)
        
        # email
        lb1Email=Label(labelframeleft,text="Email:",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Email.grid(row=6, column=0,sticky=W)
        
        txtEmail=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtEmail.grid(row=6,column=1)
        
        # nationality
        lb1Nationality=Label(labelframeleft,text="Nationality",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Nationality.grid(row=7, column=0,sticky=W)
        
        combo_Nationality=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_Nationality["value"]=("Indian","American","British")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7,column=1)
        
        # idproof type combobox
        lb1IdProof=Label(labelframeleft,text="Id Proof type:",font=("arial",12,"bold"),padx=2,pady=6)
        lb1IdProof.grid(row=8, column=0,sticky=W)
        
        combo_id=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),width=27,state="readonly")
        combo_id["value"]=("Adhar Card","Driving Liecence","Passport")
        combo_id.current(0)
        combo_id.grid(row=8,column=1)

        
        # id number
        lb1IdNumber=Label(labelframeleft,text="Id Number:",font=("arial",12,"bold"),padx=2,pady=6)
        lb1IdNumber.grid(row=9, column=0,sticky=W)
        
        txtIdNumber=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtIdNumber.grid(row=9,column=1)
        
        # address
        lb1Address=Label(labelframeleft,text="Address:",font=("arial",12,"bold"),padx=2,pady=6)
        lb1Address.grid(row=10, column=0,sticky=W)
        
        txtAddress=ttk.Entry(labelframeleft,width=29,font=("arial",13,"bold"))
        txtAddress.grid(row=10,column=1)
        
        
        # .....buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=381,width=412,height=30)
        
        # frame ke andr kr rhe h usliye grid use kiya hai.
        btnAdd=Button(btn_frame,text="Add",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
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
        
        #  .........table frame
        
        table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("arial",12,"bold"),padx=2)
        table_Frame.place(x=435,y=50,width=850,height=490)
        
        # search system
        lb1SearchBy=Label(table_Frame,text="Search By:",font=("arial",12,"bold"),bg="red",fg="white")
        lb1SearchBy.grid(row=0, column=0,sticky=W,padx=2)
        
        combo_Search=ttk.Combobox(table_Frame,font=("arial",12,"bold"),width=15,state="readonly")
        combo_Search["value"]=("Mobile No","Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0,column=1,padx=2)
        
        txtSearch=ttk.Entry(table_Frame,width=24,font=("arial",13,"bold"))
        txtSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(table_Frame,text="Serach",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowall=Button(table_Frame,text="Show All",font=("arial",12,"bold"),bg="black",fg="gold",width=9)
        btnShowall.grid(row=0,column=4,padx=1)
        
        
        # ................sShow data tabledetails
        details_table=Frame(table_Frame,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=840,height=350)
        
        # for scroll bar
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        
        # make table
        self.Cust_Details_Table=ttk.Treeview(details_table,columns=("ref","name","mother","gender","post","mobile","email","nationality","idproof","idnumber","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)
        
        # show coloum name
        self.Cust_Details_Table.heading("ref",text="Refer No")
        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("mother",text="Mother Name")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("post",text="PostCode")
        self.Cust_Details_Table.heading("mobile",text="Mobile")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("nationality",text="Nationality")
        self.Cust_Details_Table.heading("idproof",text="Id Proof")
        self.Cust_Details_Table.heading("idnumber",text="Id Number")
        self.Cust_Details_Table.heading("address",text="Address")
        
        self.Cust_Details_Table["show"]="headings"
        
        self.Cust_Details_Table.column("ref",width=100)
        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("mother",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("post",width=100)
        self.Cust_Details_Table.column("mobile",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("nationality",width=100)
        self.Cust_Details_Table.column("idproof",width=100)
        self.Cust_Details_Table.column("idnumber",width=100)
        self.Cust_Details_Table.column("address",width=100)
        
        
        self.Cust_Details_Table.pack(fill=BOTH,expand=1)
        







if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop()