from tkinter import * 
from .User_page import *

root = Tk()
root.title("Class page")
root.geometry("1000x500")


list = IntVar()

user_1 = Radiobutton(root, text="Math", variable=v, value=1)
user_2 = Radiobutton(root, text="Math", variable=v, value=1)
user_3 = Radiobutton(root, text="Math", variable=v, value=1)


root.mainloop()