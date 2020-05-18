from tkinter import *

global screen

screen = Tk()

def register():
    global reg_screen
    reg_screen = Toplevel(screen)
    reg_screen.title("Create Account")
    reg_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
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

    Button(reg_screen, text = "Register", width = 10, height = 1, bg = "blue", command = register_user).pack()


def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")

    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(reg_screen, text = "Sign Up successful", fg = "green", font = ("calibri", 11)).pack()
