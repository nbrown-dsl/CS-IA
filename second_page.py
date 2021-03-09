from tkinter import * 

root = Tk()
root.title("Second page")
root.geometry("1000x500")

def clicked(): 
    label_12= Label(root, text= "About the app").pack()

def clicked(): 
    label_12= Label(root, text= "Users").pack()

def clicked(): 
    label_12= Label(root, text= "Notes").pack()




label_1 = Label(root, text="Welcome!")
label_1.pack()
label_2 = Label(root, text="to Tangeni's scheduling app!")
label_2.pack(pady=50)

button_l = Button(root, text="about", command=clicked)
button_l.pack(pady= 20)

button_l = Button(root, text="Users", command=clicked)
button_l.pack(pady= 20)

button_l = Button(root, text="Notes", command=clicked)
button_l.pack(pady= 20)