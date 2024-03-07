from tkinter import *
import ttkbootstrap as tb
import pybricks as file
from pybricks.pupdevices import Motor
from pybricks.parameters import Port
from pybricks.parameters import Stop
from pybricks.hubs import PrimeHub
import micropython
from pybricks.tools import wait

hub = PrimeHub()

Bal_motor = Motor(Port.B)


root = tb.Window(themename="superhero")

#root = Tk()
root.title("TTK Bootstrap! Slider/Scale")
root.iconbitmap('c:/Users/VarjasiTeodorIstván/Videos/')
root.geometry('500x350')


def scaler(e):
	my_label.config(text=f'{int(my_scale.get())}%')
	sesbesség = int(my_scale.get())
	print(sesbesség)
	Bal_motor.run(sesbesség)

# Create a Scale/Slider
my_scale = tb.Scale(root, bootstyle="warning",
	length=400,
	orient="horizontal",
	from_=0,
	to=100,
	command=scaler,
	state="normal")
my_scale.pack(pady=50)

# Create a label
my_label = tb.Label(root, text="", font=("Helvetica", 18))
my_label.pack()


root.mainloop()