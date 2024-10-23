import inspect


class TextAPI():
    textBody = None

    def __init__(self, textBody=None):
        if textBody == None and self.textBody == None:
            self.textBody = TextBody()
        elif textBody == None:
            self.textBody = TextBody(textBody)

    def saveText(self):
        print("Saved Text")

    def loadText(self):
        print("Loaded Text")


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
