from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
import mysql.connector
from tkinter import messagebox


class Employee:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("EMPLOYEE MANAGEMENT SYSTEM")

# Variables
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_designition=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        


        lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg="darkblue",bg="white")
        lbl_title.place(x=0,y=0,width=1530,height=50)

        img_logo=Image.open(r"college_images\emplogo.png")
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photoimg_logo=ImageTk.PhotoImage(img_logo)

        self.logo=Label(self.root,image=self.photoimg_logo)
        self.logo.place(x=270,y=0,width=50,height=50)

        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=50,width=1530,height=160)

   # 1st
        img=Image.open(r"college_images\emp5.jpg")
        img=img.resize((540,160),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        self.btn_1=Label(img_frame,image=self.photoimg,)
        self.btn_1.place(x=0,y=0,width=540,height=160)

    # 2st
        img_2=Image.open(r"college_images\emp2.png")
        img_2=img_2.resize((540,160),Image.ANTIALIAS)
        self.photoimg_2=ImageTk.PhotoImage(img_2)

        self.btn_2=Label(img_frame,image=self.photoimg_2)
        self.btn_2.place(x=540,y=0,width=540,height=160)

    # 3st
        img_3=Image.open(r"college_images\emp4.jpg")
        img_3=img_3.resize((540,160),Image.ANTIALIAS)
        self.photoimg_3=ImageTk.PhotoImage(img_3)

        self.btn_3=Label(img_frame,image=self.photoimg_3)
        self.btn_3.place(x=1000,y=0,width=540,height=160)

    # bg image

        img_4=Image.open(r"college_images\university.jpg")
        img_4=img_4.resize((1530,580),Image.ANTIALIAS)
        self.photoimg_4=ImageTk.PhotoImage(img_4)

        bg_lbl=Label(self.root,image=self.photoimg_4,bd=2,relief=RIDGE)
        bg_lbl.place(x=0,y=210,width=1530,height=580)


         # manage Frame
        Manage_frame=Frame(bg_lbl,bd=2,relief=RIDGE,bg="white")
        Manage_frame.place(x=15,y=10,width=1500,height=560)


        # left Frame
        DataLeftFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Employee Information",font=("times new roman",11,"bold"),fg="red",bg="white")
        DataLeftFrame.place(x=10,y=10,width=1480,height=270)
        
       
        # Employee class LabelFrame Information
        emp_lbl_frame=Frame(DataLeftFrame,bd=4,relief=RIDGE,padx=2,bg="white")
        emp_lbl_frame.place(x=0,y=10,width=1470,height=235)

        # labels entry
        # ID
        # department
        lbl_dep=Label(emp_lbl_frame,text="Department",font=("arial",11,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)

        combo_dep=ttk.Combobox(emp_lbl_frame,textvariable=self.var_dep,font=("arial",12,"bold"),width=17,state="readonly")
        combo_dep["value"]=("Select Department","HR","Software Engineer","Infrastracture","Manager")
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        
        # Name
        lbl_Name=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,sticky=W,padx=2,pady=7)

        txt_name=ttk.Entry(emp_lbl_frame,textvariable=self.var_name,width=22,font=("arial",11,"bold"))
        txt_name.grid(row=0,column=3,padx=2,pady=7)

        # # lbl_Designition
        lbl_Designition=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Designition:",bg="white")
        lbl_Designition.grid(row=1,column=0,sticky=W,padx=2,pady=7)

        txt_Designition=ttk.Entry(emp_lbl_frame,textvariable=self.var_designition,width=22,font=("arial",11,"bold"))
        txt_Designition.grid(row=1,column=1,sticky=W,padx=2,pady=7)

        # Email
        lbl_email=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Email:",bg="white")
        lbl_email.grid(row=1,column=2,sticky=W,padx=2,pady=7)

        txt_email=ttk.Entry(emp_lbl_frame,textvariable=self.var_email,width=22,font=("arial",11,"bold"))
        txt_email.grid(row=1,column=3,padx=2,pady=7)

        # Address
        lbl_adderss=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Address:",bg="white")
        lbl_adderss.grid(row=2,column=0,sticky=W,padx=2,pady=7)

        txt_adderss=ttk.Entry(emp_lbl_frame,textvariable=self.var_address,width=22,font=("arial",11,"bold"))
        txt_adderss.grid(row=2,column=1,padx=2,pady=7)

        # Married
        lbl_merried_status=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Married Status:",bg="white")
        lbl_merried_status.grid(row=2,column=2,sticky=W,padx=2,pady=7)

        com_txt_married=ttk.Combobox(emp_lbl_frame,textvariable=self.var_married,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_married['value']=("Married","Unmarried")
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,sticky=W,padx=2,pady=7)

        # Dob
        lbl_dob=Label(emp_lbl_frame,font=("arial",12,"bold"),text="DOB:",bg="white")
        lbl_dob.grid(row=3,column=0,sticky=W,padx=2,pady=7)

        txt_dob=ttk.Entry(emp_lbl_frame,textvariable=self.var_dob,width=22,font=("arial",11,"bold"))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)

        # Doj
        lbl_doj=Label(emp_lbl_frame,font=("arial",12,"bold"),text="DOJ:",bg="white")
        lbl_doj.grid(row=3,column=2,sticky=W,padx=2,pady=7)

        txt_doj=ttk.Entry(emp_lbl_frame,textvariable=self.var_doj,width=22,font=("arial",11,"bold"))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)

         # Id Proof
        # lbl_id_proof=Label(emp_lbl_frame,font=("arial",12,"bold"),text="ID Proof:",bg="white")
        # lbl_id_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        com_txt_proof=ttk.Combobox(emp_lbl_frame,textvariable=self.var_idproofcomb,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_proof['value']=("Select ID Proof","PAN CARD","ADHAR CARD","DRIVING LICENCE")
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,sticky=W,padx=2,pady=7)

        txt_proof=ttk.Entry(emp_lbl_frame,textvariable=self.var_idproof,width=22,font=("arial",11,"bold"))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)


        # gender
        lbl_gender=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Gender:",bg="white")
        lbl_gender.grid(row=4,column=2,sticky=W,padx=2,pady=7)

        com_txt_gender=ttk.Combobox(emp_lbl_frame,textvariable=self.var_gender,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_gender['value']=("Male","Female","Other")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,sticky=W,padx=2,pady=7)
       
        # phone
        lbl_phone=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Phone No:",bg="white")
        lbl_phone.grid(row=0,column=4,sticky=W,padx=2,pady=7)

        txt_phone=ttk.Entry(emp_lbl_frame,textvariable=self.var_phone,width=22,font=("arial",11,"bold"))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)

         # # country
        lbl_country=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Country:",bg="white")
        lbl_country.grid(row=1,column=4,sticky=W,padx=2,pady=7)

        txt_country=ttk.Entry(emp_lbl_frame,textvariable=self.var_country,width=22,font=("arial",11,"bold"))
        txt_country.grid(row=1,column=5,padx=2,pady=7)

        # # CTC
        lbl_ctc=Label(emp_lbl_frame,font=("arial",12,"bold"),text="Salary(CTC):",bg="white")
        lbl_ctc.grid(row=2,column=4,sticky=W,padx=2,pady=7)

        txt_ctc=ttk.Entry(emp_lbl_frame,textvariable=self.var_salary,width=22,font=("arial",11,"bold"))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)

          # stayhome=Label(emp_lbl_frame,text="STAY HOME STAY SAFE",font=("times new roman",30,"bold"),fg="red",bg="white")
        # stayhome.place(x=780,y=0,width=670,height=30)

        img_logo_mask1=Image.open(r"college_images\emp1.png")
        img_logo_mask1=img_logo_mask1.resize((220,220),Image.ANTIALIAS)
        self.photoimg_logo_mask1=ImageTk.PhotoImage(img_logo_mask1)

        self.logo=Label(emp_lbl_frame,image=self.photoimg_logo_mask1)
        self.logo.place(x=1000,y=0,width=220,height=220)

        
        # Button Frame
        btn_frame=Frame(DataLeftFrame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=1290,y=20,width=170,height=210)

        btn_Add=Button(btn_frame,text="Save",command=self.add_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn_Add.grid(row=0,column=0,padx=1,pady=5)

        btn_update=Button(btn_frame,text="Update",command=self.update_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn_update.grid(row=1,column=0,padx=1,pady=5)

        btn__delete=Button(btn_frame,text="Delete",command=self.delete_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn__delete.grid(row=2,column=0,padx=1,pady=5)

        btn_reset=Button(btn_frame,text="Reset",command=self.reset_data,font=("arial",15,"bold"),width=13,bg="blue",fg="white")
        btn_reset.grid(row=3,column=0,padx=1,pady=5)

        
         # Down Frame
        DataRightFrame=LabelFrame(Manage_frame,bd=4,relief=RIDGE,padx=2,text="Employee Information",font=("times new roman",11,"bold"),fg="darkblue",bg="white")
        DataRightFrame.place(x=10,y=280,width=1480,height=270)

        # Down Frame
        Search_Frame=LabelFrame(DataRightFrame,bd=4,relief=RIDGE,padx=2,text="Search Employee Information",font=("times new roman",11,"bold"),fg="darkblue",bg="white")
        Search_Frame.place(x=0,y=0,width=1470,height=60)

        search_by=Label(Search_Frame,font=("arial",11,"bold"),text="Search By:",fg="white",bg="red")
        search_by.grid(row=0,column=0,sticky=W,padx=5)

        # search
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(Search_Frame,textvariable=self.var_com_search,state="readonly",
                                                        font=("arial",12,"bold"),width=18)
        com_txt_search['value']=("Select Option","Phone","id_proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,sticky=W,padx=5)

        self.var_search=StringVar()
        txt_search=ttk.Entry(Search_Frame,textvariable=self.var_search,width=22,font=("arial",11,"bold"))
        txt_search.grid(row=0,column=2,padx=5)

        btn__search=Button(Search_Frame,command=self.search_data,text="Search",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn__search.grid(row=0,column=3,padx=5)

        btn_ShowAll=Button(Search_Frame,command=self.fetch_data,text="Show All",font=("arial",11,"bold"),width=14,bg="blue",fg="white")
        btn_ShowAll.grid(row=0,column=4,padx=5)

    
       
        # ==============Employee Table and Scroll bar====================
        table_frame=Frame(DataRightFrame,bd=4,relief=RIDGE)
        table_frame.place(x=0,y=60,width=1470,height=170)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        self.employee_table=ttk.Treeview(table_frame,column=("dep","name","degi","email","address","married","dob","doj","idproofcomb","idproof","gender","phone","country","salary",),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        self.employee_table.heading("dep",text="Department")
        self.employee_table.heading("name",text="Name")
        self.employee_table.heading("degi",text="Degignition")
        self.employee_table.heading("email",text="Email")
        self.employee_table.heading("address",text="Address")
        self.employee_table.heading("married",text="Married Status")
        self.employee_table.heading("dob",text="DOB")
        self.employee_table.heading("doj",text="DOJ")
        self.employee_table.heading("idproofcomb",text="ID Type")
        self.employee_table.heading("idproof",text="ID Proof")
        self.employee_table.heading("gender",text="Gender")
        self.employee_table.heading("phone",text="Phone")
        self.employee_table.heading("country",text="Country")
        self.employee_table.heading("salary",text="Salary")

        self.employee_table["show"]="headings"

        self.employee_table.column("dep",width=100)
        self.employee_table.column("name",width=100)
        self.employee_table.column("degi",width=100)
        self.employee_table.column("email",width=100)
        self.employee_table.column("address",width=100)
        self.employee_table.column("married",width=100)
        self.employee_table.column("dob",width=100)
        self.employee_table.column("doj",width=100)
        self.employee_table.column("idproofcomb",width=100)
        self.employee_table.column("idproof",width=100)
        self.employee_table.column("gender",width=100)
        self.employee_table.column("phone",width=100)
        self.employee_table.column("country",width=100)
        self.employee_table.column("salary",width=100)

        
        
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()


    def add_data(self):
      if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_idproof.get()==""):
          messagebox.showerror("Error","All Fields Are required")
      else:
            try:
                conn=mysql.connector.connect(host="localhost",username="amey020",password="1234",database="mydata")
                my_cursur=conn.cursor()
                my_cursur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                            self.var_dep.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_designition.get(),
                                                                                                            self.var_email.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_married.get(),
                                                                                                            self.var_dob.get(),
                                                                                                            self.var_doj.get(),
                                                                                                            self.var_idproofcomb.get(),
                                                                                                            self.var_idproof.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_phone.get(),
                                                                                                            self.var_country.get(),
                                                                                                            self.var_salary.get()
        
                                                                                                   
                                                                                                   ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Employee has been added!",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

     # fetch Function
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="amey020",password="1234",database="mydata")
        my_cursur=conn.cursor()
        my_cursur.execute("select * from employee")
        data=my_cursur.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert("",END,values=i)
            conn.commit()
        conn.close()

      # Get Cursor
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content["values"]

        
        self.var_dep.set(data[0])
        self.var_name.set(data[1])
        self.var_designition.set(data[2])
        self.var_email.set(data[3])
        self.var_address.set(data[4])
        self.var_married.set(data[5])
        self.var_dob.set(data[6])
        self.var_doj.set(data[7])
        self.var_idproofcomb.set(data[8])
        self.var_idproof.set(data[9])
        self.var_gender.set(data[10])
        self.var_phone.set(data[11])
        self.var_country.set(data[12])
        self.var_salary.set(data[13])

    def update_data(self):
        if (self.var_dep.get()=="" or self.var_email.get()=="" or self.var_idproof.get()==""):
            messagebox.showerror("Error","All Fields Are required")
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure update this employee data",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="amey020",password="1234",database="mydata")
                    my_cursur=conn.cursor()
                    my_cursur.execute("update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s",(

                                                                                                                                                                self.var_dep.get(),
                                                                                                                                                                self.var_name.get(),
                                                                                                                                                                self.var_designition.get(),
                                                                                                                                                                self.var_email.get(),
                                                                                                                                                                self.var_address.get(),
                                                                                                                                                                self.var_married.get(),
                                                                                                                                                                self.var_dob.get(),
                                                                                                                                                                self.var_doj.get(),
                                                                                                                                                                self.var_idproofcomb.get(),

                                                                                                                                                                self.var_gender.get(),
                                                                                                                                                                self.var_phone.get(),
                                                                                                                                                                self.var_country.get(),
                                                                                                                                                                self.var_salary.get(),
                                                                                                                                                                self.var_idproof.get()
                                                                                                                                                                
                                                                                                                                                                 ))
                                                                                                                                                                 
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                
                conn.close()

                messagebox.showinfo("Success","Employee successfully updaded",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

 # Delete
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror("Error","All Fields Are required",parent=self.root)
        else:
            try:
                Delete=messagebox.askyesno("Delete","Are sure delete this employee",parent=self.root)
                if Delete>0:
                    conn=mysql.connector.connect(host="localhost",username="amey020",password="1234",database="mydata")
                    my_cursur=conn.cursor()
                    sql="delete from employee where id_proof=%s"
                    value=(self.var_idproof.get(),)
                    my_cursur.execute(sql,value)
                else:
                    if not Delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Your Employee has been Deleted",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)


 # reset
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_name.set("")
        self.var_designition.set("")
        self.var_email.set("")
        self.var_address.set("")
        self.var_married.set("Married")
        self.var_dob.set("")
        self.var_doj.set("")
        self.var_idproofcomb.set("Select ID Proof")
        self.var_idproof.set("")
        self.var_gender.set("Male")
        self.var_phone.set("")
        self.var_country.set("")
        self.var_salary.set("")

 # search data
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror("Error","Plaese select option")
        else:
            try:
                conn=mysql.connector.connect(host='localhost',username='amey020',password='1234',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute("select * from employee where " +str(self.var_com_search.get())+" LIKE '%"+str(self.var_search.get())+"%'") 
                rows=my_cursor.fetchall() 

                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                
    
                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
      


            
     


if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()



    