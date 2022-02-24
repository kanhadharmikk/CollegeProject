from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector

def main():
    win=Tk()
    app=Login(win)
    win.mainloop()

class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN WINDOW")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
        # self.root.config(bg="#FAFAD2")

        self.bg=ImageTk.PhotoImage(file="bg.jpg")
        lab1_bg=Label(self.root,image=self.bg)
        lab1_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open("logo.png")
        img1=img1.resize((110,110),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)

        labimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        labimg1.place(x=730,y=195,width=100,height=100)

        get_str=Label(frame,text="Login Page",font=("Arial",20,"bold"),fg="black",bg="black")
        get_str.place(x=95,y=100)

        #Label
        username=lb1=Label(frame,text="Username",font=("Arial",15),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("Arial",15,"bold"))
        self.txtuser.place(x=40,y=190,width=270)

        password = lb1 = Label(frame, text="Password", font=("Arial", 15), fg="white", bg="black")
        password.place(x=70, y=235)

        self.txtpass = ttk.Entry(frame, font=("Arial", 15, "bold"))
        self.txtpass.place(x=40, y=270, width=270)

        # Icon Image
        img2 = Image.open("user.png")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimage2 = ImageTk.PhotoImage(img2)

        labimg1 = Label(image=self.photoimage2, bg="black", borderwidth=0)
        labimg1.place(x=650, y=323, width=25, height=25)

        img3 = Image.open("pass.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimage3 = ImageTk.PhotoImage(img3)

        labimg1 = Label(image=self.photoimage3, bg="black", borderwidth=0)
        labimg1.place(x=650, y=405, width=25, height=30)


        # Button
        loginbtn=Button(frame,text="Login",font=("Arial", 15, "bold"),bd=3,relief=RIDGE,fg="#EEE8AA",bg="#FF6347",command=self.login)
        loginbtn.place(x=110,y=330,width=120,height=35)

        registerbtn = Button(frame, text="Create New Account",command=self.register_window, font=("Arial", 10, "bold"), borderwidth=0, fg="#EEE8AA",bg="black")
        registerbtn.place(x=20, y=375, width=160)

        forgetbtn = Button(frame, text="Forget Password ?",command=self.forgot_pass, font=("Arial", 10, "bold"), borderwidth=0, fg="#EEE8AA",bg="black")
        forgetbtn.place(x=15, y=405, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","Username or Password cannot be empty.")
        elif self.txtuser.get()=="Kanha" and self.txtpass.get()=="Nachi":
            messagebox.showinfo("Success","Login Successful.")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Testkanha123",database="archsafedb")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from regtable where Email=%s and Password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=endecrypt(self.new_window)
                else:
                    if not open_main:
                        return

            conn.commit()
            conn.close()






#Forgot Password
    def forgot_pass(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the email")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Testkanha123",
                                           database="archsafedb")
            my_cursor = conn.cursor()
            query=("select * from regtable where Email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            # print(row)

            if row==None:
                messagebox.showerror("Error","Please Enter the valid Username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("Arial", 20, "bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                new_mob=Label(self.root2,text="Enter Mobile Number",font=("Arial", 16, "bold"),fg="black")
                new_mob.place(x=50,y=90)

                self.new_mob_entry = ttk.Entry(self.root2, font=("Arial", 15))
                self.new_mob_entry.place(x=50, y=130, width=250)

                new_pass = Label(self.root2, text="Enter New Password", font=("Arial", 16, "bold"), fg="black")
                new_pass.place(x=50, y=170)

                self.new_pass_entry = ttk.Entry(self.root2, font=("Arial", 15))
                self.new_pass_entry.place(x=50, y=210, width=250)


                forgotbtn = Button(self.root2, text="Reset Password", font=("Arial", 9, "bold"), bd=3, relief=RIDGE, fg="white",
                                bg="#FF6347",command=self.reset_pass)
                forgotbtn.place(x=110, y=280, width=120)

    def reset_pass(self):
        if self.new_mob_entry.get()=="":
            messagebox.showerror("Error","Enter Registered Mobile Number")
        elif self.new_pass_entry.get()=="":
            messagebox.showerror("Error", "Enter New Password")

        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Testkanha123",
                                           database="archsafedb")
            my_cursor = conn.cursor()
            query=("select * from regtable where Email=%s and Password=%s")
            value=(self.txtuser.get(),self.txtpass.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","Enter valid Information")
            else:
                query=("update regtable set Password=%s where Email=%s ")
                value=(self.new_pass_entry.get(),self.txtuser.get())
                my_cursor.execute(query,value)

                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been Reset,Please Login new Password")


class Register:
    def __init__(self,root):
        self.root = root
        self.root.title("REGISTERATION WINDOW")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))

        # Variable
        self.var_fname=StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_pass = StringVar()
        self.var_cpass = StringVar()





        self.bg = ImageTk.PhotoImage(file="bg.jpg")
        bg_lab1 = Label(self.root, image=self.bg)
        bg_lab1.place(x=0, y=0, relwidth=1, relheight=1)

        self.bg1 = ImageTk.PhotoImage(file="register.jpg")
        left_lab1 = Label(self.root, image=self.bg1)
        left_lab1.place(x=50, y=100,width=470,height=550)

        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        # Label
        reg_lbl = Label(frame,text="REGISTER HERE",font=("Arial",20,"bold"),fg="black",bg="white")
        reg_lbl.place(x=20, y=20)

        # Row1
        # Firstname
        fname=Label(frame,text="First Name",font=("Arial",16),fg="black",bg="white")
        fname.place(x=20,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("Arial",15))
        self.fname_entry.place(x=20,y=130,width=250)

        # Lastname
        lname = Label(frame, text="Last Name", font=("Arial", 16), fg="black", bg="white")
        lname.place(x=370, y=100)

        self.lname_entry = ttk.Entry(frame,textvariable=self.var_lname, font=("Arial", 15))
        self.lname_entry.place(x=370, y=130, width=250)

        # Row2
        contact=Label(frame,text="Mobile Number",font=("Arial",16),fg="black",bg="white")
        contact.place(x=20,y=170)
        self.txt_contact = ttk.Entry(frame,textvariable=self.var_contact, font=("Arial", 15))
        self.txt_contact.place(x=20, y=200, width=250)

        email = Label(frame, text="Email Id", font=("Arial", 16), fg="black", bg="white")
        email.place(x=370, y=170)
        self.txt_email = ttk.Entry(frame,textvariable=self.var_email, font=("Arial", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # Row3
        pwd = Label(frame, text="Password", font=("Arial", 16), fg="black", bg="white")
        pwd.place(x=20, y=240)
        self.txt_pwd = ttk.Entry(frame,textvariable=self.var_pass, font=("Arial", 15))
        self.txt_pwd.place(x=20, y=270, width=250)

        cpwd = Label(frame, text="Confirm Password", font=("Arial", 16), fg="black", bg="white")
        cpwd.place(x=370, y=240)
        self.txt_cpwd = ttk.Entry(frame,textvariable=self.var_cpass, font=("Arial", 15))
        self.txt_cpwd.place(x=370, y=270, width=250)

        #button
        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("Arial", 15), fg="black", bg="white",onvalue=1,offvalue=0)
        self.checkbtn.place(x=20,y=340)

        # img=Image.open("regbtn.jpg")
        # img = img.resize((200, 50), Image.ANTIALIAS)
        # self.photoimage=ImageTk.PhotoImage(img)
        # b1=Button(frame,image=self.photoimage,borderwidth=0,cursor="hand2",font=("Arial", 15),bg="white")
        # b1.place(x=10,y=420,width=300)
        regbtn = Button(frame, text="Register", font=("Arial", 15, "bold"), bd=3, relief=RIDGE, fg="#EEE8AA",bg="#FF6347",command=self.register_data)
        regbtn.place(x=20,y=420,width=300)

        loginbtn = Button(frame, text="Login", font=("Arial", 15, "bold"), bd=3, relief=RIDGE, fg="#EEE8AA",bg="#FF6347")
        loginbtn.place(x=370, y=420, width=300)

    def register_data(self):
        if self.var_fname.get()=="" or self.var_lname.get()=="" or self.var_email.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are required")

        elif self.var_pass.get() != self.var_cpass.get():
            messagebox.showerror("Error","Password and Confirm Password must be same.")
        elif self.var_check.get()==0:
            messagebox.showerror("Error", "Please agree our Terms & Conditions")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Testkanha123",database="archsafedb")
            my_cursor=conn.cursor()
            query=("select * from regtable where email=%s")
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist , Please try another email")
            else:
                my_cursor.execute("insert into regtable values(%s,%s,%s,%s,%s)",(
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

class endecrypt:
    def __init__(self,root):
        self.root=root
        self.root.title("Encryption Decryption")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    #
    # lab1 = Label(text="Enter your Message", font=("Arial", 13), bg="#FAFAD2", fg="#800000")
    # lab1.grid(row=0, column=0)
    #
    # lab2 = Label(text="Your Decrypted Message", font=("Arial", 13), bg="#FAFAD2", fg="#800000")
    # lab2.grid(row=0, column=1)
    #
    # # Entry
    # m_entry1 = Text(padx=15, width=60, height=30)
    # m_entry1.focus()
    # m_entry1.grid(row=1, column=0, padx=20)
    #
    # m_entry2 = Text(padx=15, width=60, height=30)
    # m_entry2.grid(row=1, column=1, padx=20)
    #
    # # Button
    # en_btn = Button(text="Encrypt", bg="#FFF8DC", fg="#800000", padx=28)
    # en_btn.grid(row=2, column=0, pady=15)
    #
    # dn_btn = Button(text="Decrypt", bg="#FFF8DC", fg="#800000", padx=28)
    # dn_btn.grid(row=2, column=1, pady=15)











if __name__ == '__main__':
    main()


