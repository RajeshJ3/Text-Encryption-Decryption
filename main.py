##############################################
##  Data Encryption / Decryption software   ##
##############################################

# Software is not using any predefined encryption library.
# The encryption algo. is completely designed by me.

from tkinter import *
import decryption 

def about_press():                        # Action for 'About' button (2nd window)
    about_win = Tk()
    about_win.title("About")
    about_win.resizable(0,0)              # Can't be resized

    L1 = Label(about_win, text="About the app", width=40, font=("Helvetica", 15), underline=0)
    L1.grid(row=0, column=0, columnspan=5, padx=10, pady=5)

    L2 = Label(about_win, text="Author:", font=("Helvetica", 12), underline=0)
    L2.grid(row=1, column=0,)
    
    L3 = Label(about_win, text="Github:", font=("Helvetica", 12), underline=0)
    L3.grid(row=2, column=0,)

    L4 = Label(about_win, text="E-mail:", font=("Helvetica", 12), underline=0)
    L4.grid(row=3, column=0,)

    L5 = Label(about_win, text="Donate:", font=("Helvetica", 12), underline=0)
    L5.grid(row=4, column=0,)

    L6 = Label(about_win, text="Version:", font=("Helvetica", 12), underline=0)
    L6.grid(row=5, column=0,)

    L2_ = Label(about_win, text="Rajesh Joshi", font=("Helvetica", 12))
    L2_.grid(row=1, column=1, padx=0, pady=3)
    
    L3_ = Label(about_win, text="https://github.com/Rajesh-Joshi-Rj", font=("Helvetica", 12))
    L3_.grid(row=2, column=1, padx=0, pady=3)

    L4_ = Label(about_win, text="JoshiRajesh448@gmail.com", font=("Helvetica", 12))
    L4_.grid(row=3, column=1, padx=0, pady=3)

    L5_ = Label(about_win, text="PayTm / Paypal(above email)", font=("Helvetica", 12))
    L5_.grid(row=4, column=1, padx=0, pady=3)
    
    L6_ = Label(about_win, text="V 1.0", font=("Helvetica", 12))
    L6_.grid(row=5, column=1, padx=0, pady=3)

    L7_ = Label(about_win, text="This Encryption / Decryption software is using Python's \n and tkinter module only. This is my second desktop app programmed \n in Python. Software may have some bugs. But i'll be updating  \n this frequently.", font=("Helvetica", 10))
    L7_.grid(row=6, column=0, columnspan=5,padx=0, pady=3)
    

    about_win.mainloop()

window = Tk()
window.title('Encryption')
window.resizable(0,0)

inputValue=''
def retrieve_input():
    inputValue=text1.get("1.0","end-1c")
    inputValue = decryption.encryption(inputValue)
    text2.insert(INSERT, inputValue)
    # return inputValue

def decrypt_command():
    window2 = Tk()
    window2.title('Decryption')
    window2.resizable(0,0)

    inputValues = ''
    def retrieve_enc_input():
        inputValues=text10.get("1.0","end-1c")
        inputValues = decryption.decrypy(inputValues)
        text20.insert(INSERT, inputValues)
        # return inputValues

    l10 = Label(window2, text='Enter encrypted message', font=("Helvetica 18 bold", 15)) 
    l10.grid(row = 0, column = 0, padx=0, pady=10)

    b10 = Button(window2, text='Decrypt', width = 10, command=retrieve_enc_input, borderwidth=1, font=("", 11), underline=0)
    b10.grid(row = 0, column = 1, padx=0, pady=10)

    b30 = Button(window2, text='exit', command=window2.destroy, width = 5, borderwidth=0, font=("", 11), underline=0)
    b30.grid(row = 0, column = 2, padx=0, pady=10)

    text10 = Text(window2, height=6, width=80)
    text10.grid(row=1, column=0, columnspan=3, padx=10, pady=0)


    l20 = Label(window2, text='Message',  font=("Helvetica 18 bold", 15)) 
    l20.grid(row = 2, column = 0, padx=0, pady=10)

    text20 = Text(window2, height=6, width=80)
    text20.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

    window2.mainloop()

l1 = Label(window, text='Enter message', font=("Helvetica 18 bold", 15)) 
l1.grid(row = 0, column = 0, padx=0, pady=10)

b1 = Button(window, text='Encrypt', width = 10, command=retrieve_input, borderwidth=1, font=("", 11), underline=0)
b1.grid(row = 0, column = 1, padx=0, pady=10)

b3 = Button(window, text='About', width = 5, borderwidth=0, command=about_press, font=("", 11), underline=0)
b3.grid(row = 0, column = 2, padx=0, pady=10)

text1 = Text(window, height=6, width=80)
text1.grid(row=1, column=0, columnspan=3, padx=10, pady=0)


l2 = Label(window, text='Encrypted message',  font=("Helvetica 18 bold", 15)) 
l2.grid(row = 2, column = 0, padx=0, pady=10)

b2 = Button(window, text='Decrypt message',command=decrypt_command, width = 15, borderwidth=0, font=("", 11), underline=0)
b2.grid(row = 2, column = 1, columnspan=2, padx=0, pady=10)


text2 = Text(window, height=6, width=80)
text2.grid(row=3, column=0, columnspan=3, padx=10, pady=5)

window.mainloop()