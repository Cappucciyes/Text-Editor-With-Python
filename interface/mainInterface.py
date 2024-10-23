from tkinter import *
from tkinter import ttk
from interface.ToolBar import ToolBar
from interface.TextDisplay import TextDisplay


class EditorInterface(Tk):
    # this class's job is placing correct components of interface in correct places
    def __init__(self, textAPI):
        super().__init__()
        self.title = "Text Editor"
        self.connectedAPI = textAPI
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.mainFrame = ttk.Frame(self, padding="3 3 12 12")

        # grid is now added within the frame
        self.mainFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        # attaching toolbar to the main frame
        self.toolBar = ToolBar(self.mainFrame, self.connectedAPI)
        self.toolBar.grid(column=0, row=0, sticky=(E, W))

        # attaching text within the frame
        self.textDisplay = TextDisplay(self.mainFrame, self.connectedAPI)
        self.textDisplay.grid(row=1, column=0, sticky=(E, S, N))

    def startInterface(self):
        self.mainloop()


if __name__ == "__main__":
    interface = EditorInterface()
    interface.title = "Interface file is running"
    interface.startInterface()
