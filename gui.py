from tkinter import *
import random
import webbrowser
from tkinter import ttk
from time import strftime
from PIL import Image, ImageTk
from ciphers import RSAC, affineC, vernamOneTimePadC, caesarC, homophonicC, railfenceC, autokeyC, atbashC, columnerC, \
    beaufortC, beaufortautokeyC, vignereC, vignereautokeyC, playfairC, morseC



root = Tk()

bg = ImageTk.PhotoImage(file="bg.jpg")
lab1_bg = Label(root, image=bg)
lab1_bg.place(x=0, y=0, relwidth=1, relheight=1)
root.title("cryptociphers")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
bg1 = ImageTk.PhotoImage(file="hacker.jpg")
left_lab1 = Label(root, image=bg1)
left_lab1.place(x=570,y=10,width=300,height=300)




################################################################################################################################

def cipher():
    root.destroy()

    window = Tk()

    window.configure(background='gray')
    window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
    window.title("Cryptographic ciphers")
    left_frame = Frame(window, width=200, height=600, relief=SUNKEN)
    left_frame.pack(side=LEFT)
    right_frame = Frame(window, width=200, height=600, relief=SUNKEN)
    right_frame.pack(side=RIGHT)

    main_frame = Frame(window, width=800, height=100, relief=SUNKEN, borderwidth=10)
    main_frame.pack()

    main = Frame(window, width=800, height=600, relief=SUNKEN, bg='black')
    main.pack(pady=10)

    time_frame = Frame(window, width=500, height=30, relief=SUNKEN, background='gray')
    time_frame.pack(side=BOTTOM)

    ###############################################################################################################################



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

        text_label = Label(main, text="Enter text: ", font=('Arial', 12, 'bold'), bg='black', fg="white")
        text_label.grid(row=0, column=0, padx=20, pady=20)

        scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
        label = Label(main, text="homophonic_cipher")
        label.grid(row=0, column=1)
        text_box = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text.set)
        text_box.grid(row=1, column=0, pady=1, padx=1)
        scroll_text.config(command=text_box.yview)
        scroll_text.grid(row=1, column=1, sticky='NS')

        scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
        new_text = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text2.set)
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

        text_label = Label(main, text="Enter text: ", font=('Arial', 12, 'bold'), bg='black', fg="cyan")
        text_label.grid(row=0, column=0, padx=20, pady=20)

        scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
        label = Label(main, text="atbash_cipher")
        label.grid(row=0, column=1)
        text_box = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text.set)
        text_box.grid(row=1, column=0, pady=1, padx=1)
        scroll_text.config(command=text_box.yview)
        scroll_text.grid(row=1, column=1, sticky='NS')

        scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
        new_text = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text2.set)
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

        text_label = Label(main, text="Enter text: ", font=('Arial', 12, 'bold'), bg='black', fg="cyan")
        text_label.grid(row=0, column=0, padx=20, pady=20)

        scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
        label = Label(main, text="morse_code_cipher")
        label.grid(row=0, column=1)
        text_box = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text.set)
        text_box.grid(row=1, column=0, pady=1, padx=1)
        scroll_text.config(command=text_box.yview)
        scroll_text.grid(row=1, column=1, sticky='NS')

        scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
        new_text = Text(main, height=20, width=40, pady=10, yscrollcommand=scroll_text2.set)
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
        text_label = Label(main, text="Input Type: ", font=('Arial', 12, 'bold'), bg='black', fg="cyan")
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
    home_button.grid(row=0, column=0,pady=5)

    caesar = Button(left_frame, padx=15, bd=10, text='Caesar Cipher', width=20, height=2, command=caesar_cipher,
                    bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                    activeforeground='SeaGreen1')
    caesar.grid(row=1, column=0,pady=5)

    homophonic = Button(left_frame, padx=15, bd=10, text='Homophonic Cipher', width=20, height=2,
                        command=homophonic_cipher, bg='#3D3C3A', fg='white', activebackground='black',
                        font=('arial', 12, 'bold'), activeforeground='SeaGreen1')
    homophonic.grid(row=2, column=0,pady=5)

    vignere = Button(left_frame, padx=15, bd=10, text='Vignere Cipher', width=20, height=2, command=vignere_cipher,
                     bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                     activeforeground='SeaGreen1')
    vignere.grid(row=3, column=0,pady=5)

    autokey = Button(left_frame, padx=15, bd=10, text='Autokey Cipher', width=20, height=2, command=autokey_cipher,
                     bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                     activeforeground='SeaGreen1')
    autokey.grid(row=4, column=0,pady=5)

    railfence = Button(left_frame, padx=15, bd=10, text='Railfence Cipher', width=20, height=2,
                       command=railfence_cipher, bg='#3D3C3A', fg='white', activebackground='black',
                       font=('arial', 12, 'bold'), activeforeground='SeaGreen1')
    railfence.grid(row=5, column=0,pady=5)

    affine = Button(left_frame, padx=15, bd=10, text='Affine Cipher', width=20, height=2, command=affine_cipher,
                    bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                    activeforeground='SeaGreen1')
    affine.grid(row=7, column=0,pady=5)

    onetimepad = Button(left_frame, padx=15, bd=10, text='One Time Pad', width=20, height=2, command=onetimepad,
                        bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'), activebackground='black',
                        activeforeground='SeaGreen1')
    onetimepad.grid(row=8, column=0,pady=5)

    playfair = Button(right_frame, padx=15, bd=10, text='Playfair Cipher', width=20, height=2, command=playfair_cipher,
                      bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                      activeforeground='SeaGreen1')
    playfair.grid(row=6, column=0,pady=5,padx=10)

    atbash = Button(right_frame, padx=15, bd=10, text='Atbash Cipher', width=20, height=2, command=atbash_cipher,
                    bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                    activeforeground='SeaGreen1')
    atbash.grid(row=9, column=0,pady=5)

    vignere_autokey = Button(right_frame, padx=15, bd=10, text='Vignere Autokey Cipher', width=20, height=2,
                             command=vignere_autokey_cipher, bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'),
                             activebackground='black', activeforeground='yellow')
    vignere_autokey.grid(row=10, column=0,pady=5)

    beaufort = Button(right_frame, padx=15, bd=10, text='Beaufort Cipher', width=20, height=2, command=beaufort_cipher,
                      bg='#3D3C3A', fg='white', activebackground='black', font=('arial', 12, 'bold'),
                      activeforeground='SeaGreen1')
    beaufort.grid(row=11, column=0,pady=5)

    beaufort_autokey = Button(right_frame, padx=15, bd=10, text='Beaufort Autokey Cipher', width=20, height=2,
                              command=beaufort_autokey_cipher, bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'),
                              activebackground='black', activeforeground='SeaGreen1')
    beaufort_autokey.grid(row=12, column=0,pady=5)

    columnar = Button(right_frame, padx=15, bd=10, text='Columnar Transposition Cipher', width=20, height=2,
                      command=columnar_trans_cipher, bg='#3D3C3A', fg='white', font=('arial', 12, 'bold'),
                      activebackground='black', activeforeground='SeaGreen1')
    columnar.grid(row=13, column=0,pady=5)

    morse = Button(right_frame, padx=15, bd=10, text='Morse Code', width=20, height=2, command=morse_code, bg='#3D3C3A',
                   fg='white', font=('arial', 12, 'bold'), activebackground='black', activeforeground='SeaGreen1')
    morse.grid(row=14, column=0,pady=5)
    Exit = Button(right_frame,padx=20, text="Exit", bd=10, width=20,height=2, command=window.destroy, activebackground="black",
                  bg='#98AFC7', fg="white", font=('arial', 12, 'bold'), activeforeground="green2")
    Exit.grid(row=15, column=0,pady=9)

    window.mainloop()


############################################################################################################################
def hackertools():
    root.destroy()
    window = Tk()
    window.title("hackertools")
    label = Label(window, text=" hackertools").pack()
    left_frame = Frame(window, width=200, height=600, relief=SUNKEN)
    left_frame.pack(side=LEFT)
    main = Frame(window, width=200, height=600, relief=SUNKEN)
    main.pack()

    def remove():
        for widget in main.winfo_children():
            widget.destroy()

    def window_show():
        remove()
        downLabelName = Label(main, text="downLabel", fg="cyan", bg='black', font=('fixedsys', 17), anchor=CENTER,
                              wraplength=250)
        downLabelName.grid(row=1, column=0)

    def lab():
        text_label = Label(main, text="Enter text: ", font=('fixedsys', 16, "bold"), bg="tomato2", fg="white")
        text_label.grid(row=0, column=0, padx=20, pady=20)

        scroll_text = ttk.Scrollbar(main, orient=VERTICAL)
        text_box = Text(main, height=13, width=40, pady=10, yscrollcommand=scroll_text.set, bg='white')
        text_box.grid(row=1, column=0, pady=1, padx=1)
        scroll_text.config(command=text_box.yview)
        scroll_text.grid(row=1, column=1, sticky='NS')

        key_label = Label(main, text="Enter key: ", font=('fixedsys', 14), pady=15,
                          bg='black', fg="cyan")
        key_label.grid(row=2, column=0)

        scroll_text2 = ttk.Scrollbar(main, orient=VERTICAL)
        new_text = Text(main, height=13, width=40, pady=10, yscrollcommand=scroll_text2.set, bg='white')
        new_text.grid(row=1, column=2, columnspan=2, padx=(10, 0))
        scroll_text2.config(command=new_text.yview)
        scroll_text2.grid(row=1, column=4, sticky='NS')
        return text_box, new_text
        #############################################################################################################################

    def caesar_cipher():
        # 1st cipher

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

        def encrypt():
            new_text.delete('1.0', END)
            txt = text_box.get("1.0", END)
            key = int(list_key.get())
            enc_text = caesarC.hacking(txt)
            new_text.insert(1.0, enc_text)

        enc = Button(main, text="hacking", bd=10, width=10, command=encrypt, bg='tomato2', fg='white')
        enc.grid(row=0, column=2, padx=20, pady=30)

    ############################################################################################################################

    def RSA():
        remove()

        list_key = ttk.Combobox(main)
        list_key['values'] = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        list_key.current(0)
        list_key.grid(row=5, column=0)

        list_key1 = ttk.Combobox(main)
        list_key1['values'] = (
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26)
        list_key1.current(0)
        list_key1.grid(row=6, column=0)

        text_box, new_text = lab()
        sample = "Sample text input:\nAny character\n\nSample public Key input:\nnumerical value 1-26\nDefault: 1"
        new_text.insert(1.0, sample)

        def encrypt():
            new_text.delete('1.0', END)
            txt = text_box.get("1.0", END)
            key = int(list_key.get())
            key1 = int(list_key1.get())
            enc_text = RSAC.encrypt((key, key1), txt)
            new_text.insert(1.0, enc_text)

        enc = Button(main, text="Encrypt", bd=10, width=10, command=encrypt, bg='tomato2', fg='white')
        enc.grid(row=0, column=2, padx=20, pady=30)

        def decrypt():
            new_text.delete('1.0', END)
            txt = text_box.get("1.0", END)
            key = int(list_key.get())
            key1 = int(list_key1.get())
            dec_text = RSAC.decrypt((key, key1), txt)
            new_text.insert(1.0, dec_text)

        dec = Button(main, text="Decrypt", bd=10, width=10, command=decrypt, bg='tomato2', fg='white')
        dec.grid(row=0, column=3, padx=10, pady=10)

        def hacking():
            new_text.delete('1.0', END)
            txt = text_box.get("1.0", END)
            key = int(list_key.get())
            key1 = int(list_key1.get())
            dec_text = RSAC.hacking((key, key1), txt)
            new_text.insert(1.0, dec_text)

        dec = Button(main, text="Hacking", bd=10, width=10, command=hacking, bg='tomato2', fg='white')
        dec.grid(row=0, column=4, padx=10, pady=10)

    caesar = Button(left_frame, padx=20, bd=10, text='Caesar Cipher', width=20, height=3, command=caesar_cipher,
                    bg='white', fg='red', activebackground='black', font=('arial', 12, 'bold'),
                    activeforeground='SeaGreen1')
    caesar.grid(row=1, column=0)
    caesar = Button(left_frame, padx=20, bd=10, text='RSA', width=20, height=3, command=RSA, bg='white', fg='red',
                    activebackground='black', font=('arial', 12, 'bold'), activeforeground='SeaGreen1')
    caesar.grid(row=2, column=0)
    window.mainloop()


#####################################################################################################################


Welcome_label = Label(root, text="Welcome to Cryptography ciphers", padx=10, pady=20, fg="black",
                      font=("Arial", 20, "bold")).place(x=500,y=320)
chiper_button = Button(root, text="Cryptocypher", padx=20, bd=10, width=20, height=3, command=cipher, bg="black",
                       fg="white",font=("Arial",10,"bold"))
chiper_button.place(x=620,y=430)


root.mainloop()