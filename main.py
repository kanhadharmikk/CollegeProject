from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import base64
import pyttsx3

from ciphers import RSAC, affineC, vernamOneTimePadC, caesarC, homophonicC, railfenceC, autokeyC, atbashC, columnerC, \
    beaufortC, beaufortautokeyC, vignereC, vignereautokeyC, playfairC, morseC


class Login():
    def __init__(self,root):
        self.root=root
        self.root.title("LOGIN WINDOW")
        self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
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
            # self.engine.say('Username or Password cannot be empty')
            # self.engine.runAndWait()
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
                    wind1=Toplevel()
                    app=project(wind1)
                    # exec(open(project))

                



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


class Register():
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





# class endecrypt:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Encryption Decryption")
#         self.root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))




def project(root):
    root = Tk()
    root.configure(background="gray")
    root.title("cryptociphers")
    root.geometry("500x500")
    root.state("zoomed")
    title_frame = Frame(root, width=180, height=180, relief=SUNKEN, borderwidth=10)
    title_frame.pack()


    # img=Image.open('C:/Users/Kolluri Midhun/OneDrive/Documents/bennett.png')
    # img=ImageTk.PhotoImage(img)
    # icon=Button(title_frame,image=img)
    # icon.pack()

    ################################################################################################################################

    def cipher():
        root.destroy()

        window = Tk()

        window.configure(background='gray')
        window.geometry("500x500")
        window.state("zoomed")
        window.title("Cryptographic ciphers")

        # downLabel = "Cryptography, or cryptology, is the practice and study of techniques for /n secure communication in the presence of third parties called adversaries."
        ###################################################################################################################################
        # frame code

        left_frame = Frame(window, width=200, height=600, relief=SUNKEN)
        left_frame.pack(side=LEFT)
        right_frame = Frame(window, width=200, height=600, relief=SUNKEN)
        right_frame.pack(side=RIGHT)

        main_frame = Frame(window, width=800, height=100, relief=SUNKEN, borderwidth=10)
        main_frame.pack()

        main = Frame(window, width=800, height=400, relief=SUNKEN, bg='black')
        main.pack()

        time_frame = Frame(window, width=500, height=30, relief=SUNKEN, background='gray')
        time_frame.pack(side=BOTTOM)

        ###############################################################################################################################

        # img=Image.open('C:/Users/Kolluri Midhun/OneDrive/Pictures/title_image.png')
        # img=ImageTk.PhotoImage(img)
        # icon=Button(main_frame,image=img)
        # icon.pack()

        def remove():
            for widget in main.winfo_children():
                widget.destroy()

        def window_show():
            remove()

        def lab():

            text_label = Label(main, text="Enter text: ", font=('Arial', 16, "bold"), bg="black", fg="white")
            text_label.grid(row=0, column=0, padx=20, pady=20)

            scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
            text_box = Text(main, height=8, width=40, pady=10, yscrollcommand=scroll_text.set, bg='white')
            text_box.grid(row=1, column=0, pady=1, padx=1)
            scroll_text.config(command=text_box.yview)
            scroll_text.grid(row=1, column=1, sticky='NS')

            key_label = Label(main, text="Enter key: ", font=('Arial', 14), pady=15,
                              bg='black', fg="cyan")
            key_label.grid(row=2, column=0)

            scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
            new_text = Text(main, height=8, width=40, pady=10, yscrollcommand=scroll_text2.set, bg='white')
            new_text.grid(row=1, column=2, columnspan=2, padx=(10, 0))
            scroll_text2.config(command=new_text.yview)
            scroll_text2.grid(row=1, column=4, sticky='NS')
            return text_box, new_text

        ################################################################################################################################
        def caesar_cipher():  # 1st cipher

            remove()

            # label.config(text = "Caesar Cipher")
            # label.grid(row = 0, column = 0)

            list_key = ttk.Combobox(main)
            list_key['values'] = (
            1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
            list_key.current(0)
            list_key.grid(row=5, column=0)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nnumerical value 1-26\nDefault: 1"
            new_text.insert(1.0, sample)
            label = Label(main, text="caesar_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = int(list_key.get())
                enc_text = caesarC.encryption(txt, key)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt, bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = int(list_key.get())
                dec_text = caesarC.decryption(txt, key)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt, bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        #############################################################################################################################
        def homophonic_cipher():
            remove()

            key_table = {'A': 'D9', 'B': 'X', 'C': 'S', 'D': 'F', 'E': 'Z721', 'F': 'E', 'G': 'H', 'H': 'C', 'I': 'V3',
                         'J': 'I', 'K': 'T', 'L': 'P', 'M': 'G', 'N': 'A5', 'O': 'Q0', 'P': 'L', 'Q': 'K', 'R': 'J',
                         'S': 'R4', 'T': '6U',
                         'U': 'O', 'V': 'W', 'W': 'M', 'X': 'Y', 'Y': 'B', 'Z': 'N', 'a': 'd(', 'b': 'x', 'c': 's',
                         'd': 'f', 'e': 'z&@!',
                         'f': 'e', 'g': 'h', 'h': 'c', 'i': 'v#', 'j': 'i', 'k': 't', 'l': 'p', 'm': 'g', 'n': 'a%',
                         'o': 'q)', 'p': 'l',
                         'q': 'k', 'r': 'j', 's': 'r$', 't': '^u', 'u': 'o', 'v': 'w', 'w': 'm', 'x': 'y', 'y': 'b',
                         'z': 'n'}

            text_label = Label(main, text="Enter text: ", font=('fixedsys', 12, 'bold'), bg='black', fg='white')
            text_label.grid(row=0, column=0, padx=20, pady=20)

            scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
            label = Label(main, text="homophonic_cipher")
            label.grid(row=0, column=1)
            text_box = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text.set, bg='plum1')
            text_box.grid(row=1, column=0, pady=1, padx=1)
            scroll_text.config(command=text_box.yview)
            scroll_text.grid(row=1, column=1, sticky='NS')

            scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
            new_text = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text2.set, bg='plum1')
            new_text.grid(row=1, column=2, columnspan=2, padx=(10, 0))
            sample = "Sample text input:\nAny character\n"
            new_text.insert(1.0, sample)

            scroll_text2.config(command=new_text.yview)
            scroll_text2.grid(row=1, column=4, sticky='NS')

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                enc_text = homophonicC.encryption(txt)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=20)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                dec_text = homophonicC.decryption(txt)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ##############################################################################################################################
        def vignere_cipher():
            remove()

            key_text = Entry(main, width=40)
            key_text.grid(row=3, column=0, padx=10, pady=10)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: a"
            new_text.insert(1.0, sample)
            label = Label(main, text="vignere_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                enc_text = vignereC.encrypt(txt, key)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                dec_text = vignereC.decrypt(txt, key)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        #############################################################################################################################
        def autokey_cipher():
            remove()

            key_text = Entry(main, width=40)
            key_text.grid(row=3, column=0, padx=10, pady=10)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault: A"
            new_text.insert(1.0, sample)
            label = Label(main, text="autokey_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                enc_text = autokeyC.encrypt(txt, key)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                dec_text = autokeyC.decrypt(txt, key)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ################################################################################################################################

        def railfence_cipher():
            remove()

            list_key = ttk.Combobox(main)
            list_key['values'] = (2, 3, 4, 5, 6, 7, 8)
            list_key.current(0)
            list_key.grid(row=5, column=0)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nPositive integer < length of input\nDefault: 2"
            new_text.insert(1.0, sample)
            label = Label(main, text="railfence_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                string = (text_box.get("1.0", END)).strip()
                key = int(list_key.get())
                enc_text = railfenceC.encrypt(string, key)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                string = (text_box.get("1.0", END)).strip()
                key = int(list_key.get())
                dec_text = railfenceC.decrypt(string, key)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ###############################################################################################################################

        def playfair_cipher():
            remove()

            key_text = Entry(main, width=40)
            key_text.grid(row=3, column=0, padx=10, pady=10)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault: ABCD\n(Note:Case of key & text should be same)"
            new_text.insert(1.0, sample)
            label = Label(main, text="playfair_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                enc_text = playfairC.encrypt(txt, key)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                dec_text = playfairC.decrypt(txt, key)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ###############################################################################################################################

        def atbash_cipher():
            remove()

            text_label = Label(main, text="Enter text: ", font=('fixedsys', 12, 'bold'), bg='black', fg="cyan")
            text_label.grid(row=0, column=0, padx=20, pady=20)

            scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
            label = Label(main, text="atbash_cipher")
            label.grid(row=0, column=1)
            text_box = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text.set, bg='plum1')
            text_box.grid(row=1, column=0, pady=1, padx=1)
            scroll_text.config(command=text_box.yview)
            scroll_text.grid(row=1, column=1, sticky='NS')

            scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
            new_text = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text2.set, bg='plum1')
            new_text.grid(row=1, column=2, columnspan=2, padx=(10, 0))
            scroll_text2.config(command=new_text.yview)
            scroll_text2.grid(row=1, column=4, sticky='NS')
            sample = "Sample text input:\nAny character\n"
            new_text.insert(1.0, sample)

            def convert():
                new_text.delete('1.0', END)
                string = text_box.get("1.0", END)
                converted_text = atbashC.encrypt(string)
                new_text.insert(1.0, converted_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=convert,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=10)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=convert,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=20)

        #################################################################################################################

        def vignere_autokey_cipher():
            remove()

            key_text = Entry(main, width=40)
            key_text.grid(row=3, column=0, padx=10, pady=10)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: a"
            new_text.insert(1.0, sample)
            label = Label(main, text="vignere_autokey_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                enc_text = vignereautokeyC.encrypt(txt, key)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                dec_text = vignereautokeyC.decrypt(txt, key)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ###############################################################################################################################
        def beaufort_cipher():
            remove()

            key_text = Entry(main, width=40)
            key_text.grid(row=3, column=0, padx=10, pady=10)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: abc"
            new_text.insert(1.0, sample)
            label = Label(main, text="beaufort_cipher")
            label.grid(row=0, column=1)

            def convert():
                spl = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '<', '~', ':', ';', '<', '>', '?', '/']
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                converted_text = beaufortC.convert(txt, key)
                new_text.insert(1.0, converted_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=convert,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=10)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=convert,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=30)

        ##############################################################################################################################
        def beaufort_autokey_cipher():
            remove()

            key_text = Entry(main, width=40)
            key_text.grid(row=3, column=0, padx=10, pady=10)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: abc"
            new_text.insert(1.0, sample)
            label = Label(main, text="beaufort_autokey_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                converted_text = beaufortautokeyC.encrypt(txt, key)
                new_text.insert(1.0, converted_text)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get()
                converted_text = beaufortautokeyC.decrypt(txt, key)
                new_text.insert(1.0, converted_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ############################################################################################################################
        def columnar_trans_cipher():
            remove()

            key_text = Entry(main, width=40)
            key_text.grid(row=3, column=0, padx=10, pady=10)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nAlphabet/Word\nDefault Key: key"
            new_text.insert(1.0, sample)
            label = Label(main, text="columnar_trans_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get().lower()
                enc_text = columnerC.encrypt(txt, key)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = key_text.get().lower()
                dec_text = columnerC.decrypt(txt, key)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ################################################################################################################################
        def morse_code():

            remove()

            text_label = Label(main, text="Enter text: ", font=('fixedsys', 12, 'bold'), bg='black', fg="cyan")
            text_label.grid(row=0, column=0, padx=20, pady=20)

            scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
            label = Label(main, text="morse_code_cipher")
            label.grid(row=0, column=1)
            text_box = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text.set, bg='plum1')
            text_box.grid(row=1, column=0, pady=1, padx=1)
            scroll_text.config(command=text_box.yview)
            scroll_text.grid(row=1, column=1, sticky='NS')

            scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
            new_text = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text2.set, bg='plum1')
            new_text.grid(row=1, column=2, columnspan=2, padx=(10, 0))
            scroll_text2.config(command=new_text.yview)
            scroll_text2.grid(row=1, column=4, sticky='NS')
            sample = "Sample text input:\nCapital Letter/Numbers/Punctuations\n\nFor decryption: Add spaces between each character"
            new_text.insert(1.0, sample)

            Morse_dict = {
                'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
                'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
                '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....',
                '7': '--...', '8': '---..', '9': '----.', '0': '-----', ',': '--..--', '.': '.-.-.-',
                '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', ' ': '`'}

            Reverse_morse = {val: key for key, val in Morse_dict.items()}

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                enc_text = morseC.encrypt(txt)
                new_text.insert(1.0, enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt,
                         bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=20)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get('1.0', END)
                dec_text = morseC.decrypt(txt)
                new_text.insert(1.0, dec_text)

            dec = Button(main, text='Decrypt', bd=10, width=10, command=decrypt,
                         bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ##############################################################################################################################
        def onetimepad():
            remove()

            key_text = Text(main, height=1, width=10, pady=5, bg='white')
            key_text.grid(row=3, column=0, pady=1, padx=1)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nInput Type\n for alphabets 1\n for binary 2 \n for numbers 3"
            new_text.insert(1.0, sample)
            text_label = Label(main, text="Input Type: ", font=('fixedsys', 12, 'bold'), bg='black', fg="cyan")
            text_label.grid(row=4, column=0, pady=5)
            box = Text(main, height=1, width=10, pady=5, bg='white')
            box.grid(row=5, column=0, pady=1, padx=1)
            label = Label(main, text="onetimepad_cipher")
            label.grid(row=0, column=1)

            def encrypt():

                new_text.delete('1.0', END)
                plainText = text_box.get("1.0", END)
                key = key_text.get('1.0', END)

                input_type = box.get(1.0, END)

                def encryption(plainText, key, input_type):

                    method = [26, 2, 10]
                    subract = [97, 48, 48]

                    input_type = int(input_type)
                    plainText, key = plainText.rstrip().lower().split(), key.rstrip().lower().split()
                    cipherText = []

                    for i in range(len(plainText)):
                        partial_cipherText = ""
                        for j in range(len(plainText[i])):
                            c = (ord(plainText[i][j]) + ord(key[i][j]) - 2 * subract[input_type - 1]) % method[
                                input_type - 1]
                            partial_cipherText += chr(c + subract[input_type - 1])
                        cipherText.append(partial_cipherText)

                    cipherText = " ".join(cipherText)

                    enc_text = cipherText
                    new_text.insert('1.0', enc_text)

                encryption(plainText, key, input_type)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt, bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():

                new_text.delete('1.0', END)
                plainText = text_box.get("1.0", END)
                key = key_text.get('1.0', END)

                input_type = box.get(1.0, END)

                def decryption(cipherText, key, input_type):
                    method = [26, 2, 10]
                    subract = [97, 48, 48]
                    input_type = int(input_type)

                    cipherText, key = cipherText.lower().split(), key.lower().split()
                    plainText = []

                    for i in range(len(cipherText)):
                        partial_plainText = ""
                        for j in range(len(cipherText[i])):
                            p = (ord(cipherText[i][j]) - ord(key[i][j])) % method[input_type - 1]
                            partial_plainText += chr(p + subract[input_type - 1])
                        plainText.append(partial_plainText)

                    plainText = " ".join(plainText)

                    enc_text = plainText
                    new_text.insert('1.0', enc_text)

                decryption(plainText, key, input_type)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt, bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ###################################################################################################################################

        def affine_cipher():

            remove()

            list_key = ttk.Combobox(main)
            list_key['values'] = (1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25)
            list_key.current(0)
            list_key.grid(row=5, column=0)
            list_key1 = ttk.Combobox(main)
            list_key1['values'] = (1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
            list_key1.current(0)
            list_key1.grid(row=6, column=0)

            text_box, new_text = lab()
            sample = "Sample text input:\nAny character\n\nSample Key input:\nnumerical value 1-26\nDefault: 1"
            new_text.insert(1.0, sample)
            label = Label(main, text="Affine_cipher")
            label.grid(row=0, column=1)

            def encrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = int(list_key.get())
                key1 = int(list_key1.get())
                enc_text = affineC.encryption(txt, key, key1)
                new_text.insert('1.0', enc_text)

            enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt, bg='white', fg='black')
            enc.grid(row=0, column=2, padx=20, pady=30)

            def decrypt():
                new_text.delete('1.0', END)
                txt = text_box.get("1.0", END)
                key = int(list_key.get())
                key1 = int(list_key1.get())
                dec_text = affineC.decryption(txt, key, key1)
                new_text.insert('1.0', dec_text)

            dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt, bg='white', fg='black')
            dec.grid(row=0, column=3, padx=10, pady=10)

        ###########################################################################################################################
        # buttons on window left lide
        home_button = Button(left_frame, padx=20, bd=10, text='Home', width=20, height=3, command=window_show,
                             bg='#98AFC7', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                             activeforeground='SeaGreen1')
        home_button.grid(row=0, column=0, pady=5)

        caesar = Button(left_frame, padx=15, bd=10, text='Caesar Cipher', width=20, height=2, command=caesar_cipher,
                        bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                        activeforeground='SeaGreen1')
        caesar.grid(row=1, column=0, pady=5)

        homophonic = Button(left_frame, padx=15, bd=10, text='Homophonic Cipher', width=20, height=2,
                            command=homophonic_cipher, bg='#3D3C3A', fg='white', activebackground='black',
                            font=('arial', 12, 'bold'), activeforeground='SeaGreen1')
        homophonic.grid(row=2, column=0, pady=5)

        vignere = Button(left_frame, padx=15, bd=10, text='Vignere Cipher', width=20, height=2, command=vignere_cipher,
                         bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                         activeforeground='SeaGreen1')
        vignere.grid(row=3, column=0, pady=5)

        autokey = Button(left_frame, padx=15, bd=10, text='Autokey Cipher', width=20, height=2, command=autokey_cipher,
                         bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                         activeforeground='SeaGreen1')
        autokey.grid(row=4, column=0, pady=5)

        railfence = Button(left_frame, padx=15, bd=10, text='Railfence Cipher', width=20, height=2,
                           command=railfence_cipher, bg='#3D3C3A', fg='white', activebackground='black',
                           font=('arial', 12, 'bold'), activeforeground='SeaGreen1')
        railfence.grid(row=5, column=0, pady=5)

        affine = Button(left_frame, padx=15, bd=10, text='Affine Cipher', width=20, height=2, command=affine_cipher,
                        bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                        activeforeground='SeaGreen1')
        affine.grid(row=7, column=0, pady=5)

        onetimepad = Button(left_frame, padx=15, bd=10, text='One Time Pad', width=20, height=2, command=onetimepad,
                            bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'), activebackground='black',
                            activeforeground='SeaGreen1')
        onetimepad.grid(row=8, column=0, pady=5)

        playfair = Button(right_frame, padx=15, bd=10, text='Playfair Cipher', width=20, height=2,
                          command=playfair_cipher,
                          bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                          activeforeground='SeaGreen1')
        playfair.grid(row=6, column=0, pady=5, padx=10)

        atbash = Button(right_frame, padx=15, bd=10, text='Atbash Cipher', width=20, height=2, command=atbash_cipher,
                        bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                        activeforeground='SeaGreen1')
        atbash.grid(row=9, column=0, pady=5)

        vignere_autokey = Button(right_frame, padx=15, bd=10, text='Vignere Autokey Cipher', width=20, height=2,
                                 command=vignere_autokey_cipher, bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'),
                                 activebackground='black', activeforeground='yellow')
        vignere_autokey.grid(row=10, column=0, pady=5)

        beaufort = Button(right_frame, padx=15, bd=10, text='Beaufort Cipher', width=20, height=2,
                          command=beaufort_cipher,
                          bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                          activeforeground='SeaGreen1')
        beaufort.grid(row=11, column=0, pady=5)

        beaufort_autokey = Button(right_frame, padx=15, bd=10, text='Beaufort Autokey Cipher', width=20, height=2,
                                  command=beaufort_autokey_cipher, bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'),
                                  activebackground='black', activeforeground='SeaGreen1')
        beaufort_autokey.grid(row=12, column=0, pady=5)

        columnar = Button(right_frame, padx=15, bd=10, text='Columnar Transposition Cipher', width=20, height=2,
                          command=columnar_trans_cipher, bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'),
                          activebackground='black', activeforeground='SeaGreen1')
        columnar.grid(row=13, column=0, pady=5)

        morse = Button(right_frame, padx=15, bd=10, text='Morse Code', width=20, height=2, command=morse_code,
                       bg='#3D3C3A',
                       fg='white', font=('arial', 12, 'bold'), activebackground='black', activeforeground='SeaGreen1')
        morse.grid(row=14, column=0, pady=5)
        Exit = Button(right_frame, padx=20, text="Exit", bd=10, width=20, height=2, command=window.destroy,
                      activebackground="black",
                      bg='#98AFC7', fg="white", font=('arial', 12, 'bold'), activeforeground="green2")
        Exit.grid(row=15, column=0, pady=9)

        window.mainloop()





    ##############################################################################################################

    Welcome_label = Label(root, text="Welcome to Cryptography ciphers", padx=10, pady=20, fg="black",
                          font=("Arial", 20, "bold")).place(x=500, y=320)
    chiper_button = Button(root, text="Cryptocypher", padx=20, bd=10, width=20, height=3, command=cipher, bg="black",
                           fg="white", font=("Arial", 10, "bold"))
    chiper_button.place(x=620, y=430)


    root.mainloop()






def main():
    win=Tk()
    app=Login(win)
    win.mainloop()






if __name__ == '__main__':
    main()





