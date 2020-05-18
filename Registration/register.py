from tkinter import *

global screen
screen = Tk()

def register():
    reg_screen = Toplevel(screen)
    reg_screen.title("Create Account")
    reg_screen.geometry("300x250")

    username = StringVar()
    password = StringVar()

    Label(reg_screen, text = "Enter the details below", bg = "blue").pack()
    Label(reg_screen, text = "").pack()

    username_label = Label(reg_screen, text = "Username ")
    username_label.pack()

    username_entry = Entry(reg_screen, textvariable = username)
    username_entry.pack()

    password_entry = Entry(reg_screen, textvariable = password, show = '*')
    password_entry.pack()

    Button(reg_screen, text = "Register", width = 10, height = 1, bg = "blue").pack()
