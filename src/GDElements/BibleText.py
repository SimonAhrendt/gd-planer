from GDElement import GDElement

class BibleText(GDElement):

    def __init__(self, translation=None):
        super().__init__()
        self.translation = translation
        self.type_string = "BibleText"

    # A method to print this object to console for testing
    def print(self):
        super().print()
        print("Translation: " + str(self.translation))

