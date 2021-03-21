from tkinter import * 

root = Tk()
root.title("Note page")
root.geometry("1000x500")

def clicked(): 
    input= Name.get()
    user_name = label(root, text = "welcome" + input)
    user_name.pack()

User = Label(root, text="Please enter Username:")
User.pack()

user_name = Entry(root, font=("Helvetica",15))
user_name.pack(pady=20)

button_1 = Button(root, text="ADD", command=clicked)
button_1.pack(pady=20)



#add messagebos for buttons, yes or no prompt


root.mainloop()