from tkinter import*
from Registration.register import *

#This is the main login screen function
def main_screen():
    screen.geometry("720x1440") #Screen resolution
    screen.title("SAMPLE LOGIN PAGE")
    Label(text = "LOG IN SCREEN ", bg = "grey", width = "300", height = "2",font = ("calibri", 13)).pack()
    Label(text = "").pack()

    #The Login button
    Button(text = "LOGIN",height = "2", width = "30",bg = "green",command = login_).pack()
    Label(text = "").pack()

    #The Register button
    Button(text = "REGISTER", height= "2", width = "30", bg = "blue", command = register).pack()

    screen.mainloop()

#Call the function to run infinitely
main_screen()
