from interface.mainInterface import EditorInterface


class MainProcessManager():
    interface = None

    def __init__(self):
        if self.interface == None:
            self.interface = EditorInterface()
            self.interface.startInterface()

    def openInterface(self):
        if self.interface == None:
            self.interface = EditorInterface()
            self.interface.startInterface()


def main():
    mainProcessManager = MainProcessManager()
    mainProcessManager.openInterface()


if __name__ == "__main__":
    main()
