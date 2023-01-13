#!/usr/bin/python3

"""class Mylist that inherits list"""

class Mylist(list):
    """a subclass of list"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))