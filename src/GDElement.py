# A class representing a single element of a service (e.g. a psalm, a sermon, a song, ...)

class GDElement:

    TOTAL_ELEMENT_NUMBER = 0

    def __init__(self):
        self.id = GDElement.TOTAL_ELEMENT_NUMBER
        GDElement.TOTAL_ELEMENT_NUMBER += 1
        self.type_string = "GDElement"

    # A method to print this object to console for testing
    def print(self):
        print("Printing GDElement with ID: " + str(self.id) + " and type: " + self.type_string)