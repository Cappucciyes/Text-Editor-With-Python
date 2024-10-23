from tkinter import *
from tkinter import ttk


class SaveButton(ttk.Frame):
    def __init__(self, parent, saveFunction):
        super().__init__(parent)
        self.button = ttk.Button(self, text="Save", command=saveFunction)
        self.button.grid(column=0, row=0, padx=1, pady=1)
