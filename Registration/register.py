from tkinter import *

screen = Tk()

#This is the Registration screen called after pressing the Register button
def register():
    global reg_screen #must be global to be accessed everywhere
    reg_screen = Toplevel(screen)
    reg_screen.title("Create Account")
    reg_screen.geometry("300x250") #Resolution of the window

    #Variables must be global to be accessed by other methods
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar() #Strotes a string variable
    password = StringVar()

    #These are labels for user instructions
    Label(reg_screen, text = "Enter the details below", bg = "blue").pack()
    Label(reg_screen, text = "").pack()

    #Label for user instruction to enter username
    username_label = Label(reg_screen, text = "ENTER USERNAME")
    username_label.pack()

    #Set username Entry to appear in text field
    username_entry = Entry(reg_screen, textvariable = username)
    username_entry.pack()

    #Label for user instruction to enter password
    Label(text ="").pack()
    Label(reg_screen,text ="ENTER PASSWORD").pack()

    #Set password entry to appear in text field but hudden as ****
    password_entry = Entry(reg_screen, textvariable = password, show = '*')
    password_entry.pack()

    #This is the submit button that calls the register_user function when clicked
    Button(reg_screen, text = "Register", width = 10, height = 1, bg = "blue", command = register_user).pack()



#This function performs the actual registration by saving user info in a text file
def register_user():

    #Use getter method to store username input into username_info
    username_info = username.get()
    password_info = password.get()

    #Open a file in write mode and store username_info and password_info then close
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()


    #CLear the input on the user entry text field after submitting the info
    #Clears from element 0 to the last element
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    #Label for sign up successful
    Label(reg_screen, text = "Sign Up successful", fg = "green", font = ("calibri", 11)).pack()

    Label(reg_screen,text ="").pack()
    Button(reg_screen, text = "REGISTER", width = 10, height = 1, bg = "blue").pack()

    reg_screen.after(2000, reg_screen.destroy)

def login_():
    global reg_screen
    reg_screen = Toplevel(screen)
    reg_screen.title("LOGIN TO YOUR ACCOUNT")
    reg_screen.geometry("300x250")

    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()

    Label(reg_screen, text = "Enter you details below", bg ="green").pack()
    Label(reg_screen, text = "").pack()

    username_label = Label(reg_screen, text = "ENTER USERNAME")
    username_label.pack()

    username_entry = Entry(reg_screen, textvariable = username)
    username_entry.pack()

    Label(text ="").pack()
    Label(reg_screen,text ="ENTER PASSWORD").pack()

    password_entry = Entry(reg_screen, textvariable = password, show = '*')
    password_entry.pack()

    Label(reg_screen,text ="").pack()
    Button(reg_screen, text = "LOGIN", width = 10, height = 1, bg = "green", command = login_user).pack()


    #funtion to login the user
def login_user():
    username_login = username.get()
    password_login = password.get()

    #This opens a file in append mode
    #Seperates username and password with comma
    #Seperates credentials of each user with a \n
    file = open("credentials.txt", "a")
    file.write(username_login +",")
    file.write(password_login + "\n")
    file.close()

    #Clears the text input field from element 0 (1st) to the END (last)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

    Label(reg_screen, text = "Sign Up successful", fg = "green", font = ("calibri", 11)).pack()

    Label(reg_screen,text ="").pack()
    Button(reg_screen, text = "LOGIN", width = 10, height = 1, bg = "GREEN").pack()

    reg_screen.after(3000, reg_screen.destroy)
