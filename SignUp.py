from tkinter import *
from tkinter import messagebox
from BLC import *
from PIL import *
from PIL import ImageTk,Image
from BLC import *
import tkinter as tk
from MainPage import Main_Page


def signUp():
    window = Tk()
    window.title("BookShelf System")
    window.iconbitmap("./Icons/bookshelf.ico")
    window.geometry("700x500")
    window.resizable(False,False)


    backgroundIMG = PhotoImage(file="./Icons/Book_and_light.gif")
    Label_Bg = Label(window, image=backgroundIMG,width=800,height=500)
    Label_Bg.place(x=0,y=0,relwidth=1,relheight=1)


    name_label= Label(window,text="Name: ", fg="white", bg="black", font=("Arial",15))
    name_label.place(x=100,y=50)
    name = Entry(window ,width=40)
    name.place(x=200,y=55)


    email_label= Label(window,text="Email: ", fg="white", bg="black", font=("Arial",15))
    email_label.place(x=100,y=120)
    email= Entry(window ,width=40)
    email.place(x=200,y=125)


    password_label= Label(window,text="Password: ", fg="white", bg="black", font=("Arial",15))
    password_label.place(x=90,y=180)
    password= Entry(window ,width=40,show="*")
    password.place(x=200,y=185)




    phone_label= Label(window,text="Phone: ", fg="white", bg="black", font=("Arial",15))
    phone_label.place(x=90,y=240)
    phone = Entry(window ,width=40)
    phone.place(x=200,y=245)




    def exit():
        window.destroy()

    exit_snButton = Button(window,text="Exit",font="bold", width=11,command=exit,bg="white",fg="black")
    exit_snButton.place(x=200 ,y=300 )

    def signup():
        if check_login(email.get(),password.get()):
            messagebox.showwarning("showwarning", "This Email is used before")
        
        elif not emailValidation(email.get()):
            messagebox.showerror("Email Validation Error","Your Email must be like ****@gmail.com")

        else:
                addNewUser(name.get(),email.get(),password.get(),int(phone.get()))
                messagebox.showinfo("showinfo", "Sign up done !!!!")
                name.delete(0,END)
                email.delete(0,END)
                password.delete(0,END)
                phone.delete(0,END)
                window.destroy()
                Main_Page()

    sign_up_button = Button(window,text="Sign up ",font="bold",width=11,command=signup,bg="white",fg="black")
    sign_up_button.place(x=420 ,y = 300)


    window.mainloop()


