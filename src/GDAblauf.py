from GDElements.Psalm import *
from GDElements.BibleText import *
from GDElement import *

class GDAblauf:

    # Initialize GDAblauf
    # Create empty GDAblauf or initialize with template if given
    def __init__(self, ablauf_template=None):

        self.element_list = []
        if ablauf_template is not None:
            self.apply_template(ablauf_template)


    # Apply a Gottesdienstablauf-Template to the current GDAblauf
    def apply_template(self, ablauf_template):
        pass

    # Add a new GDElement to this GDAblauf (at the end))
    def append_element(self, element):
        self.element_list.append(element)

    # Insert a new GDElement to this GDAblauf at a given position
    def insert_element(self, position, element):
        self.element_list.insert(position, element)

    # Delete all entries from this GDAblauf
    def clear(self):
        # Ask the user if they really want to delete
        # REQUIRED: Functionality to ask user to proceed or abandon

        self.element_list.clear()

    # Delete a last element
    def delete_last_element(self):
        self.element_list.pop()

    # Delete a single element by position
    def delete_element_at_position(self, position):
        self.element_list.pop(position)

    # Remove an GDElement from this GDAblauf
    def remove_element(self, element):
        self.element_list.remove(element)

    # Printing to console for tsting purposes
    def print(self):
        if len(self.element_list) == 0:
            print("Leerer Gottesdienstablauf")
        else:
            for element in self.element_list:
                element.print()