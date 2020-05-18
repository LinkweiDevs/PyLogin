from tkinter import*

def main_screen():
    screen = Tk()
    screen.geometry("720x1440")
    screen.title("Notes 1.01")
    Label(text = "Notes ", bg = "grey", width = "300", height = "2",font = ("calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "Login",height = "2", width = "30",bg = "green").pack()
    Label(text = "").pack()
    Button(text = "Register", height= "2", width = "30", bg = "blue").pack()

    screen.mainloop()

main_screen()