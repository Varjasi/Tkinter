from tkinter import *

root = Tk()

#A gomb a root-ban van és a gombra az lesz ráírva, hogy nyomd meg
#disable hatására a gombot nem lehet megnyomni
button1 = Button(root, text="Nyomd meg", state=DISABLED)
button2 = Button(root, text="Nyomd meg ezt is!", padx=50, pady=20)

button1.pack()
button2.pack()

root.mainloop()