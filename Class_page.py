from tkinter import * 


root = Tk()
root.title("Class page")
root.geometry("1000x500")

Classes = [
"User 1",
"User 2",
"User 3"

] 

master = Tk()

variable = StringVar(master)
variable.set(Classes[0]) 

w = OptionMenu(master, variable, *Classes)
w.pack()



list_1 = IntVar()

user_1 = Radiobutton(root, text="Math", variable=list_1, value=1).pack()
user_2 = Radiobutton(root, text="English", variable=list_1, value=2).pack()


root.mainloop()