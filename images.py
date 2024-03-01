from tkinter import *
from PIL import ImageTk, Image
root = Tk()

root.title("Videók")
root.iconbitmap('c:/Users/varja/Videos/')

kép = ImageTk.PhotoImage(Image.open("c:/Users/varja/Videos/netfit.png"))

kilépés = Button(root, text="kilépés", padx="20", pady="20", borderwidth="3", command=root.quit)
kilépés.pack()

címke = Label(root, image=kép)
címke.pack()

root.mainloop()