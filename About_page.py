from tkinter import * 
from tkinter import messagebox 

root = Tk()
root.title("About page")
root.geometry("1000x500")

#messagebox

def popup():
    messagebox.showinfo("About the application", "This application was produced for...")

Button(root, text="About the application", command=popup).pack()




root.mainloop()