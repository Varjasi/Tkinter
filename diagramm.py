import customtkinter as ctk
import csv
from tkinter import *

class CTkChart(ctk.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.global_width = self.cget('width')
        self.global_height = self.cget('height')
        self.col = 0

    def y_axis(self, text):
        frame = ctk.CTkFrame(self, fg_color="green", width=(self.global_width/10))
        frame.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")

        sep = ctk.CTkLabel(frame, text="", fg_color="transparent")
        sep.grid(row=0, column=0, padx=2, pady=((self.global_height/10)))

        inner_frame = ctk.CTkFrame(frame, fg_color="transparent", width=(self.global_width/10))
        inner_frame.grid(row=0, column=1, padx=2, pady=0, sticky="n")  

        label = ctk.CTkLabel(frame, text=text, fg_color="transparent", width=20, height=5)
        label.grid(row=0, column=0, padx=0, pady=0)
        label.grid_rowconfigure(0, weight=0)
        label.grid_columnconfigure(0, weight=0)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.bar_height = []
        return inner_frame

    def x_axis(self, text):
        frame = ctk.CTkFrame(self, fg_color="green", height=(self.global_width/10))
        frame.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")
        
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        sep = ctk.CTkLabel(frame, text="", fg_color="green")
        sep.grid(row=0, column=0, padx=(self.global_width/5), pady=2)

        label = ctk.CTkLabel(frame, text=text, fg_color="green", width=40, height=5)
        label.grid(row=0, column=1, padx=0, pady=0)
        return frame

    def chart(self):
        frame = ctk.CTkFrame(self, fg_color="green")
        frame.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        return frame

    def create_bar(self, parent, h, color, value):
        label = ctk.CTkLabel(parent, text="", fg_color=color, width=20, height=h)
        label.grid(row=0, column=self.col, padx=2, pady=2, sticky="s")

        self.bar_height.append(h)

        data = ctk.CTkLabel(parent, text=value, fg_color="transparent", width=20, height=20)
        data.grid(row=1, column=self.col, padx=2, pady=2, sticky="s")
    
    def data_y(self, parent, text, row, l_data, max_value):
        height = max(self.bar_height) / (l_data) * 2
        label = ctk.CTkLabel(parent, text=text, fg_color="transparent", width=20, height=height)
        label.grid(row=l_data - row - 1, column=0, padx=2, pady=0, sticky="n")

    def clear_chart(self):

        for widget in self.winfo_children():
            widget.destroy()

    def create_chart(self, x_values, y_values, color):

        self.clear_chart()

        chart = self.chart()
        x = self.x_axis('test')
        y = self.y_axis("t\ne\ns\nt")

        max_value = max(y_values)

        max_bar_height = self.global_height * 0.8

        for n, value in enumerate(y_values):
            bar_height = (value / max_value) * max_bar_height
            print(f"Bar {n}: value={value}, bar_height={bar_height}")
            self.col = n
            self.create_bar(chart, bar_height, color, value)

        for n, value in reversed(list(enumerate(y_values))):
            if n % 2 == 0:
                label = str(round((value), 2))
                self.data_y(y, label, n, len(y_values), max_value)
                print(f"Label {n}: value={value}, label={label}")

root = Tk()
root.geometry("700x700")

frame = CTkChart(root, height=600)

chart = frame.chart()

x_values = ['Label 1', 'Label 2', 'Label 3', 'Label 4']
y_values = [100, 90, 150, 200]

frame.create_chart(x_values, y_values, "blue")

frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

root.mainloop()