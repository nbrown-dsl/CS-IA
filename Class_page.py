from tkinter import * 


def classpage(root):

    Classes = [
    "User 1",
    "User 2",
    "User 3"

    ] 

    

    variable = StringVar(root)
    variable.set(Classes[0]) 

    w = OptionMenu(root, variable, *Classes)
    w.pack()



    list_1 = IntVar()

    user_1 = Radiobutton(root, text="Math", variable=list_1, value=1).pack()
    user_2 = Radiobutton(root, text="English", variable=list_1, value=2).pack()


