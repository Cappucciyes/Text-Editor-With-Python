from interface.mainInterface import EditorInterface
from api.TextAPI import TextAPI


class MainProcessManager():
    interface = None
    # this will be the API of that will contain all the functions regarding actions for text
    textAPI = TextAPI()

    def __init__(self):
        if self.interface == None:
            self.interface = EditorInterface(self.textAPI)
            self.interface.startInterface()

    def openInterface(self):
        if self.interface == None:
            self.interface = EditorInterface(self.textAPI)

        self.interface.startInterface()


def main():
    mainProcessManager = MainProcessManager()
    mainProcessManager.openInterface()


if __name__ == "__main__":
    main()
