from tkinter import * 
from tkinter import messagebox 

root = Tk()
root.title("About page")
root.geometry("1000x500")

#messagebox



def aboutinfo():
    messagebox.showinfo("About the application", "This application was produced for...")

Button(root, text="About the application", command=aboutinfo).pack(pady=30)


def futureinfo():
    messagebox.showinfo("Updates and Future plans", "This application was produced for...")

Button(root, text="Updates and Future plans", command=futureinfo).pack(pady=30)

root.mainloop()