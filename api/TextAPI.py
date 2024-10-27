import inspect
from tkinter import *
from tkinter import ttk


class TextAPI():
    textBody = None

    def __init__(self, textBody=None):
        if textBody == None and self.textBody == None:
            self.textBody = TextBody()
        else:
            self.textBody = TextBody(textBody)

    def saveText(self):
        print("Saved Text")

    def loadText(self):
        print("Loaded Text")

        popup = Tk()
        subFrame = ttk.Frame(popup)
        subFrame.grid(column=0, row=0, sticky=(N, W, E, S))

        label = ttk.Label(subFrame, text="this is Load Window!")
        label.grid(row=0, column=0)

        popup.mainloop()


class TextBody():
    def __init__(self):
        self.text = None

    def createSnapShot(self):
        return TextBodyMemento(self)


class TextBodyMemento():
    def __init__(self, TextBody):
        self.fingerPrint = dict(inspect.getmembers(TextBody))


def main():
    testObj = TextBodyMemento(TextBody())
    attributesAndMethods = filter(lambda x: (len(x) < 2) or (
        x[0] != '_' and x[1] != '_'), testObj.__dict__.keys())

    print(testObj.fingerPrint)
    print(list(attributesAndMethods))


if __name__ == "__main__":
    main()
