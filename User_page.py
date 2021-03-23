from tkinter import * 



def clicked(root): 
    Name = Entry(root, font=("Helvetica",15))
    Name.pack()
    input= Name.get()
    user_name = Label(root, text = "welcome" + input)
    user_name.pack()

    User = Label(root, text="Please enter Username:")
    User.pack()

    user_name = Entry(root, font=("Helvetica",15))
    user_name.pack(pady=20)

    button_1 = Button(root, text="ADD", command=clicked)
    button_1.pack(pady=20)



#add messagebos for buttons, yes or no prompt


