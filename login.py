from tkinter import*

def main_screen():
    screen = Tk()
    screen.geometry("720x1440")
    screen.title("SAMPLE LOGIN PAGE")
    Label(text = "LOG IN SCREEN ", bg = "grey", width = "300", height = "2",font = ("calibri", 13)).pack()
    Label(text = "").pack()
    Button(text = "LOGIN",height = "2", width = "30",bg = "green").pack()
    Label(text = "").pack()
    Button(text = "REGISTER", height= "2", width = "30", bg = "blue").pack()

    screen.mainloop()

main_screen()