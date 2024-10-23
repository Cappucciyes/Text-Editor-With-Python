from tkinter import *
from tkinter import ttk

from interface.LoadButton import LoadButton
from interface.SaveButton import SaveButton


class ToolBar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # frame that holds everything in the toolbar
        self.toolbarFrame = ttk.Frame(self, width=100, height=100)
        self.toolbarFrame.grid(row=0, column=0)

        # attaching save button to toolbarFrame
        self.saveButton = SaveButton(self.toolbarFrame)
        self.saveButton.grid(column=0, row=0)

        # attaching load button to toolbarFrame
        self.loadButton = LoadButton(self.toolbarFrame)
        self.loadButton.grid(column=1, row=0)
