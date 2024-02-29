from tkinter import *

root = Tk()

def Myclick():
    címke = Label(root, text="A megadott név: " + e.get(), bg="red", fg="white", borderwidth="3")
    címke.pack()

e = Entry(root, width="100", borderwidth="3", bg="blue", fg="white")
e.pack()
e.insert(0, "Enter your username! \n")

gomb = Button(root, text="Kiíratás", padx=12, pady=12, command=Myclick)
gomb.pack()

root.mainloop()