from tkinter import *

root = Tk()

def végrehajtás():
    címke = Label(root, text="Welcome on Teofone Hungary ZRT. webpage")
    címke.pack()

# A command végrahjtja a függvényt
# fg: betűszínét állítja; bg: a háttérszínet állítja

gomb = Button(root, text="KATTINTS IDE", padx=20, pady=20, command=végrehajtás, fg="red", bg="green", font=("Helvetica", 16))

gomb2 = Button(root, text="Ide már nem lehet", state=DISABLED)
gomb2.pack()
gomb.pack()
root.mainloop()