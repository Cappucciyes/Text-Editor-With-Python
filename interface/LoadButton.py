from tkinter import *
from tkinter import ttk


class LoadButton(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.button = ttk.Button(self, text="Load", command=self.loadText)
        self.button.grid(column=0, row=0, padx=1, pady=1)

    def loadText(self):
        print("Load Button Pressed")
