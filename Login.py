
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from BLC import *
from PIL import *
from PIL import ImageTk,Image
from tkinter import *
from SignUp import signUp
from MainPage import Main_Page

window = Tk()
window.title("Login Page")
window.iconbitmap("./Icons/bookshelf.ico")
window.geometry("700x500")
window.resizable(False,False)

# Background Image
backgroundIMG = PhotoImage(file="./Icons/Book_and_light.gif")
Label_Bg = Label(window, image=backgroundIMG,width=800,height=500)
Label_Bg.place(x=0,y=0,relwidth=1,relheight=1)

# Widgets
email_label= Label(window,text="Email: ", fg="white", bg="black", font=("Arial",15))
email_label.place(x=100,y=120)

emailuser = StringVar()
email = Entry(window ,width=40,textvariable=emailuser)
email.place(x=200,y=125)


password_label= Label(window,text="Password: ",fg="white", bg="black", font=("Arial",15))
password_label.place(x=90,y=180)

passworduser = StringVar()
password = Entry(window ,width=40,textvariable= passworduser ,show="*")
password.place(x=200,y=185)

# Buttons

def login():
    if check_login(email.get(),password.get()):
        window.destroy()
        Main_Page()
    else:
        messagebox.showwarning("showwarning", "Invalide email or password")
login_button = Button(window,text="Login",font="bold",width=11 ,bg="white",fg="black",command=login)
login_button.place(x=100,y=300)

def exit():
    window.destroy()

exit_logButton = Button(window,text="Exit",font="bold", width=11,command=exit,bg="white",fg="black")
exit_logButton.place(x=280 ,y=300 )

def signup():
    window.destroy()
    signUp()

singup_Button = Button(window,text="Sign up ",font="bold",width=11,bg="white",fg="black",command=signup)
singup_Button.place(x=460 ,y = 300)

def logout():
    deleteUser(email.get(),password.get())
    messagebox.showwarning("Logout!!!", "You Logged Out !!!!")
    window.destroy()


logout_Button = Button(window,text="Logout ",font="bold",width=8,bg="red",fg="black",command=logout)
logout_Button.place(x=480,y=380)

window.mainloop()









