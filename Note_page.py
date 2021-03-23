from tkinter import * 

def note(root):

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

    

    variable = StringVar(root)
    variable.set(Classes[0]) 

    w = OptionMenu(root, variable, *Classes)
    w.pack()

    #Need to creat a tab to write text for the user and an add button




