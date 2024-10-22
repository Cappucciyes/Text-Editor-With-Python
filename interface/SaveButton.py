from tkinter import *
from tkinter import ttk


class SaveButton(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.button = ttk.Button(self, text="Save", command=self.saveText)
        self.button.grid(column=0, row=0, padx=1, pady=1)

    def saveText(self):
        print("Save Button Pressed")
