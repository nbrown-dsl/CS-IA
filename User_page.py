from tkinter import * 
import tkinter as tk 
from tkinter import ttk 

root = Tk()
root.title("User page")
root.geometry("1000x500")

v = tk.StringVar()
def setText(word):
    v.set(word)

def clicked(): 
    Add_button = Label(root, text="Welcome").pack() 

User_label = Label(root, text="Users", font=("Helvtica", 16))
User_label.pack()

User_Name = Entry(root, width= 30, font=("Helvetica", 15 ), command= setText("Insert Name"))
User_Name.pack()

Add_button = Button(root, text="ADD", command=clicked)
Add_button.pack()




root.mainloop()