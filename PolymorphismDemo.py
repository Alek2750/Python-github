class Document:
    def __init__(self, name):
        self.name = name

    def show(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def pr(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Pdf(Document):
    def show(self):
        return 'Show pdf contents!'
    def pr(self):
        print("Pdf")

class Word(Document):
    def show(self):
        return 'Show word contents!'
    def pr(self):
        print("Word")


def show(Document):
    Document.pr()


pdf1 = Pdf("Pdf")
W1 = Word("Word")
show(pdf1)
show(W1)
