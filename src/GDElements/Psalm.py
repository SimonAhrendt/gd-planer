from GDElements.BibleText import BibleText

class Psalm(BibleText):

    def __init__(self, psalm_number=None, EG_Number=None, psalm_translation=None):

        super().__init__(translation=psalm_translation)
        self.type_string = "Psalm"
        self.psalm_number = psalm_number
        self.EG_number = EG_Number

        #self.translation = translation

    # A method to print this object to console for testing
    def print(self):
        super().print()
        print("Psalmnummer: "+str(self.psalm_number))
        print("Nummer im EG: "+str(self.EG_number))