from tkinter import * 

root = Tk()
root.title("Note page")
root.geometry("1000x500")

label_1 = Label(root, text="Notes", bg= "grey", font=("Helvtica", 18))
label_1.pack()

#Created a list that has all needed classes
Classes = [
"Math",
"English",
"History",
"Lunch",
"Economics",
"Business",
"Physical Education"
] 

master = Tk()

variable = StringVar(master)
variable.set(Classes[0]) 

w = OptionMenu(master, variable, *Classes)
w.pack()

#Need to creat a tab to write text for the user and an add button




root.mainloop()