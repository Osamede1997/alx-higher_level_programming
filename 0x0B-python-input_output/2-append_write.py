#!/usr/bin/python3

"""Defines a file-appending function"""


def append_file(filename="", text=""):
    """Append a string to a UTF8 text file.
    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
