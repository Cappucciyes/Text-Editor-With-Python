from tkinter import *
from tkinter import ttk


class TextDisplay(ttk.Frame):
    def __init__(self, parent, textAPI):
        super().__init__(parent)

        self.textBody = Text(self)
        self.textBody.grid(row=0, column=0, sticky=(N, W, E, S))
