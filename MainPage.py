from tkinter import font
from PIL import *
from tkinter import *
from PIL import ImageTk,Image
import DALC


def Main_Page():
    window  = Tk()
    window.title("BookShelf System")
    window.iconbitmap("./Icons/bookshelf.ico")
    window.geometry("700x500")
    window.resizable(False,False)

    # Background Image
    backgroundIMG = PhotoImage(file="./Icons/Book_and_light.gif")
    Label_Bg = Label(window, image=backgroundIMG,width=800,height=500)
    Label_Bg.place(x=0,y=0,relwidth=1,relheight=1)


    # SELECTED BOOK
    def getSelectedBook(event):
        try:
            global selectedBook
            index = listBox.curselection()[0]
            selectedBook = listBox.get(index)
            Title_entry.delete(0,END)
            Title_entry.insert(END,selectedBook[1])
            Author_entry.delete(0,END)
            Author_entry.insert(END, selectedBook[2])
            Date_entry.delete(0,END)
            Date_entry.insert(END, selectedBook[3])
            ISBN_entry.delete(0,END)
            ISBN_entry.insert(END, selectedBook[4])
        except IndexError:
            pass


    # Widgets
    Welcome_label = Label(window, text="Welcome To BookShelf  ",font=("Arial",25),fg="white", bg="black",)
    Welcome_label.place(x=200,y=10)


    Title_label = Label(window,text="Title: ", fg="white", bg="black", font=("Arial",15))
    Title_label.place(x=10,y=80)

    titleText = StringVar()
    Title_entry = Entry(window, textvariable=titleText,width=40)
    Title_entry.place(x=70,y=85)

    Author_label = Label(window,text="Author:", fg="white", bg="black", font=("Arial",15))
    Author_label.place(x=5,y=120)

    authorText = StringVar()
    Author_entry = Entry(window, textvariable=authorText,width=40)
    Author_entry.place(x=70,y=125)

    Date_label = Label(window,text="Date:", fg="white", bg="black", font=("Arial",15))
    Date_label.place(x=320,y=120)

    dateText = StringVar()
    ISBN_entry = Entry(window, textvariable=dateText,width=40)
    ISBN_entry.place(x=390,y=125)

    Date_label = Label(window,text="ISBN:", fg="white", bg="black", font=("Arial",15))
    Date_label.place(x=320,y=80)

    isbnText = StringVar()
    Date_entry = Entry(window, textvariable=isbnText,width=40)
    Date_entry.place(x=390,y=85)


    # ScrollBar
    my_scrollbar = Scrollbar(window, orient=VERTICAL)
    my_scrollbar.place(x=440,y=280)
    

    # List Box
    listBox = Listbox(window,height=15,width=60,yscrollcommand=my_scrollbar.set)
    listBox.place(x=70,y =180)
    listBox.bind('<<ListboxSelect>>',getSelectedBook)
    listBox.configure(yscrollcommand = my_scrollbar.set)

    my_scrollbar.config(command=listBox.yview)






    # Buttons
    def viewBooks():
        listBox.delete(0,END)
        for row in DALC.viewBooks():
            listBox.insert(END,row)

    viewAllButton = Button(window, text = "View All", width = 15, command=viewBooks )
    viewAllButton.place(x=530,y=220)

    
    def addEntry():
        DALC.insertBook(titleText.get(), authorText.get(), dateText.get(), isbnText.get())
        viewBooks()

    addEntryButton = Button(window,text= "Add Entry", width=15,command=addEntry)
    addEntryButton.place(x=530, y=270)

    def updateBook():
        DALC.update(selectedBook[0], titleText.get(), authorText.get(),dateText.get(),isbnText.get())
        viewBooks()

    updateButton = Button(window,text= "Update Entry", width=15,command=updateBook)
    updateButton.place(x=530, y=320)

    def deleteBook():
        DALC.deleteBook(selectedBook[0])
        viewBooks()

    deleteButton = Button(window,text= "Delete Book", width=15,command=deleteBook)
    deleteButton.place(x=530, y=370)


    def exit():
        window.destroy()

    closeButton = Button(window,text= "Exit", width=15,command=exit)
    closeButton.place(x=530, y=420)

    window.mainloop()


