from logging import root
from tkinter import *
from tkinter import ttk
from ToolBar import ToolBar


class EditorInterface(Tk):

    def __init__(self):
        super().__init__()
        self.title = "Text Editor"
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.mainFrame = ttk.Frame(
            self, padding="3 3 12 12")

        # grid is now added within the frame
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        # attaching toolbar to the main frame
        self.toolBar = ToolBar(self.mainFrame)
        self.toolBar.grid(column=0, row=0, sticky=(E, W))

    def openInterface(self):
        self.mainloop()


if __name__ == "__main__":
    interface = EditorInterface()
    interface.title = "Interface file is running"
    interface.openInterface()
