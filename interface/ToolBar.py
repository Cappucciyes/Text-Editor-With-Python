from tkinter import *
from tkinter import ttk

from interface.LoadButton import LoadButton
from interface.SaveButton import SaveButton


class ToolBar(ttk.Frame):
    # this class is to:
    # - place correct tools in correct places in the tool bar
    # - assign correct functions to correct tools
    def __init__(self, parent, textAPI):
        super().__init__(parent)
        # frame that holds everything in the toolbar
        self.toolbarFrame = ttk.Frame(self, width=100, height=100)
        self.toolbarFrame.grid(row=0, column=0)

        # attaching save button to toolbarFrame
        self.saveButton = SaveButton(self.toolbarFrame, textAPI.saveText)
        self.saveButton.grid(column=0, row=0)

        # attaching load button to toolbarFrame
        self.loadButton = LoadButton(self.toolbarFrame, textAPI.loadText)
        self.loadButton.grid(column=1, row=0)
