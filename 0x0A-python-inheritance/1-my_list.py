#!/usr/bin/python3

"""class Mylist that inherits list"""

class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
