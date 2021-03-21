from tkinter import * 
from tkinter import messagebox 

root = Tk()
root.title("About page")
root.geometry("1000x500")

#messagebox

def popup():
    messagebox.showinfo("About the application", "This application was produced for...")

Button(root, text="About the application", command=popup).pack(pady=30)


def popup():
    messagebox.showinfo("Updates and Future plans", "This application was produced for...")

Button(root, text="Updates and Future plans", command=popup).pack(pady=30)

root.mainloop()