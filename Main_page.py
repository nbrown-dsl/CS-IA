from tkinter import *
import About_page, Class_page, Note_page, User_page
import time 
import os


root = Tk()
root.title("Welcome to TASP!")
root.geometry("1000x500")


#Navigation bar
def our_command():
    pass

nav_menu = Menu(root)
root.config(menu=nav_menu)

file_Main = Menu(nav_menu)

nav_menu.add_cascade(label="Menu", menu = file_Main)

file_Main.add_command(label="Main Page", command=our_command)

file_Main.add_command(label="About Page", command=About_page.aboutinfo)

file_Main.add_command(label="User Page", command=lambda : User_page.clicked(root))

file_Main.add_command(label="Notes Page", command=lambda : Note_page.note(root))

file_Main.add_command(label="Class Page", command=lambda : Class_page.classpage(root))

file_Main.add_separator()

file_Main.add_command(label="Exit application", command=root.quit)

#Title
label_1 = Label(root, text="Welcome to TASP!", bg= "grey", font=("Helvtica", 18))
label_1.pack()
label_2 = Label(root, text="Tangeni's Aspirational Scheduling Planner!", bg= "grey", font=("Helvtica", 18))
label_2.pack(pady=50)

#possibly make the background of the clock grey or something, shouldn't just be white
class App(Frame):

    def __init__(self,master=None):

        Frame.__init__(self, master)

        self.master = master

        self.label = Label(text="", fg="Black", font=("Helvtica", 18))

        self.label.place(x=50,y=80)

        self.update_clock()

    def update_clock(self):

        now = time.strftime("%H:%M:%S")

        self.label.configure(text=now)

        self.after(1000, self.update_clock)

root2 = Tk()

app=App(root2)

root2.wm_title("Tkinter clock")

root2.geometry("400x400")

root2.after(1000, app.update_clock)

root.mainloop()