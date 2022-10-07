from Models import *
from DALC import *
from tkinter import *

def check_login(email,pwd):
    for user in getAllUsers():
        if user.email == email and user.password == pwd:
            Logged_user.id = user.id
            Logged_user.name = user.name
            Logged_user.email = user.email
            Logged_user.password = user.password
            Logged_user.phone = user.phone
            return True

    return False

def addNewUser(name,email,password,phone):
    user = User()
    user.name = name
    user.password = password
    user.email = email
    user.phone = phone

    addUser(user) 

def emailValidation(email):
    user = User()
    user.email = email
    if user.email.endswith("@gmail.com") or user.email.endswith("@yahoo.com") or user.email.endswith("@hotmail.com"):
        return True


Logged_user = User()